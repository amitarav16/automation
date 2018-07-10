from os import *
name = listdir("/home/ucifer/Downloads")
name1 = listdir("/home/ucifer/Documents")
for song in name:
	if song in name1:
		common = path.join(name1, song)
		remove(common)

