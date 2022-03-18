import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data, img_as_float
from PIL import Image
from skimage.segmentation import chan_vese
fig, axes = plt.subplots(1, 3, figsize=(10, 10))
import numpy as np

with Image.open('/content/41077_120219_S000090_ch01.tif') as img:
  img = np.array(img)

img_gray = chan_vese(img, max_iter= 60,extended_output=True)

ax = axes.flatten()

ax[0].imshow(img, cmap="gray")
ax[0].set_title("Original Image")

ax[1].imshow(img_gray[0], cmap="gray")
title = "Chan-Vese segmentation - {} iterations".format(len(img_gray[2]))

ax[1].set_title(title)

ax[2].imshow(img_gray[1], cmap="gray")
ax[2].set_title("Final Level Set")
plt.show()
