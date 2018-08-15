import os
import shutil



path = "/Volumes/MachsionHD/drone_dataset_02.28/"


for name in ["train","valid"]:
    dirnames = os.listdir(path+name+"1/")
    if '.DS_Store' in dirnames:
       dirnames.remove('.DS_Store')


    if not os.path.exists(path+name):
       os.mkdir(path+name)


    for dirname in dirnames:
        print(dirname)
        filenames = os.listdir(path+name+"1/"+dirname)
        if 'listxml.txt' in filenames:
            filenames.remove('listxml.txt')
        if 'train.txt' in filenames:
            filenames.remove('train.txt')
        for filename in filenames:
            if os.path.splitext(filename)[1] != '.xml':
                shutil.copy(path+name+"1/"+dirname+"/"+filename, path+name)
    