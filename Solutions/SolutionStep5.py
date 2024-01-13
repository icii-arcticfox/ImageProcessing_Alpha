#>1
import matplotlib.pyplot as plt
#<1 #>2
from PIL import ImageEnhance
#<2 #>3
import numpy as np
from PIL import Image
#<3 #>4
import matplotlib.image as mpimg
#<4


#[Data Philadelphia.jpg]#@>5
image = mpimg.imread('Philadelphia.jpg') #[$Data.out]#@1
#<5

#[Rotate --degrees 3.3]#@>6
pilImage = Image.fromarray(image)
imageRotated = np.array(pilImage.rotate(3.3)) #[$Rotate.out]#@2
#<6

#[Crop --amount 15%]#@>7
pilShape = imageRotated.shape
pilImageHeight = pilShape[0]
pilImageWidth = pilShape[1]

pilImage = Image.fromarray(imageRotated)
imageCropped = np.array(pilImage.crop((0.15 * pilImageWidth, 0.15 * pilImageHeight, 0.85 * pilImageWidth, 0.85 * pilImageHeight))) #[$Crop.out]#@3
#<7

#[Brighten 10%]#@>8
pilImage = Image.fromarray(imageCropped)
pilImage = ImageEnhance.Brightness(pilImage).enhance(1.1)
imageBrightened = np.array(pilImage) #[$Brighten.out]#@4
#<8

#[Saturation --amount 30%]#@>9
pilImage = Image.fromarray(imageBrightened)
pilImage = ImageEnhance.Color(pilImage).enhance(1.3)
imageSaturation = np.array(pilImage) #[$Saturation.out]#@5
#<9

#[Visualize]#@>10
plt.imshow(imageSaturation)
plt.show()
#<10
