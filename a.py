# delete duplicate files
from os import *
name = listdir("enter the path of folder")
name1 = listdir("enter the path of folder wich contains copy of files")
for song in name:
	if song in name1:
		common = path.join(name1, song)
		remove(common)

