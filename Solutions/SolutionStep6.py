#>1
import matplotlib.pyplot as plt
#<1 #>2
from math import sqrt
#<2 #>3
from PIL import ImageEnhance
#<3 #>4
import numpy as np
from PIL import Image
#<4 #>5
import matplotlib.image as mpimg
#<5 #>6
def ModifyHighlights(image, amount, highlightPoint):
    newImage = image.copy()

    slope = amount
    yIntercept = highlightPoint * (1 - amount)

    highlightPoint = 3 * highlightPoint

    for rowIndex, row in enumerate(image):
        for columnIndex, column in enumerate(row):
            summed = sum(column)
            if summed > highlightPoint:

                floatColumn = column.astype(np.float32)

                hue, saturation, intensity = RgbToHsi(floatColumn[0], floatColumn[1], floatColumn[2])

                initialIntensity = intensity
                intensity = slope * intensity + yIntercept
                if intensity < 0:
                    intensity = 0
                elif intensity > 255:
                    intensity = 255

                newR, newG, newB = HsiToRgb(hue, saturation, intensity)

                if max([newR, newG, newB]) < 25 and intensity > 100:
                    print([floatColumn[0], floatColumn[1], floatColumn[2]])
                    print([hue, saturation, intensity])
                    print([newR, newG, newB])
                    print(intensity)
                    print(initialIntensity)


                newR = max(min(newR, 255), 0)
                newG = max(min(newG, 255), 0)
                newB = max(min(newB, 255), 0)


                newImage[rowIndex][columnIndex] = np.array([newR, newG, newB]).astype(np.uint8)

    return newImage
def HsiToRgb(hue, saturation, intensity, show = False):
    newR = 0
    newG = 0
    newB = 0
    if hue < 120:
        denominator = np.cos(np.deg2rad(60 - hue))
        if hue == 0 or denominator == 0 :
            newR = intensity + 2 * intensity * saturation
            newG = intensity - intensity * saturation
            newB = intensity - intensity * saturation
        elif hue < 120:
            newR = intensity + intensity * saturation * np.cos(np.deg2rad(hue))/denominator
            newG = intensity + intensity * saturation * (1 - np.cos(np.deg2rad(hue))/denominator)
            newB = intensity - intensity * saturation
    elif hue < 240:
        denominator = np.cos(np.deg2rad(180 - hue))
        if hue == 120 or denominator == 0 :
            newR = intensity - intensity * saturation
            newG = intensity + 2 * intensity * saturation
            newB = intensity - intensity * saturation
        elif hue < 240:
            newR = intensity - intensity * saturation
            newG = intensity + intensity * saturation * np.cos(np.deg2rad(hue - 120))/denominator
            newB = intensity + intensity * saturation * (1 - np.cos(np.deg2rad(hue - 120))/denominator)
    else:
        denominator = np.cos(np.deg2rad(300 - hue))
        if hue == 240 or denominator == 0 :
            newR = intensity - (intensity * saturation)
            newG = intensity - (intensity * saturation)
            newB = intensity + (2 * intensity * saturation)
        else:
            newR = intensity + intensity * saturation * (1 - np.cos(np.deg2rad(hue - 240))/denominator)
            newG = intensity - intensity * saturation
            newB = intensity + intensity * saturation * np.cos(np.deg2rad(hue - 240))/denominator

    return newR, newG, newB
def RgbToHsi(red, green, blue):

    allColors = [red, green, blue]

    intensity = sum(allColors) / 3
    saturation = 0 if intensity == 0 else (1 - min(allColors) / intensity)

    denominator = sqrt(red**2 + green**2 + blue**2 - red*green - red*blue - green*blue)
    if denominator == 0:
        hue = 0
    else:
        hue = np.rad2deg(np.arccos((red - .5*green - .5*blue)/denominator))
        if green >= blue:
            pass
        else:
            hue = 360 - hue

    return hue, saturation, intensity
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

#[Highlights --amount 40% --threshold 60%]#@>12
imageHighlight = ModifyHighlights(imageSaturation, 1.4, 153) #[$Highlights.out]#@6
#<12

#[Visualize]#@>13
plt.imshow(imageHighlight)
plt.show()
#<13