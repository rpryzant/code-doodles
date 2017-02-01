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













