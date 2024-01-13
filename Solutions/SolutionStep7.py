#>1
import matplotlib.pyplot as plt
#<1 #>2
import os
import sys
from math import sqrt
#<2 #>3
from PIL import ImageEnhance
#<3 #>4
import numpy as np
from PIL import Image
#<4 #>5
import matplotlib.image as mpimg
#<5 #>6
sys.path.append(os.path.abspath('ImageFunctions.py'))
from ImageFunctions import *
#<6


#[Data Philadelphia.jpg]#@>7
image = mpimg.imread('Philadelphia.jpg') #[$Data.out]#@1
#<7

#[Rotate --degrees 3.3]#@>8
pilImage = Image.fromarray(image)
imageRotated = np.array(pilImage.rotate(3.3)) #[$Rotate.out]#@2
#<8

#[Crop --amount 15%]#@>9
pilShape = imageRotated.shape
pilImageHeight = pilShape[0]
pilImageWidth = pilShape[1]

pilImage = Image.fromarray(imageRotated)
imageCropped = np.array(pilImage.crop((0.15 * pilImageWidth, 0.15 * pilImageHeight, 0.85 * pilImageWidth, 0.85 * pilImageHeight))) #[$Crop.out]#@3
#<9

#[Brighten 10%]#@>10
pilImage = Image.fromarray(imageCropped)
pilImage = ImageEnhance.Brightness(pilImage).enhance(1.1)
imageBrightened = np.array(pilImage) #[$Brighten.out]#@4
#<10

#[Saturation --amount 30%]#@>11
pilImage = Image.fromarray(imageBrightened)
pilImage = ImageEnhance.Color(pilImage).enhance(1.3)
imageSaturation = np.array(pilImage) #[$Saturation.out]#@5
#<11

#[Highlights --amount 40% --threshold 60% --functions ImageFunctions.py]#@>12
imageHighlight = ModifyHighlights(imageSaturation, 1.4, 153) #[$Highlights.out]#@6
#<12

#[Visualize]#@>13
plt.imshow(imageHighlight)
plt.show()
#<13