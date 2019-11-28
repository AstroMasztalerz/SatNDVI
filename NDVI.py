import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from astropy.nddata import NDDataArray
print("This programm will lead you through creating a NDVI map from images")
print("It works under assumption that you input two images into it: A Red band image and Near infrared image")
print("The images must be monochrome, cloudless and it would be best if they had a ocean mask applied.")
print("If they contain clouds/waterbodies, those will also be falsely ranged on scale.")
print("NIR is Band 4, R is Band 3 or broadband VIS")
pathNIR=input("Please input the path to near infrared image:    ")
pathR=input("Please input the path to red image:    ")
print("Please select a color pallete you want to use. Available palletes:")
print("Greens   Greys   hot    seismic")
cmapN=input()

r=mpimg.imread(pathR)
nir=mpimg.imread(pathNIR)
numerator=NDDataArray.subtract(nir,r)
denominator=NDDataArray.add(nir,r)
NDVI=NDDataArray.divide(numerator,denominator)
plt.imshow(NDVI,cmap=cmapN)
plt.colorbar()
plt.show()