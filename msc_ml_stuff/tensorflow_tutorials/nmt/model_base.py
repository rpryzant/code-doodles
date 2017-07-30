import abc

import tensorflow as tf
from tensorflow.python.layers import core as layers_core

class BaseModel(object):
    """ sequence to sequence base class
    """
    def __init__(self,
                 config, 
                 iterator, 
                 mode,
                 tgt_vocab_table,
                 reverse_tgt_vocab_table=None):
        if mode == "inference":
            assert reverse_tgt_vocab_table is not None

        self.iterator = iterator
        self.config = config
        self.tgt_vocab_table = tgt_vocab_table

        self.batch_size = config.batch_size
        self.src_vocab_size = config.src_vocab_size
        self.tgt_vocab_size = config.tgt_vocab_size
        self.num_layers = config.num_layers

        self.mode = mode

        # initializer for all matrices
        initializer = tf.random_uniform_initializer(
            -config.init_weight, config.init_weight, seed=config.random_seed)
        tf.get_variable_scope().set_initializer(initializer)

        # init global step
        self.global_step = tf.Variable(0, trainable=False)
        # make embeddings
        self.encoder_embeddings, self.decoder_embeddings = self.make_embeddings()
        # make graph
        self.loss, self.logits, self.sample_ids = self.build_graph()
        if self.mode == 'inference':
            self.sample_words = reverse_tgt_vocab_table.lookup(
                tf.to_int64(self.sample_ids))
        # make training op
        self.train_op = self._make_training_op()

        # tf boilerplate
        self.summaries = tf.summary.merge_all()
        self.saver = tf.trian.Saver(tf.global_variables())


    def make_embeddings(self):
        with tf.variable_scope("embeddings"):
            with tf.variable_scope("encoder"):
                encoder_embeddings = tf.get_variable(
                    "embedding_encoder",
                    [self.src_vocab_size, self.config.src_embed_size])
            with tf.variable_scope("decoder"):
                decoder_embeddings = tf.get_variable(
                    "embedding_decoder",
                    [self.tgt_vocab_size, self.config.tgt_embed_size])

        return encoder_embeddings, decoder_embeddings


    def build_graph(self):
        with tf.variable_scope("encoder"):
            encoder_outputs, encoder_state = self._build_encoder()
        with tf.variable_scope("decoder"):
            logits, sample_ids = self._build_decoder(encoder_outputs, encoder_state)
        with tf.variable_scope("loss"):
            loss = self._compute_loss(logits)
        return loss, logits, sample_ids

    @abc.abstractmethod
    def _build_encoder(self):
        pass


    @abc.abstractmethod
    def _build_decoder_cell(self, encoder_outputs, encoder_state):
        pass


    def _build_decoder(self, encoder_outputs, encoder_state):


        output_layer = layers_core.Dense(
            self.config.tgt_vocab_size, use_bias=False, name="out_projection")

        cell, initial_state = self._build_decoder_cell(
            encoder_outputs, encoder_state)

        # train or eval (argmax)
        if self.mode != 'inference':
            target_input = iterator.target_input
            target_embeddings = tf.nn.embedding_lookup(
                self.decoder_embeddings, target_input)
            # argmax sampler
            sampler = tf.contrib.seq2seq.TrainingHelper(
                target_embeddings, self.iterator.target_sequence_length)

            decoder = tf.contrib.seq2seq.BasicDecoder(
                cell, sampler, initial_state)
            outputs, final_context_state, _ = tf.contrib.seq2seq.dynamic_decode(
                decoder, swap_memory=True)  # move tensors to cpu after computation, avoid memory issues on long seqs

            # applying projection all at once is faster than 
            #    the per-timestep behavior in inference
            logits = output_layer(outputs.rnn_output)
            sample_ids = outputs.sample_id

        # Inference (beam search)
        else:
            tgt_sos_id = tf.cast(self.tgt_vocab_table.lookup(tf.constant(self.config.sos)),
                                 tf.int32)
            tgt_eos_id = tf.cast(self.tgt_vocab_table.lookup(tf.constant(self.config.eos)),
                                 tf.int32)
            beam_width = self.config.beam_width
            length_penalty_weight = self.config.length_penalty_weight
            start_tokens = tf.fill([self.batch_size], tgt_sos_id)
            end_token = tgt_eos_id

            # max decoding steps
            decoding_length_factor = 2.0
            max_encoder_length = tf.reduce_max(iterator.source_sequence_length)
            maximum_iterations = tf.to_int32(tf.round(
                tf.to_float(max_encoder_length) * decoding_length_factor))

            if beam_width > 0:
                decoder = tf.contrib.seq2seq.BeamSearchDecoder(
                    cell=cell,
                    embedding=self.decoder_embeddings,
                    start_tokens=start_tokens,
                    end_token=end_token,
                    initial_state=initial_state,
                    beam_width=beam_width,
                    output_layer=output_layer,
                    length_penalty_weight=length_penalty_weight)
            else:
                # inference argmax sampler
                sampler = tf.contrib.seq2seq.GreedyEmbeddingHelper(
                    self.embedding_decoder, start_tokens, end_token)
                decoder = tf.contrib.seq2seq.BasicDecoder(
                    cell, sampler, initial_state, output_layer=output_layer)

            outputs, final_context_state, _ = tf.contrib.seq2seq.dynamic_decode(
                decoder, maximum_iterations=maximum_iterations, swap_memory=True)

            if beam_width > 0:
                logits = tf.no_op()
                sample_ids = outputs.predicted_ids
            else:
                logits = outputs.rnn_output  # already projected
                sample_id = outputs.sample_id

            return logits, sample_ids



    def _compute_loss(self, logits):
        targets = self.iterator.target_output
        time_axis = 1
        max_time = targets.shape[time_axis].value or tf.shape(targets)[time_axis]

        crossent = tf.nn.sparse_softmax_cross_entropy_with_logits(
            labels=targets, logits=logits)
        target_weights = tf.sequence_Mask(
            self.iterator.target_sequence_length, max_time, dtype=logits.dtype)
        loss = tf.reduce_sum(crossent * target_weights) / tf.to_float(self.batch_size)

        tf.summary.scalar("loss", loss)

        return loss

    def _make_training_op(self):
        optimizer = tf.train.Adamoptimizer(self.config.learning_rate)
        params = tf.trainable_variables()
        gradients = tf.gradients(self.loss, params)
        clipped_gradients, gradient_norm = tf.clip_by_global_norm(
            gradients, self.config.max_gradient_norm)

        tf.summary.scalar("grad_norm", gradient_norm)
        tf.summary.scalar("clipped_norm", tf.global_norm(clipped_gradients))

        train_op = optimizer.apply_gradients(
            zip(clipped_gradients, params), global_step=self.global_step)

        return train_op


    ###########################
    #  utility functions for subclasses
    ###########################
    def _build_rnn_cell(self):
        def _single_cell():
            cell = tf.contrib.rnn.BasicLSTMCell(
                self.config.num_units, forget_bias=self.config.forget_bias)

            dropout = self.config.dropout if self.mode == "train" else 0.0
            cell = tf.contrib.rnn.DropoutWrapper(
                cell = cell, input_keep_prob=(1.0 - dropout))

            return cell

        cell_list = [_single_cell() for _ in range(self.config.num_layers)]

        if len(cell_list) == 1:
            cell = cell_list[0]
        else:
            cell = tf.contrib.rnn.MultiRNNCell(cell_list)

        return cell


    def build_unidirectional_encoder(self, source_embedded):
        cell = self._build_rnn_cell()
        encoder_outputs, encoder_state = tf.nn.dynamic_rnn(
            cell,
            source_embedded,
            sequence_length=self.iterator.source_sequence_length)
        return encoder_outputs, encoder_state


    def build_bidirectional_encoder(self, source_embedded):
        fw_cell = self._build_rnn_cell()
        bw_cell = self._build_rnn_cell()
        bi_output, bi_state = tf.nn.bidirectional_dynamic_rnn(
            fw_cell,
            bw_cell,
            source_embedded,
            sequence_length=self.iterator.source_sequence_length)
        return tf.concat(bi_outputs, -1), bi_state



















