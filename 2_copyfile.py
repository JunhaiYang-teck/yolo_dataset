import os
import shutil


# 将由kcf得到的标注数据集进行筛选，比如跳帧选取
# 基本每个视频选取30帧

# path = "/Volumes/MachsionHD/实验视频/标注/wmj/"
# path = "/Volumes/MachsionHD/实验视频/标注/lxx/B9_Dji4_1/"
# path = "/Volumes/MachsionHD/实验视频/标注/xwg/"
path = "/Volumes/MachsionHD/实验视频/标注/yj/"
videoname = "Pg_Dji4_6 00_01_47-00_01_58"
savepath = "/Volumes/MachsionHD/drone_dataset_02.28/"
newname = "PGDji4b" #重新命名选取的图片

filenames = os.listdir(path+videoname+'/drone')
if '.DS_Store' in filenames:
	filenames.remove('.DS_Store')
filenames.sort(key= lambda x:int(x[:-4]))


if not os.path.exists(path+videoname+"/select"):
	os.mkdir(path+videoname+"/select")
if not os.path.exists(savepath+videoname):
    os.mkdir(savepath+videoname)


step = len(filenames)//30
num = 1
count = 1
for filename in filenames:
    name = filename.split(".")[0]
    if count > 30:
        break
    if name == str(num):
        # 拷贝到原始目录的select文件夹下
        # shutil.copyfile(path+videoname+'/frame/'+filename,path+videoname+'/select/'+newname+filename)
        # shutil.copyfile(path+videoname+'/txt/'+name+".txt",path+videoname+'/select/'+newname+name+".txt")
        # 拷贝到数据集目录下的以videoname命名的文件夹下
        shutil.copyfile(path+videoname+'/frame/'+filename,savepath+videoname+"/"+newname+filename)
        shutil.copyfile(path+videoname+'/txt/'+name+".txt",savepath+videoname+"/"+newname+name+".txt")
        num = num+step
        count = count+1
        print(count)
    