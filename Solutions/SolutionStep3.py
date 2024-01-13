#>1
import matplotlib.pyplot as plt
#<1 #>2
import numpy as np
from PIL import Image
#<2 #>3
import matplotlib.image as mpimg
#<3


#[Data Philadelphia.jpg]#@>4
image = mpimg.imread('Philadelphia.jpg') #[$Data.out]#@1
#<4

#[Rotate --degrees 3.3]#@>5
pilImage = Image.fromarray(image)
imageRotated = np.array(pilImage.rotate(3.3)) #[$Rotate.out]#@2
#<5

#[Crop --amount 15%]#@>6
pilShape = imageRotated.shape
pilImageHeight = pilShape[0]
pilImageWidth = pilShape[1]

pilImage = Image.fromarray(imageRotated)
imageCropped = np.array(pilImage.crop((0.15 * pilImageWidth, 0.15 * pilImageHeight, 0.85 * pilImageWidth, 0.85 * pilImageHeight))) #[$Crop.out]#@3
#<6

#[Visualize]#@>7
plt.imshow(imageCropped)
plt.show()
#<7
