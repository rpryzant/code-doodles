""" Implementations of attention layers.
	NOTE: inherits from seq2seq
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import collections

import tensorflow.google as tf
from tensorflow.python.framework import function  # pylint: disable=E0611

from seq2seq.models import AttentionSeq2Seq
from seq2seq.decoders.attention import AttentionLayerBahdanau
from seq2seq import losses as seq2seq_losses
from seq2seq.graph_utils import templatemethod
from seq2seq import graph_utils

def reverse_grad_grad(op, grad):
  return tf.constant(-1.) * grad

@function.Defun(tf.float32, python_grad_func=reverse_grad_grad)
def reverse_grad(tensor):
  return tf.identity(tensor)

class DiscriminatorSeq2Seq(AttentionSeq2Seq):

  def _discriminator(self, encoder_output, features, labels, num_classes, num_units=256):
    # A class discriminator
    # Create attention over the encoder states
    encoder_output_output = encoder_output["outputs"]
    encoder_output_output_shape = encoder_output_output.get_shape()
    encoder_output_att_values = encoder_output["attention_values"]
    encoder_output_att_values_shape = encoder_output_att_values.get_shape()

    if self.params["discriminator_reverse_grad"]:
      encoder_output_output = reverse_grad(encoder_output_output)
      encoder_output_output.set_shape(encoder_output_output_shape)
      encoder_output_att_values = reverse_grad(encoder_output_att_values)
      encoder_output_att_values.set_shape(encoder_output_att_values_shape)

    attention_fn = AttentionLayerBahdanau(params={}, mode=self.mode)
    _, attention_context = attention_fn(
        query=tf.zeros_like(encoder_output["outputs"][:, 0, :]),
        keys=encoder_output_output,
        values=encoder_output_att_values,
        values_length=encoder_output["attention_values_length"])

    # Fully connected layer
    fc1 = tf.contrib.layers.fully_connected(
      inputs=attention_context,
      num_outputs=num_units,
      activation_fn=tf.nn.tanh,
      scope="discriminator_fc")

    # Create logits
    logits = tf.contrib.layers.fully_connected(
      inputs=fc1,
      num_outputs=num_classes,
      activation_fn=None,
      scope="discriminator_softmax")

    losses = tf.nn.sparse_softmax_cross_entropy_with_logits(
        logits=logits, labels=labels["domain"])

    mean_loss = tf.reduce_mean(losses, name="mean_loss")

    return (mean_loss, fc1)

  def _preprocess(self, features, labels):
    features, labels = super(DiscriminatorSeq2Seq, self)._preprocess(
        features, labels)

    # Convert domain string to a class id
    domains = tf.map_fn(
      lambda x: tf.case({
        tf.equal(x, "domain=aspec"): lambda: tf.constant(0),
        tf.equal(x, "domain=subtitles"): lambda: tf.constant(1)},
        default=lambda: tf.constant(-1),
        exclusive=True),
      elems=labels["target_tokens"][:, 1],
      dtype=tf.int32)

    labels["domain"] = domains

    # Remove the domain token from the data
    # Token #0 is SEQUENCE_START. Token #1 is the domain token.
    labels["target_tokens"] = tf.concat(
        [labels["target_tokens"][:, 0:1], labels["target_tokens"][:, 2:]], 1)
    labels["target_ids"] = tf.concat(
        [labels["target_ids"][:, 0:1], labels["target_ids"][:, 2:]], 1)
    labels["target_len"] = labels["target_len"] - 1

    return features, labels

  @staticmethod
  def default_params():
    params = AttentionSeq2Seq.default_params()
    params["discriminator_units"] = 256
    params["discriminator_loss_multiplier"] = 10.0
    params["discriminator_reverse_grad"] = False
    params["discriminator_mix_context"] = False
    return params

  def compute_loss(self, decoder_output, features, labels):
    """Computes the loss for this model.

    Returns a tuple `(losses, loss)`, where `losses` are the per-batch
    losses and loss is a single scalar tensor to minimize.
    """
    #pylint: disable=R0201
    # Calculate loss per example-timestep of shape [B, T]

    # Get the original loss from the model
    losses, loss = super(DiscriminatorSeq2Seq, self).compute_loss(
        decoder_output, features, labels)

    # Add the Discriminator
    encoder_output = graph_utils.get_dict_from_collection("encoder_output")
    with tf.variable_scope("discriminator"):
      discriminator_loss, disc_context = self._discriminator(
        encoder_output=encoder_output,
        features=features,
        labels=labels,
        num_classes=2,
        num_units=self.params["discriminator_units"])

    discriminator_loss *= self.params["discriminator_loss_multiplier"]
    tf.summary.scalar("loss/discriminator", discriminator_loss)
    tf.summary.scalar("loss/generator", loss)

    # Add discriminator loss to original loss (training only)
    if self.mode == tf.contrib.learn.ModeKeys.TRAIN:
      loss = loss + discriminator_loss

    tf.summary.scalar("loss/total", loss)

    return losses, loss

  @templatemethod("encode")
  def encode(self, features, labels):
    res = super(DiscriminatorSeq2Seq, self).encode(features, labels)
    # Add the encoder output to a graph collection so that we can find it.
    dict_items = collections.OrderedDict(zip(res._fields, res))
    dict_items.pop("final_state")
    graph_utils.add_dict_to_collection(dict_items, "encoder_output")

    return res
