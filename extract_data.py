!pip install Pillow

#Import All the Required Components
from PIL import Image
from PIL.TiffTags import TAGS
import numpy as np

#Extraction of Data -- Meta Dictionary (met_dict) and Array of Pixels (img)


with Image.open('/content/41077_120219_S000090_ch01.tif') as img:
    meta_dict = {TAGS[key] : img.tag[key] for key in img.tag}
    img = np.array(img)

#Check of the Image Dimension
if img.ndim == 2:
  dim = 1
  print("image has 1 dim")
else:
  dim = img.shape[-1]
  print("image has", dim, "channels")
  
