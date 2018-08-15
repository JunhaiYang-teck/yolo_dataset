# -*- coding: utf-8 -*
import os;
import shutil
import sys

path='/Users/wumanjia/Desktop/xuelang_round1_train_part3_20180709'

filedir = os.listdir(path)
f= open(path+"/name.txt",'wb')
for files in filedir:
	new_context = "\"" + files + "\"" + ','
	f.write(new_context.encode("utf-8"))



for files in filedir:
	Olddir = os.path.join(path,files);
	if os.path.isdir(Olddir):#如果是文件夹
		filelist = os.listdir(Olddir)
		for filename in filelist:
			Olddir2 = os.path.join(Olddir,filename);
			shutil.copyfile(Olddir2,path+"/data/"+filename)
