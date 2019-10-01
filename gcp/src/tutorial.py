import os
import tensorflow as tf
from tensorflow.contrib import tpu
def computation(alpha, x, y):
  return alpha * x + y
alpha = tf.Variable(3.0, name='alpha')
x = tf.Variable(tf.ones([3, 3], tf.float32), name='x')
y = tf.Variable(tf.ones([3, 3], tf.float32), name='y')
tpu_computation = tpu.rewrite(computation, [alpha, x, y])
with tf.Session('grpc://{TPU_IP}:8470'.format(**os.environ)) as sess:
  sess.run(tpu.initialize_system())
  sess.run(tf.global_variables_initializer())
  output = sess.run(tpu_computation)
  print(output)
  sess.run(tpu.shutdown_system())

  print('Done!')