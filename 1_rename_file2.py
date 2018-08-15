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
import shutil
import os;
def rename(count):
    # count = 600;
    # path = '/Volumes/MachsionHD/drone_dataset_03.07/train1/'+str(count)+'/';
    # savepath = '/Volumes/MachsionHD/drone_dataset_03.07/train/'
    path = '/Volumes/MachsionHD/USCdata/image_label/'+str(count)+'/';
    savepath = '/Volumes/MachsionHD/USCdata/image_label/droneUSC/'
    filelist = os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    # filename = "begin";
    print(filelist);
    # print(filelist)
    aaa = 1
    # aaa =len(filelist)//60
    num = 1
    for files in filelist:#遍历所有文件
        Olddir = os.path.join(path,files);#原来的文件路径
        if ((os.path.isdir(Olddir)) or (files == ".DS_Store") or (files == "anotation.mat")):#如果是文件夹则跳过 
            continue;
        filename1 = os.path.splitext(files)[0];#文件名
        filetype = os.path.splitext(files)[1];#文件扩展名
        # print(filename,filetype)
        # if filename != filename1:
        #     count += 1;
        # Newdir = os.path.join(path,str(count).rjust(4,'0')+filetype);#新的文件路径
        if int(filename1)%(aaa*10) == 0:
            num = num +1
            print(num)
            shutil.copyfile(path+filename1+".txt",savepath+str(count)+"_"+filename1+".txt")
            shutil.copyfile(path+files,savepath+str(count)+"_"+files)
            # Newdir = os.path.join(path,str(count)+"_"+filename1+filetype);#新的文件路径
            # print(Newdir);
            # os.rename(Olddir,Newdir);#重命名
        # filename = filename1;
    # count = 0;

for count in [26]:
    rename(count);

