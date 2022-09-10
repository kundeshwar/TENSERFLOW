import tensorflow as tf
#mathmatical operation by using tensorflow
import numpy as np
#a = 10
#b = tf.sqrt(a) it gives error when you gives integer it only accept datatype float16,half,float32,float64,complex64,complex128
#print(b)
a = 10.0
b = tf.sqrt(a)
print(b)

l1 = [4.0,9.0,16.0,25.0]
c = tf.sqrt(l1)
print(c)

t = (4.0,9.0,25.0,16.0)
c = tf.sqrt(t)
print(c)


a = np.array([4.0,25.0,9.0,16.0])
c = tf.sqrt(a)
print(c)

a = np.ones(6).reshape(2,1,3,1)*4
c = tf.sqrt(a)
print(c)


a = tf.convert_to_tensor([4,5,6,9],dtype="float")
c = tf.sqrt(a)
print(c)

a = tf.constant([4,9,25,16],dtype="float")
c = tf.sqrt(a)
print(c)

a = tf.Variable([4,16,25,9],dtype="float")
c = tf.sqrt(a)
print(c)