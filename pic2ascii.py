#!/usr/bin/python3

import numpy as np
from PIL import Image, ImageFont, ImageDraw
from os import listdir, chdir, mkdir
import shutil

# set up variables
path = "/home/mitchell/Scripts/picture 2 ascii/asciianimation/"
ratio = 1

# Distribute the characters based on length and the position in list
characters = [' ', ' ', '.', '.', '.', '\'', '-', '-', 'o', ':', ';', '*', '+', 'i', 't', 'v', 'p', 'w', '=', '|', '(', '[', '/', '7', '?', 'X', '@', 'U', 'S', 'B', 'E']
interval = 255 / len(characters)

# Gets all files ending in png
images = [x for x in listdir(path) if '.png' in x]

def getCharacter(coords):
	global characters
	global interval

	dark = img_g.getpixel(coords)

	count = 0
	while ((255 - interval * count) > dark):
		count += 1

	return characters[count - 1]


# Create and move to the output folder

shutil.rmtree(path + 'output')

chdir(path)
mkdir('output')
chdir('output')


for image in images:
	
	# Get image ready
	img = Image.open(path + image)

	width, height = round(img.width / ratio), round(img.height / (ratio * 3))
	larger_image = img.resize((width, height), Image.BILINEAR)
	
	img_g = larger_image.convert('L')

	finalimage = ''
	for y in range(height):
		for x in range(width):
			finalimage += getCharacter((x, y))

		finalimage += '\n' # Used to create newline


	# Save ascii to file
	with open(image.replace('.png', '.txt'), 'w') as file:
		file.write(finalimage)
		