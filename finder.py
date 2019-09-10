
import os
from PIL import Image
import imagehash


#find duplicates use dhash
#def dhash(image, hash_size=8):
#must use pil image


#hash = imagehash.average_hash(Image.open('test.png'))



#add all duplicates (ones that occour after) to a list
#delete all in the list if opted into 


files = os.listdir()

print(len(files))



def hash(path):
	with open(path, 'rb') as f:
		return f.read() #hash stuff
		#hash = imagehash.average_hash(Image.open('test.png'))





#open folder
#save path
#get all files in path
#list strings with path + names
def gen_list(path):



