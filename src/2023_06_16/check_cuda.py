import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow as tf
import torch
import os

# sess = tf.Session(config=tf.ConfigProto(log_device_placement=True)) # tf < v2.0
sess = tf.compat.v1.Session(config=tf.compat.v1.ConfigProto(log_device_placement=True))
print (sess)
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())

from keras import backend as K
K.tensorflow_backend._get_available_gpus()