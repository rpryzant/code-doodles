import tensorflow as tf
import os

import models
import input_pipeline
import utils.vocab_utils as vocab_utils



def create_train_model(model_creator, config):
    src_file = os.path.join(config.data_dir, "%s.%s" % (config.train_prefix, config.src))
    tgt_file = os.path.join(config.data_dir, "%s.%s" % (config.train_prefix, config.tgt))
    src_vocab_file = os.path.join(config.data_dir, "%s.%s" % (config.vocab_prefix, config.src))
    tgt_vocab_file = os.path.join(config.data_dir, "%s.%s" % (config.vocab_prefix, config.tgt))


    graph = tf.Graph()

    with graph.as_default():
        src_vocab_table, tgt_vocab_table = vocab_utils.create_vocab_tables(
            src_vocab_file, tgt_vocab_file, config.share_vocab)

        src_dataset = tf.contrib.data.TextLineDataset(src_file)
        tgt_dataset = tf.contrib.data.TextLineDataset(tgt_file)

        iterator = input_pipeline.get_iterator(
            src_file,
            tgt_file,
            src_vocab_file,
            tgt_vocab_file,
            config)
        print iterator



def train(config):
    out_dir = config.out_dir
    num_train_steps = config.num_train_steps
    steps_per_stats = config.steps_per_stats
    steps_per_eval = config.steps_per_eval

    if not config.attention:
        model_creator = models.VanillaModel
    else:
        model_creator = models.AttentionModel

    train_model = create_train_model(model_creator, config)
