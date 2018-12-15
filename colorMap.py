import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import cv2
import numpy as np
from PIL import Image
import sys
import PIL

formals_shoes_pants = {
	"black" : ["black", "lgrey", "dgrey"],
	"dbrown" : ["tan", "olive", "white"],
	"lbrown" : ["blue", "olive", "brown", "tan", "white", "beige", "red"]
}

formals_pants_shirts = {
	"beige" : ["lblue", "white"],
	"black" : ["lblue", "white", "grey"],
	"blue"  : ["white", "pink", "grey"],
	"brown" : ["white", "pink"],
	"lgrey" : ["lblue", "white"],
	"dgrey" : ["dblue", "white"],
	"olive" : ["lblue", "white"],
	"red"   : ["white"],
	"tan"   : ["lblue", "white", "black"],
	"white" : ["lblue", "dblue"]
}

def concat_images(imga, imgb):
    """
    Combines two color image ndarrays side-by-side.
    """
    ha,wa = imga.shape[:2]
    hb,wb = imgb.shape[:2]
    max_height = np.max([ha, hb])
    total_width = wa+wb
    new_img = np.zeros(shape=(max_height, total_width, 3))
    new_img[:ha,:wa]=imga
    new_img[:hb,wa:wa+wb]=imgb
    return new_img

def concat_n_images(image_path_list):
    """
    Combines N color images from a list of image paths.
    """
    output = None
    for i, img_path in enumerate(image_path_list):
        img = plt.imread(img_path)[:,:,:3]
        print(img)
        if i==0:
            output = img
        else:
            output = concat_images(output, img)
    return output

def createMoodBoard(pantColor, shirtColor, shoeColor):
	images = ['UTStore/Formal_Pants/' + pantColor + 
		'.jpeg', 'UTStore/Belts/' + shoeColor + '.jpeg']
	output = concat_n_images(images)
	plt.imshow(output)
	plt.show()

def getFormalShirtsColors(pantColor):
	return formals_pants_shirts[pantColor]

def getFormalsPantsColor(shoeColor):
	return formals_shoes_pants[shoeColor]

def main(shoeColor, type):
	pantColors = []
	shirtColors = []
	if type == 1:
		pantColors = getFormalsPantsColor(shoeColor)

	chosenPantColor = random.choice(pantColors)

	shirtColors = getFormalShirtsColors(chosenPantColor)

	chosenShirtColor = random.choice(shirtColors)

	createMoodBoard(chosenPantColor, chosenShirtColor, shoeColor)
	print(chosenShirtColor)
	print(chosenPantColor)
	print(shoeColor)

main("lbrown", 1)