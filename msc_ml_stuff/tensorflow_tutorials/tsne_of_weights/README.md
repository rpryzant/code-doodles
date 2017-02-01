This is a nice little tutorial I came across for how to do visualizations of your weights, etc in tensorflow.

The tutorial itself is here: http://web.stanford.edu/class/cs20si/lectures/notes_04.pdf


Assume that you have an object `model` that has an instance variable `embed_matrix` that is itself a `tf.Variable`

E.g.:

```
class Model:
  def __init__(self):
      self.embed_matrix = tf.Variable(...)
```

now follow this example:

```
from tensorflow.contrib.tensorboard.plugins import projector

# obtain the embedding_matrix after you’ve trained it
final_embed_matrix = sess.run(model.embed_matrix)

# create a variable to hold your embeddings. It has to be a variable. Constants
# don’t work. You also can’t just use the embed_matrix we defined earlier for our model. Why
# is that so? I don’t know. I get the 500 most popular words.
embedding_var = tf.Variable(final_embed_matrix[:500], name='embedding')
sess.run(embedding_var.initializer)
config = projector.ProjectorConfig()
summary_writer = tf.summary.FileWriter(LOGDIR)

# add embeddings to config
embedding = config.embeddings.add()
embedding.tensor_name = embedding_var.name

# link the embeddings to their metadata file. In this case, the file that contains
# the 500 most popular words in our vocabulary
embedding.metadata_path = LOGDIR + '/vocab_500.tsv'

# save a configuration file that TensorBoard will read during startup
projector.visualize_embeddings(summary_writer, config)

# save our embedding
saver_embed = tf.train.Saver([embedding_var])
saver_embed.save(sess, LOGDIR + '/skip-gram.ckpt', 1)
```

Now run the model, go to tensorboard (`http://localhost:6006`), click on the "embeddings" tab, and have at it









