import random
import os
used = open("used_words.txt","r")
lines = used.readlines()
print("length of file is : ",len(lines))

def dupe(imgf):
	used = open("used_words.txt","r")
	lines = used.readlines()
	dupe = False
	for eachLine in lines:
		if imgf in eachLine:
			dupe = True
			return dupe
		else:
			dupe = False
	return dupe


def img_pick():
	global used
	global lines
	imgdir = '/Users/scottkirwan/Documents/api/pics/'
	number_files = os.listdir(imgdir)
	print len(number_files)
	imgfile = random.choice(os.listdir(imgdir))
	print(imgfile)
	dupe_img = dupe(imgfile)
	print(dupe_img)
	while True:
		if (dupe_img == False):
			if len(lines) >= len(number_files):
				used = open("used_words.txt","w")
				used.write("")
			used = open("used_words.txt","a")
			used.write(imgfile)
			used.write("\n")
			return imgfile
		else:
			print("IMAGE USED ALREADY, REPICKING")
			imgfile = random.choice(os.listdir(imgdir))
			while dupe_img == True:
				imgfile = random.choice(os.listdir(imgdir))
				dupe_img = dupe(imgfile)
				if len(lines) >= len(number_files)-1:
					used = open("used_words.txt","w")
					used.write("")


