# https://keras.io/guides/keras_cv/generate_images_with_stable_diffusion/


# pip install --upgrade keras-cv
# pip install tensorflow

import time
import keras_cv
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow as tf
import torch
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
from tensorflow.python.client import device_lib
print(device_lib.list_local_devices())


if torch.has_cuda:
   device = "cuda:0"
elif torch.has_mps:
   device = "mps"
else:
   device = "cpu"
   
model = keras_cv.models.StableDiffusion(img_width=512, img_height=512)

propmt = "blaues sofa fantasy art"
def plot_images(images):
    plt.figure(figsize=(20, 20))
    for i in range(len(images)):
        ax = plt.subplot(1, len(images), i + 1)
        plt.imshow(images[i])
        plt.axis("off")

images = model.text_to_image("photograph of an astronaut riding a horse", batch_size=3)
plot_images(images)

images = model.text_to_image(
    "cute magical flying dog, fantasy art, "
    "golden color, high quality, highly detailed, elegant, sharp focus, "
    "concept art, character concepts, digital painting, mystery, adventure",
    batch_size=3,
)
plot_images(images)
