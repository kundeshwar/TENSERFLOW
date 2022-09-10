import tensorflow as tf
import numpy as np
#subtraction in tensor flow

a = 10
b = 20
e = 50
c = tf.subtract(a,b)
print(c)
l1 = [4,5,2,6]
l2 = [5,2,6,3]
c = tf.subtract(l1,l2)
print(c)
t = (4,5,6,9)
c = tf.subtract(t,l1)
print(c)
c = tf.subtract(a,l1)
print(c)
c = tf.subtract(t,b)
print(c)
a = np.array([4,2,5,3])
b = np.array([4,8,6,9])
c = tf.subtract(a,b)
print(c.numpy())
c = tf.subtract(a,e)
print(c)
c = tf.subtract(a,l1)
print(c)



f = tf.constant([4,5,6,8])
g = tf.constant([7,5,8,6])
c = tf.subtract(f,g)
k = tf.subtract(f,e)
print(k)
print(c)


a = tf.Variable([4,8,5,6])
b = tf.Variable([4,8,9,3])
c = tf.subtract(a,b)
l = tf.subtract(a,f)
print(c)
print(l)
