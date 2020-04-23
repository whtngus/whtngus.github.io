# keras v 2.0 class_weight



# Tensorflow v1 -> v2 변경
## Tensorflow import v1 -> v2

from tensorflow.contrib import layers as contrib_layers
-> 변경 : from tensorflow.keras import layers as contrib_layers

from tensorflow.contrib import tpu as contrib_tpu
-> 제거

tf.train.Optimizer
-> 변경 : tf.keras.optimizers.Optimizer

tf.logging
-> 변경 : tf.compat.v1.logging

tf.gfile.GFile
-> 변경 : tf.io.gfile.GFile

 tf.contrib.predictor.from_saved_model
 -> 변경 : tf.lite.TFLiteConverter.from_saved_model

tf.python_io.TFRecordWriter(output_file)
-> 변경 :  tf.io.TFRecordWriter

tf.get_variable   
-> 변경 : tf.Variable
+ parameter initializer -> initial_value
-> 변경2 : tf.compat.v1.get_variable

optimizer 설정
keras 2.2.4 => lr
keras 2.3.0 => learning_rate


- Tensorflow 1.X 버전의 contrib은 대체 불가
https://www.tensorflow.org/guide/migrate?hl=ko
