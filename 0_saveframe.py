import cv2
import os


path = '/Users/wumanjia/Desktop/未命名文件夹/'
timeF = 30 #视频帧计数间隔频率

def saveframe(path,videoname,timeF):
    vc = cv2.VideoCapture(path+videoname+".mp4") #读入视频文件
    c=1
    if vc.isOpened(): #判断是否正常打开
        rval , frame = vc.read()
    else:
        rval = False

    if not os.path.exists(path+'image'):
        os.mkdir(path+'image')
    while rval:   #循环读取视频帧
        rval, frame = vc.read()
        if(c%timeF == 0): #每隔timeF帧进行存储操作
            cv2.imwrite(path+'image/'+videoname+'_'+str(c) + '.jpg',frame) #存储为图像
        c = c + 1
        cv2.waitKey(1)
    vc.release()



filelist = os.listdir(path)#该文件夹下所有的文件（包括文件夹）
# print(filelist)


for files in filelist:#遍历所有文件
        
    filetype = os.path.splitext(files)[1];#文件扩展名

    if filetype == ".mp4":

        videoname = os.path.splitext(files)[0] #文件名
        saveframe(path,videoname,timeF)
        




