# Sentdex example
import tensorflow as tf
x1 = tf.constant(5)
x2 = tf.constant(6)
result  = tf.mul(x1,x2)

sess = tf.Session()
output = sess.run(result)
sess.close()
print(output)
