# -*- coding: utf-8 -*-
import os


path = '/Users/wumanjia/Desktop/2/image/'
filelist = os.listdir(path)

for filename in filelist:
	if os.path.splitext(filename)[1]=='.jpg':
		print(filename)
		name = os.path.splitext(filename)[0]
		filetxt = name + '.txt'
		ftxt = open(path+filetxt, "w")
		ftxt.close()