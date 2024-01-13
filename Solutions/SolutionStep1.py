#>1
import matplotlib.pyplot as plt
#<1 #>2
import matplotlib.image as mpimg
#<2


#[Data Philadelphia.jpg]#@>3
image = mpimg.imread('Philadelphia.jpg') #[$Data.out]#@1
#<3

#[Visualize]#@>4
plt.imshow(image)
plt.show()
#<4
