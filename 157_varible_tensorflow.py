import tensorflow as tf
a = tf.Variable(1)
print(a)

b = tf.Variable([1,2,5,36,5])
print(b)
print(a.name)
print(a.shape)
print(a.dtype)
print(a.numpy())
print(type(a))


c = tf.Variable([1.2,5.25])
print(c)

d = tf.Variable("kundeshwar")
print(d)

e = tf.Variable(True)
print(e)

f = tf.Variable([4+2j])#it for complex number
print(f)


