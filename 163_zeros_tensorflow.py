# how to creat zeos tensor by using any tensor
import tensorflow as tf
import numpy as np
a = tf.constant([[4,5,2],[4,5,6],[8,9,7]])
print(a)
b = tf.zeros((4,4),tf.int16)
print(b)
print(b.numpy())
b = tf.zeros_like(a)
print(b)
c = tf.zeros_initializer()
print(c)


e = np.matrix([[4,5,6],[8,6,2],[4,2,6]])
f = np.matrix([[4,8,6],[7,5,6],[7,2,3]])
print(e+f)
