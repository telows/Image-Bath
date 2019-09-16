#!/usr/bin/python3

import os
from PIL import Image
import imagehash
import sys
import time

#find duplicates use dhash phash may be more accurate, but slower
#add all duplicates (ones that occour after) to a list
#delete all in the list if opted into 


#create class for hashes and associated img name
class hashed_img:

	def __init__(self, name, hash, path):
		self.name = name
		self.hash = hash
		#self.hash
		self.path = path


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


#list strings with path + names
#super slow
def gen_list(path):
	
	 #gives list of file names
	files = []
	if "-a" in sys.argv:
		files = subdir_files(path)
	else:
		#files = os.listdir(path)
		for f in os.listdir(path):
			if os.path.isfile(path + f) is True:
				files.append(f)

	imgs = []

	#filter out webms may need to adjust to filter out non img files
	for i in files:
		if ".webm" in i:
			files.remove(i)

	#hash images, and create hashed image objs
	for i in files:

		#ISSUE with -a command since does not have additional path part
		hash = imagehash.dhash(Image.open(path + i))
		h_im = hashed_img(i, hash, path)
		imgs.append(h_im)

	return imgs



#for -a implementation
def subdir_files(path):

	f = []
	for root, dirs, files in os.walk(path):
		for file in files:
			if os.path.isfile(root + "\\" + file) is True:
				f.append(root[len(path):] + "\\" + file)
				#print()

	#need to make individual paths for files in inner folders
	print(f)
	return f


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

	return dup



def del_duplicates(dps):
	for i in dps:
		os.remove(i.path + i.name)



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
-a for all folders in path go in every folder in the path (use -af?)

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
'''