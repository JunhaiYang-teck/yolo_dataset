#! /usr/bin/python
# -*- coding: utf-8 -*-

import os
import re

if __name__ == '__main__':
    
    path = '/Users/wumanjia/Desktop/'
    savepath = '/Users/wumanjia/Desktop/'
    txtname = "readme"



def extractNum(f1,f2): #要提取的文件，生成的文件
    ''' 获取文件中的precision和recall '''
    lines = f1.readlines()
    # re_func = re.compile(r"(\d+\.\d+).+?(\d+\.\d+)%.+?(\d+\.\d+)%.+?(\d+\.\d+)%")
    re_func = re.compile(r"(\d+).+?(\d+\.\d+)%.+?(\d+\.\d+)%.+?(\d+\.\d+)%")
    for line in lines:
        find_line = re_func.match(line)
        # find_line = re.findall(r"0\.\d+",line)
        num = find_line.group(1)
        IOU = find_line.group(2)
        Recall = find_line.group(3)
        Precision = find_line.group(4)
        new_context = num +" "+ IOU +" "+ Recall +" "+ Precision +";"+ '\n'         
        f2.write(new_context)


# getFileName(path,"valid")
f1 = open(path+txtname+".txt", "r")
f2 = open(savepath+"precision_recall11.txt", "w")

extractNum(f1,f2)

f1.close()
f2.close()
