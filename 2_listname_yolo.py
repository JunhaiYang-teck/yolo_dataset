#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    
    path = '/Volumes/MachsionHD/drone_dataset_02.28/train1/'
    savepath = '/Volumes/MachsionHD/drone_dataset_02.28/'
    txtname = "train"
    # path = '/Volumes/MachsionHD/drone_dataset_03.07/droneUSC/'
    # savepath = '/Volumes/MachsionHD/drone_dataset_03.07/droneUSC/'



def getFileName(path):
    ''' 获取指定目录下的所有指定后缀的文件名 '''

    # f = open(path+txtname+".txt", "w")
    # f_list = os.listdir(path+txtname) #==========================
    f_list = os.listdir(path)
    print(path)
    # print f_list
    for i in f_list:
        # print(i)
        if (os.path.isdir(i) or (i == ".DS_Store") or (i == "anotation.mat")):#如果是文件夹则跳过 
            continue;
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.jpeg' or os.path.splitext(i)[1] == '.jpg' or os.path.splitext(i)[1] == '.png':
            # new_context = '/Volumes/MachsionHD/drone_dataset_02.28/drone20180304/' + str(i)+ '\n'
            # new_context = '/root/wmj-docker/droneUSC/' + str(i)+ '\n'   
            new_context = '/root/wmj-docker/drone20180304/' + str(i)+ '\n'         
            f.write(new_context)




# getFileName(path,"valid")
f = open(savepath+txtname+".txt", "w")

getFileName(path)
f_listdir = os.listdir(path)
for dir in f_listdir:
    if os.path.isdir(path+dir):
        getFileName(path+dir)

f.close()