import tensorflow as tf
a = tf.constant([1,5,3,6])#constant value does not change 
print(a)
b = tf.Variable(a)#but varible value is change
print(b)
print(a.numpy())
#creat varible with different shape
c = tf.Variable([[1,8,3],[4,5,6],[5,5,5]])
print(c)
print(c.numpy())
d = tf.Variable([[4,5,6],[5,8,9]],shape=(2,3),dtype=float)
print(d)
#reshape varible
e = tf.reshape(d,(3,2))
print(e)
#get index of higher values
a = tf.argmax(c)
print(a)
#exiest highest value
print(a.numpy())


#convert into tenser
f = tf.convert_to_tensor(d)
print(f)
#change values in the varible
g = c.assign([[5,8,6],[5,6,9],[5,2,8]])
print(c)
#perfrom addition of varible
j = tf.Variable([4,8,6])
h = j.assign_add([4,5,2])
print(h)



