#!/usr/bin/python3

import os
import time

path = "/home/mitchell/Scripts/picture 2 ascii/asciianimation/output/"
os.system('clear')

for txt in os.listdir(path):
	lines = ''
	with open(path + txt) as file:
		lines = file.readlines()

	for line in lines:
		print(line, end='')
		time.sleep(0.01)

	time.sleep(5)
	os.system('clear')