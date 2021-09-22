import os
import cv2
from PIL import Image


def getFileList(dir, Filelist, ext=None):
    """
    获取文件夹及其子文件夹中文件列表
    输入 dir：文件夹根目录
    输入 ext: 扩展名
    返回： 文件路径列表
    """
    newDir = dir
    if os.path.isfile(dir):
        if ext is None:
            Filelist.append(dir)
        else:
            if ext in dir[-3:]:
                Filelist.append(dir)

    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newDir = os.path.join(dir, s)
            getFileList(newDir, Filelist, ext)

    return Filelist


org_img_folder = r'image'

# 检索文件
imglist = getFileList(org_img_folder, [], 'png')
print('本次执行检索到 ' + str(len(imglist)) + ' 张图像\n')

for imgpath in imglist:
    print(imgpath)
    im = Image.open(imgpath)  # 返回一个Image对象
    Width = im.size[0]
    height = im.size[1]
    ratio = round(Width / height, 2)
    print('宽：%d,高：%d,宽高比：%0.2f' % (Width, height, ratio))
    if ratio <= 2.00:
        image = cv2.imread(imgpath, 0)
        print(image)
        res = cv2.resize(image, (1078, 554), interpolation=cv2.INTER_AREA)
        fileName = "./images/" + os.path.basename(imgpath)
        cv2.imwrite(fileName, res)
    # imgname = os.path.splitext(os.path.basename(imgpath))[0]
    # img = cv2.imread(imgpath, cv2.IMREAD_COLOR)
