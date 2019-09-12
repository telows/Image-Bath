
import os
from PIL import Image
import imagehash
import sys

#find duplicates use dhash
#add all duplicates (ones that occour after) to a list
#delete all in the list if opted into 


#create class for hashes and associated img name
class hashed_img:

	def __init__(self, name, hash, path):
		self.name = name
		self.hash = hash
		self.path = path


def hash(path):
	print(1)



#list strings with path + names
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
				print(i.name + " and " + x.name + " are duplicates")
				dup.append(x)
				ims.remove(x)

	return dup


def del_duplicates(dps):

	for i in dps:
		os.remove(i.path + i.name)



def main():

	#argv[1] = path 2+ = other options
	path = sys.argv[1]

	#for testing
	#path = 'C:\\Users\\XPS\\Pictures\\test2\\'
	#path = 'C:\\Users\\XPS\\Pictures\\test\\'
	path = 'C:\\Users\\XPS\\Pictures\\gems\\'

	files = gen_list(path)

	#make this optional?
	print("there are " + str(len(files)) + " files in this folder")

	#make print dups an option?
	dups = compare(files)

	if "-d" in sys.argv:
		del_duplicates(dups)
		#print("-d found")


#main cunction call
main()