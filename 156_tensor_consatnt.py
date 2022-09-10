from turtle import shape
import tensorflow as tf
#tf.__version__ it used for to know version of any library of python
#a = tf.constant(10)
#print(a)
#a = tf.constant(10.25)
#print(a)
#a = tf.constant("s")
#print(a)
#a = tf.constant(True)
#print(a)
import numpy as np
#a = tf.constant(np.array([1,5,6,2,3]))
a = tf.constant([[1,5,2],[5,8,6]])
print(a)
b = tf.constant([1,5,3,6,2,0],shape=(2,3))
print(b)
c = tf.constant([[4,6,3],[8,6,3]],dtype=float)
print(c)
print(type(a))
print(a.numpy())#it gives only array
