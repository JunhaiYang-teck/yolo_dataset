import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random


# 1/读取当前目录的xml文件以及图片文件(list_xml_filename)
# 并列表记录listxml.txt和

if __name__ == '__main__':
    
    xmltxt = "listxml.txt"
    traintxt = "train.txt"
    d_traintxt = "train2.txt"
    d_validtxt = "valid.txt"
    # path = '/Users/wumanjia/Desktop/tianchi-xuelang/test/'
    path = "/Volumes/MachsionHD/drone_dataset3_08.10/drone_fixed-wing/"
    path2 = '/root/wmj-docker/droneDataset/drone_fixed-wing/' # 指定训练目录前缀

fxml = open(path+xmltxt, "w")
ftrain = open(path+traintxt, "w")

def getFileName(path):
    ''' 获取指定目录下的所有指定后缀xml的文件名 '''

    f_list = os.listdir(path)
    # print f_list
    for i in f_list:
        print(i)
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(i)[1] == '.xml':
            new_context = os.path.splitext(i)[0] + '\n'
            fxml.write(new_context)
        if os.path.splitext(i)[1] == '.jpeg' or os.path.splitext(i)[1] == '.jpg' or os.path.splitext(i)[1] == '.png':
            new_context = path2 + str(i) + '\n'
            ftrain.write(new_context)


getFileName(path)

fxml.close()
ftrain.close()

# ============================================================
# # 2/分割数据集

# ftrain = open(path+traintxt,'r')

# def divideupDataset(path):
    
#     lines = ftrain.readlines()
#     n = len(lines)
#     print("the number of pic: ", n) 

#     test_index = random.sample(range(n), n//5)
#     test_index.sort()
#     print("the number of test: ", n//5)
#     print("the number of train: ", n-n//5)

#     file1 = open(path+d_validtxt,'w') 
#     file2 = open(path+d_traintxt,'w')

#     test = []
#     train = []
#     for i in range(n):
#         if i in test_index:
#             file1.write(lines[i])
#         else:
#             file2.write(lines[i])

#     file1.close()
#     file2.close()

# # divideupDataset(path)
# ftrain.close()



# =============================================================
# 3/转换xml文件
sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["drone","fixed-wing"]
# classes = ["drone"]
# classes = ["破边","边针眼","边扎洞","粗纱","纬粗纱","弓纱","边白印","织稀","经跳花","扎梳","毛洞","织入","结洞","回边","黄渍","缺纬","经粗纱","毛斑","扎纱","油渍","愣断","擦毛","楞断","跳花","污渍","扎洞","破洞","边缺纬","紧纱","线印","嵌结","厚薄段","蒸呢印","剪洞","毛粒","擦洞","吊弓","吊经","修印","缺经","耳朵","擦伤",\
# "明嵌线","织稀","经跳花","边缺经","厚段","夹码"]
def convert(size, box):
    if size[0] == 0:
        print(image_id)
        return(0,0,0,0)
    else:
        dw = 1./size[0]
        dh = 1./size[1]
        x = (box[0] + box[1])/2.0
        y = (box[2] + box[3])/2.0
        w = box[1] - box[0]
        h = box[3] - box[2]
        x = x*dw
        w = w*dw
        y = y*dh
        h = h*dh
        return (x,y,w,h)

def convert_annotation(image_id):
    in_file = open(path+'%s.xml'%(image_id),encoding="utf-8")
    out_file = open(path+'%s.txt'%(image_id), 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        # cls_id = 1
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

# wd = getcwd()

# # image_ids = open(path+xmltxt).read().strip().split()
# image_ids = open(path+xmltxt).readlines()
# for image_id in image_ids:
#     image_id = image_id.strip('\n')
#     convert_annotation(image_id)


# =============================================================





