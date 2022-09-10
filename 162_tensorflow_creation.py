from pickletools import int4
import tensorflow as tf
## how to creat tensor flow ones tensor from any tensor
#creat tensor having all element is one
a = tf.ones((4,4),tf.int16)
print(a.numpy())
print(a.dtype)
b = tf.ones((2,2,4),tf.int16)
print(b)
e = tf.constant([[1,2,3],[4,6,8],[7,5,6]])
print(e)
d = tf.ones_like(e,tf.int16)# this function same shape tensor having same dimension with input 
print(d)
f = tf.ones_initializer()#it is used to produce tenser by only one
print(f)