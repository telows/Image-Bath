
import os
from PIL import Image
import imagehash


#find duplicates use dhash
#add all duplicates (ones that occour after) to a list
#delete all in the list if opted into 



#create class for hashes and associated img name
class hashed_img:

	def __init__(self, name, hash):
		self.hash = hash
		self.name = name
		self.path = ""



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
		h_im = hashed_img(i, hash)
		imgs.append(h_im)

	return imgs




def compare(ims):

	for i in ims:

		if(ims.index(i) == len(ims)):
			print("shoudl end")
			return

		n = ims.index(i) + 1

		for x in ims[n:]:
			if i.hash == x.hash:
				print(i.name + " and " + x.name + " are duplicates")
				#add to duplicate list

		#return list of duplicates



#path for test
path = 'C:\\Users\\XPS\\Pictures\\test2\\'

files = gen_list(path)

print("there are " + str(len(files)) + " files in this folder")

compare(files)



