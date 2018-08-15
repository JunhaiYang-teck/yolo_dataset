#导入cv模块
import os
import cv2 as cv
import pandas as pd
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
cv.namedWindow("Image",cv.WINDOW_NORMAL)

# path = '/Volumes/MachsionHD/drone_dataset_02.28/drone20180304/' 
# path = "/Volumes/MachsionHD/drone_dataset_03.07/droneUSC/"
path = "/Users/wumanjia/Desktop/tianchi-xuelang/xuelang/"
f_list = os.listdir(path) 
for i in f_list:
	if os.path.splitext(i)[1] == '.jpeg' or os.path.splitext(i)[1] == '.jpg' or os.path.splitext(i)[1] == '.png':
		print(path+i)
		img = cv.imread(path+i)
		data = pd.read_table(path+os.path.splitext(i)[0]+'.txt',header=None,delim_whitespace=True)
		print(data)
		shape = img.shape # height weight 
		for i in range(len(data)): 
			height = shape[0]*data.ix[i,4]
			weight = shape[1]*data.ix[i,3]
			x1 = shape[1]*data.ix[i,1]-weight/2
			y1 = shape[0]*data.ix[i,2]-height/2
			x2 = shape[1]*data.ix[i,1]+weight/2
			y2 = shape[0]*data.ix[i,2]+height/2
			print(x1,x2)
			cv.rectangle(img,(int(x1),int(y1)),(int(x2),int(y2)),(55,255,155),5)
		cv.imshow("Image",img)
		# cv.rectangle(img, (212,317), (290,436), (0,255,0), 4)
		cv.waitKey(0)
#释放窗口
cv.destroyAllWindows() 


# '''
# 在创建lmdb文件时显示
# Corrupt JPEG data ： premature end od data segment
# 以下程序为找出此图像
# '''
# import os
# import cv2
# path = '/Volumes/MachsionHD/drone_dataset_02.28/drone20180304/' 
# def find_bad_image():
#         dirnames = os.listdir(path)
#         for dirname in dirnames:
#         	a = cv2.imread('path%s'%(dirname))
#         	print(dirname)

# find_bad_image()