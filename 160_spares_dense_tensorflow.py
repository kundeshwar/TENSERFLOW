from tokenize import _all_string_prefixes
import tensorflow as tf
a = tf.SparseTensor(indices=[[4,5],[6,3]],values=[10,20],dense_shape=[3,10])
print(a)
#creat sparsetensor by using dense (it convert dense to sparse)
import numpy as np
b = np.array([[1,0,0,0],[0,0,0,0],[0,0,2,0],[0,0,0,4]])
f = tf.sparse.from_dense(b)
print(f)
#Extract values,indices,shapes of sparese tensor
#print(f.values())
print(f.values.numpy())
print(f.indices.numpy())
print(f.dense_shape.numpy())
#sparse tensor to dense tensor
c = tf.sparse.to_dense(f)
print(c)
#mathamatical operation on sparese tenser
e = tf.sparse.add(f,f)
print(e.numpy())
f = tf.sparse.to_dense(e)
print(f.numpy())