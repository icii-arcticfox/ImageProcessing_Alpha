#>1
import matplotlib.pyplot as plt
#<1 #>2
import numpy as np
from PIL import Image
#<2 #>3
import matplotlib.image as mpimg
#<3

#[Data Philadelphia.jpg]#>4
image = mpimg.imread('Philadelphia.jpg') #[$Data.out]#@1
#<4

#[Rotate --degrees 3.3]#>5
pilImage = Image.fromarray(image)
imageRotated = np.array(pilImage.rotate(3.3)) #[$Rotate.out]#@2
#<5

#[Visualize]#>6
plt.imshow(imageRotated)
plt.show()
#<6
