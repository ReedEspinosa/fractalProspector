import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
import time as time
# from matplotlib.pyplot import plot, ion, show
import numpy as np

# img=mpimg.imread('zeroCool.png');

plt.ion() # enables interactive mode
# imgplot = plt.imshow(img)
print "fin"
# plt.draw()
print "encore"
# NpixVert = img.shape()[0]
img = np.ones([600,800,3]) - 0.25 # everything is 0.75 grey to start
img[:,:,1] = 0.9 # make everything light green
img[range(450,580,1),range(500,580,1),[1]] = 0.75 # simulated dead patch
# make the line of creatures spaced every third square
img[300,range(200,400,3),[0]] = 0 # set other color to zero at creature
img[300,range(200,400,3),[1]] = 0.45 # divide green value by two
img[300,range(200,400,3),[2]] = 1 # 100% of color corresponding to this animal

imgplot = plt.imshow(img)

plt.show()