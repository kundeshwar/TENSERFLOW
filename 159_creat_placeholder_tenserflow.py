import tensorflow as tf
import numpy as np
#b = tf.compat.v1.disable_eager_execution()
#print(b)
#a = tf.v1.placeholder(dtype=tf.float16,shape=(50,50))
#print(a)
#c = tf.add(a,b)
#print(c)
d = np.ones((50,50),np.float32)
print(d)


#Execute Tensorflow placeholder using session 
#with tf.compat.v1.Session() as sess:
  # e = sess.run(c,feed_dict={a:d, b:d})
  #print(e)
  #print(a.name())
  #print(a.type())
  #print(a.shape())