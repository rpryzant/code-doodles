

class BaseModel(object):
    """ sequence to sequence base class
    """
    def __init__(self,
                 config, 
                 iterator, 
                 src_vocab_table, 
                 tgt_vocab_table,
                 mode):

        self.iterator = iterator
        self.config = config
        self.src_vocab_table = src_vocab_table
        self.tgt_vocab_table = tgt_vocab_table

        self.batch_size = self.config.batch_size
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
        self.loss, self.logits = self.build_graph(self)
        # make training op
        self.train_op = self._make_training_op(self)

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
            logits = self._build_decoder(encoder_outputs, encoder_state)
        with tf.variable_scope("loss"):
            loss = self._compute_loss(logits)
        return loss, logits

    @abc.abstractmethod
    def _build_encoder(self):
        pass


    @abc.abstractmethod
    def _build_decoder(self, encoder_outputs, encoder_state):
        pass


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

            if mode == 'train':
                cell = tf.contrib.rnn.DropoutWrapper(
                    cell = cell, input_keep_prob=(1.0 - self.config.dropout))

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



















