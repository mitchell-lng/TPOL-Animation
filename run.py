#!/usr/bin/python3

import os
import time

path = "/home/mitchell/Scripts/picture 2 ascii/asciianimation/output/"
os.system('clear')

files = os.listdir(path)
files.sort()

slower = ['3', '4', '5', '6', '7', '8']

for txt in files:
	delay = 6
	linetime = 0
	
	for s in slower:
		if s in txt:
			delay = 15
			break

	lines = ''
	with open(path + txt) as file:
		lines = file.readlines()

	for line in lines:
		print(line, end='')
		time.sleep(0.01)

	time.sleep(delay)
	os.system('clear')
