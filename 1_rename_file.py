# import os

# print("1")
# for file in os.listdir('.'):    #os.listdir('.')遍历文件夹内的每个文件名，并返回一个包含文件名的list
#     if file[-2: ] == 'py':
#         continue   #过滤掉改名的.py文件
#     # if file[-2: ] == 'DS_Store':
#     #   continue   #过滤掉改名的.py文件
#     # name = file.replace(' ', '')   #去掉空格
#     for i in list(range(46)):
#         new_name = str(i)+'.jpg'  #选择名字中需要保留的部分
#         os.rename(file, new_name)

import os;
def rename():
    count = 0;
    # path = '/Users/manjiawu/Desktop/drone';
    # path = '/Volumes/MachsionHD/drone_dataset_03.07/valid1/5';
    path = '/Users/wumanjia/Desktop/fixedwing'
    # path='/Users/wumanjia/Desktop/xuelang_round1_train_part2_20180705'
    filelist = os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    # print(filelist)
    for files in filelist:#遍历所有文件
        Olddir = os.path.join(path,files);#原来的文件路径
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue;
        if os.path.splitext(files)[0]=='.DS_Store':
            print("#####")
            continue;
        # filename = os.path.splitext(files)[0];#文件名
        filetype = os.path.splitext(files)[1];#文件扩展名
        print(filetype)
        Newdir = os.path.join(path,str(count).rjust(2,'0')+filetype);#新的文件路径
        print(Newdir)
        os.rename(Olddir,Newdir);#重命名
        count += 1;
    count = 0;

rename();

