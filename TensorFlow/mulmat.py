# Sentdex example

import tensorflow as tf

with tf.Session() as sess:
	with tf.device("/gpu:1"):
		matrix1 = tf.constant([[3.,3.]])
		matrix2 = tf.constant([[2.],[2.]])
		product = tf.matmul(matrix1,matrix2)
		print(product)
