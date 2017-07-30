import tensorflow as tf
import os
import numpy as np

import model_base
import models
import input_pipeline
import utils.vocab_utils as vocab_utils
from collections import namedtuple

class TrainModel(namedtuple("TrainModel", ('graph', 'model', 'iterator'))):
    pass


def create_train_model(model_creator, config):
    src_file = os.path.join(config.data_dir, "%s.%s" % (config.train_prefix, config.src))
    tgt_file = os.path.join(config.data_dir, "%s.%s" % (config.train_prefix, config.tgt))
    src_vocab_file = os.path.join(config.data_dir, "%s.%s" % (config.vocab_prefix, config.src))
    tgt_vocab_file = os.path.join(config.data_dir, "%s.%s" % (config.vocab_prefix, config.tgt))


    graph = tf.Graph()

    with graph.as_default():
        iterator, tgt_input_table = input_pipeline.get_iterator(
            src_file, tgt_file, src_vocab_file, tgt_vocab_file, config)

        model = model_creator(
            config, iterator, "train", tgt_input_table)

        return TrainModel(graph=graph, model=model, iterator=iterator)


def train(config):
    out_dir = config.out_dir

    if not config.attention:
        model_creator = models.VanillaModel
    else:
        model_creator = models.AttentionModel

    train_model = create_train_model(model_creator, config)

    train_sess = tf.Session(graph=train_model.graph)
    with train_model.graph.as_default():
        loaded_train_model, global_step = model_base.create_or_load_model(
            train_model.model, out_dir, train_sess, "train")

    summary_writer = tf.summary.FileWriter(
        os.path.join(out_dir, "train_log"), train_model.graph)

    train_sess.run(train_model.iterator.initializer)

    while global_step < config.num_train_steps:
        try:
            step_result = loaded_train_model.train(train_sess, debug=True)
            _, loss, predict_count, global_step, summary, src, src_len,  tgt, tgt_len, preds = step_result
            print loss
            print src
            print src_len
            print tgt
            print tgt_len
            print preds
            print
        except tf.errors.OutOfRangeError:
            # epoch is done 
            train_sess.run(train_model.iterator.initializer)




















