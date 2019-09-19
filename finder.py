#!/usr/bin/python3

import os
from PIL import Image
import imagehash
import sys
import time
import re

#find duplicates use dhash phash may be more accurate, but slower
#add all duplicates (ones that occour after) to a list
#delete all in the list if opted into 


#create class for hashes and associated img name
class hashed_img:

	def __init__(self, name, path):
		self.name = name
		self.hash = None
		self.path = path

	def add_hash(self, hash):
		self.hash = hash


class duplicates:

	def __init_(self, name, path, dups):
		self.name = name
		self.path = path
		#dups should be a list of images that are duplicates
		#will need to change -d and -pd for this
		self.dups = dups



#for c++ hash implementation
def hash(path):
	print(1)

def py_dhash(path):

	hash = imagehash.dhash(Image.open(path))
	return hash

#add other hashing algos 


#returns list of hashed imgs
#super slow
def gen_list(path):
	
	#gives list h_ims w/ no hash
	imgs = []
	if "-a" in sys.argv:
		imgs = subdir_files(path)
	else:
		imgs = get_ims(path)


	#filter out webms may need to adjust to filter out non img files
	for i in imgs:
		if ".webm" in i.name:
			imgs.remove(i)

	#hash images, and create hashed image objs
	#make option for diff hashing algos here
	for i in imgs:
		#need to expand to other hashing algos
		hash = py_dhash(i.path)
		i.add_hash(hash)

	return imgs

#gen list helper function no -a flag
def get_ims(path):

	ims = []
	for f in os.listdir(path):
			if os.path.isfile(path + f) is True:
				im = hashed_img(f, path + f)
				ims.append(im)

	return ims


#gen list helper function, -a implementation
def subdir_files(path):

	ims = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if os.path.isfile(root + "\\" + file) is True:
				h_im = hashed_img(file, root + "\\" + file)
				ims.append(h_im)

	return ims


def compare(ims):

	dup = []

	for i in ims:

		n = ims.index(i) + 1

		for x in ims[n:]:
			if i.hash == x.hash:
				#may change for speed
				if "-pd" in sys.argv:
					print(i.name + " and " + x.name + " are duplicates")
				dup.append(x)
				ims.remove(x)

	#make alternate for -pd flag to improve speed

	return dup



def del_duplicates(dps):
	for i in dps:
		os.remove(i.path)



def main():

	start_time = time.time()
	#add check for path existing
	#path = sys.argv[1]

	#for testing
	path = 'C:\\Users\\XPS\\Pictures\\test2\\'
	#path = 'C:\\Users\\XPS\\Pictures\\test\\'
	#path = 'C:\\Users\\XPS\\Pictures\\gems\\'

	#add finding folder option

	#takes 22.7 secs on 880 files
	#gives list of hashed imgs
	files = gen_list(path)

	if "-s" in sys.argv:
		print("there are " + str(len(files)) + " files in this folder")


	#takes 3.9 secs on 880 files
	dups = compare(files)

	#add num of dups 
	if "-nd" in sys.argv:
		print("there are " + str(len(dups)) + " duplicate images")
	
	if "-d" in sys.argv:
		#del_duplicates(dups)
		print("-d found")

	if "-t" in sys.argv:
		print(str(time.time() - start_time) + " seconds")


main()

#execute command
#os.system("command")


# **TODO LIST**
#add timer and additional flags
#add option to explore folders in given path
'''
redo file finding with -a for more efficency

make a find folder function
-ph use phash instead of dhash for more accuracy

implement hash in c++ will be faster?
create duplicate class that gives file and all its duplicates - useful for -a implementation
'''

#DONE LIST
'''
-s for number of files #done
-d for delete duplicates #done
-t for timer #done
-pd to print duplicates #done (may improve if dup class made)
-nd number of duplicates #done
fix -a to not save folder extension, and make image classes after finding the file
'''