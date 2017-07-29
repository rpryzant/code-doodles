



class Model(BaseModel):

    def _build_encoder(self):
        source_embedded = tf.nn.embedding_lookup(
            self.encoder_embeddings, self.iterator.source)

        if self.config.encoder_type == 'uni':
            outputs, encoder_state = self.build_unidirectional_encoder(source_embedded)
        elif self.config.encoder_type == 'bi':
            outputs, state = self.build_bidirectional_encoder(source_embedded)
            # alternate between fw/bw states 
            encoder_state = []
            for layer in range(self.config.num_layers)
                encoder_state.append(state[0][layer])
                encoder_state.append(state[1][layer])
            encoder_state = tuple(encoder_state)

        return outputs, encoder_state



