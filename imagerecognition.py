
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import shutil as shu

def imageopener(image):
    i = Image.open(image)
    iar = np.asarray(i)
    plt.imshow(iar)
    print(iar)
    plt.show
    plt.savefig("humanornot2.png")



def moveToFile(images):
   shu.move("/Users/dhruvanavinchander1/Desktop/Milestone AI Development/"+ images,"/Users/dhruvanavinchander1/Desktop/Milestone AI Development/humanornotimages")
    
    

images = [1]
for x in images:
    imageopener("/Users/dhruvanavinchander1/Downloads/IMG-5423.jpg")




#def crossreference(image,image2):

    



    



# this in theory should open an image then take the array and convert that into a graphable image
# we can then take that and identify a human or other thing in it 