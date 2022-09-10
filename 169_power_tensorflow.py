import tensorflow as tf
#mathmatical operation by using tensorflow
import numpy as np
# it gives error when you gives integer it only accept datatype float16,half,float32,float64,complex64,complex128
a = 3
b = 4
e = 5
c = tf.pow(a,b)#sceond value is power
print(c)


l1 = [4,5,2,6]
l2 = [5,2,6,3]
c = tf.pow(l1,l2)
print(c)
t = (4,5,6,9)
c = tf.pow(t,l1)
print(c)
c = tf.pow(a,l1)
print(c)
c = tf.pow(t,b)
print(c)
a = np.array([4,2,5,3])
b = np.array([4,8,6,9])
c = tf.pow(a,b)
print(c.numpy())
c = tf.pow(a,e)
print(c)
c = tf.pow(a,l1)
print(c)



f = tf.constant([4,5,6,8])
g = tf.constant([7,5,8,6])
c = tf.pow(f,g)
k = tf.pow(f,e)
print(k)
print(c)


a = tf.Variable([4,8,5,6])
b = tf.Variable([4,8,9,3])
c = tf.pow(a,b)
l = tf.pow(a,f)
print(c)
print(l)
