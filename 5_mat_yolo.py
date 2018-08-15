import scipy.io as scio
import os
import cv2 as cv

import pandas as pd

data_path="/Volumes/MachsionHD/USCdata/image_label/"

dirnames = os.listdir(data_path)

for dirname in dirnames:
	print(dirname)
	if os.path.isdir(data_path+dirname):
		data_train = scio.loadmat(data_path+"/"+dirname+"/anotation.mat")
		# data_train_label=data_train.get('label')#取出字典里的label
		# data_train_data=data_train.get('data')#取出字典里的data

		filenames = os.listdir(data_path+"/"+dirname)		
		# filenames =['160.jpg', '160.txt', '170.jpg', '170.txt']
		if '.DS_Store' in filenames:
			filenames.remove('.DS_Store')
		if 'anotation.mat' in filenames:
			filenames.remove('anotation.mat')
		filenames.sort(key=lambda x: int(''.join(filter(str.isdigit,x))))
		'''提取字符串中的数字'''
		i = 0
		for filename in filenames:
			# filenames.sort(key= lambda x:int(x[:-4]))
			
			if os.path.splitext(filename)[1] == '.jpeg' or os.path.splitext(filename)[1] == '.jpg' or os.path.splitext(filename)[1] == '.png':
				img = cv.imread(data_path+"/"+dirname+"/"+filename)
				shape = img.shape # 0height 1weight 
				# <x> <y> <width> <height>
				# 原始的是  左上角+长宽
				x = (data_train["box"][i][0]+data_train["box"][i][2]/2)/shape[1]
				y = (data_train["box"][i][1]+data_train["box"][i][3]/2)/shape[0]
				width = data_train["box"][i][2]/shape[1]
				height = data_train["box"][i][3]/shape[0]

				ftxt = open(data_path+"/"+dirname+"/"+os.path.splitext(filename)[0]+".txt", "w")
				new_context = "0 " + str(x)+ " " + str(y) + " " + str(width) + " " + str(height) +'\n'
				ftxt.write(new_context)
				ftxt.close()
				i = i+1


# data_train = scio.loadmat("/Volumes/MachsionHD/USCdata/image_label/1/anotation.mat")
# print(data_train["box"][0][0])
