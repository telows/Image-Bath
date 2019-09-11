
import os
from PIL import Image
import imagehash


#find duplicates use dhash
#def dhash(image, hash_size=8):
#must use pil image


#hash = imagehash.average_hash(Image.open('test.png'))



#create class for hashes and associated img name
class hashed_img:

	def __init__(self, name, hash):
		self.hash = hash
		self.name = name
		self.path = ""


#add all duplicates (ones that occour after) to a list
#delete all in the list if opted into 




def hash(path):
	print(1)


#open folder
#save path
#get all files in path
#list strings with path + names
def gen_list(path):
	
	files = os.listdir(path) #gives list of file names
	imgs = []

	#filter out webms and maybe gifs?
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

	t = 1


#path for test
path = 'C:\\Users\\XPS\\Pictures\\test\\'

files = gen_list(path)

print(len(files))

compare(files)