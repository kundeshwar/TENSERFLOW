import tensorflow as tf
#mathmatical operation by using tensorflow
import numpy as np
a = 10
b = 20
e = 50
c = tf.multiply(a,b)
print(c)
l1 = [4,5,2,6]
l2 = [5,2,6,3]
c = tf.multiply(l1,l2)
print(c)
t = (4,5,6,9)
c = tf.multiply(t,l1)
print(c)
c = tf.multiply(a,l1)
print(c)
c = tf.multiply(t,b)
print(c)
a = np.array([4,2,5,3])
b = np.array([4,8,6,9])
c = tf.multiply(a,b)
print(c.numpy())
c = tf.multiply(a,e)
print(c)
c = tf.multiply(a,l1)
print(c)



f = tf.constant([4,5,6,8])
g = tf.constant([7,5,8,6])
c = tf.multiply(f,g)
k = tf.multiply(f,e)
print(k)
print(c)


a = tf.Variable([4,8,5,6])
b = tf.Variable([4,8,9,3])
c = tf.multiply(a,b)
l = tf.multiply(a,f)
print(c)
print(l)
