
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
		self.path = path


#for c++ hash implementation
def hash(path):
	print(1)


#list strings with path + names
#super slow
def gen_list(path):
	
	files = os.listdir(path) #gives list of file names
	imgs = []

	#filter out webms
	for i in files:
		if ".webm" in i:
			files.remove(i)

	#hash images, and create hashed image objs
	for i in files:

		hash = imagehash.dhash(Image.open(path + i))
		h_im = hashed_img(i, hash, path)
		imgs.append(h_im)

	return imgs



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
	#path = 'C:\\Users\\XPS\\Pictures\\test2\\'
	#path = 'C:\\Users\\XPS\\Pictures\\test\\'
	path = 'C:\\Users\\XPS\\Pictures\\gems\\'

	#add finding folder option

	#takes 22.7 secs on 880 files
	files = gen_list(path)

	#print(time.time() - start_time)

	if "-s" in sys.argv:
		print("there are " + str(len(files)) + " files in this folder")

	#print(time.time() - start_time)

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



# **TODO LIST**
#add timer and additional flags
#add option to explore folders in given path
'''
-a for all folders in path go in every folder in the path
make a find folder function

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