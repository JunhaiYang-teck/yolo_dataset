# -*- coding: utf-8 -*-
import os


path = '/Users/wumanjia/Desktop/02/'
filelist = os.listdir(path)

for filename in filelist:
	if os.path.splitext(filename)[1]=='.jpg':
		print(filename)
		name = os.path.splitext(filename)[0]
		filexml = name + '.xml'
		if filexml in filelist:
			continue
		os.remove(path+filename)
