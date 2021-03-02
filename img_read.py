import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from floodfill import *

#from profilehooks import profile
#@profile
def fill_image(filename,x,y,color: list):
    img = mpimg.imread(filename)
    return fill_array(img,x,y,color)

def fill_array(img,x,y,color):
    img = img[:,:,:3] # slice 4th dimension (alpha value)
    height = len(img)
    width = len(img[0])
    floodfill(img,width,height,Point(x,y),np.array(color))
    return img
    

## WORKING EXAMPLES
img = fill_image('img_example.png',280,227,[1,0,0]) # turn rectangle red
img = fill_array(img,273,116,[0,0,1]) # turn outside to blue
plt.imshow(img)
plt.show()
