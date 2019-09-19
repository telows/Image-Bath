#!/usr/bin/python3

import os
from PIL import Image
import imagehash
import sys
import time



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

#python implementation of dhash **default**
def py_dhash(path):
	hash = imagehash.dhash(Image.open(path))
	return hash

#add other hashing algos 
def py_phash(path):
	hash = imagehash.phash(Image.open(path))
	return hash


#returns list of hashed imgs
#super slow
def gen_list(path):
	
	#gives list h_ims w/ no hash
	imgs = []
	if "-a" in sys.argv:
		imgs = subdir_files(path)
	else:
		imgs = get_ims(path)

	#check if folder is empty
	#if size(imgs) is 0:
		#exit(1)

	#filter out webms may need to adjust to filter out non img files
	#rework into single function call? imgs = filter()
	for i in imgs:
		if ".webm" in i.name:
			imgs.remove(i)

	#hash images, and add the hash to each object
	imgs = hash_images(imgs)

	return imgs

#gen list helper function no -a flag
def get_ims(path):

	ims = []
	for f in os.listdir(path):
			if os.path.isfile(path + f) is True:
				h_im = hashed_img(f, path + f)
				ims.append(h_im)

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


#function to hash list of hashed_imgs
def hash_images(imgs):
	#need to expand to other hashing algos based on flags
	if "-ph" in sys.argv:
		for i in imgs:
			hash = py_phash(i.path)
			i.add_hash(hash)
	else:
		for i in imgs:
			hash = py_dhash(i.path)
			i.add_hash(hash)

	return imgs

#compares image hashes and returns duplicates
def compare(ims):

	dup = []

	for i in ims:

		n = ims.index(i) + 1

		for x in ims[n:]:
			if i.hash == x.hash:
				#CHANGE FOR SPEED
				if "-pd" in sys.argv:
					print(i.name + " and " + x.name + " are duplicates")
				dup.append(x)
				ims.remove(x)

	#make alternate for -pd flag to improve speed

	return dup


#deletes duplicates
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
'''
make a find folder function

make filter function in imgs creator
make empty list check for error control

implement hash in c++ will be faster?
create duplicate class that gives file and all its duplicates - useful for -pd -nd -d implementations
'''

#FlAG LIST
'''
-ph use phash instead of dhash for more accuracy
-s for number of files #done
-d for delete duplicates #done
-t for timer #done
-pd to print duplicates #done (may improve when dup class made)
-nd number of duplicates #done
-a to go through folders
'''