import os
from PIL import Image
import sys


imgPath = sys.argv[1]
im = Image.open(imgPath)
width, hight = im.size
newPath = "PATH TO A NEW FOLDER TO SAVE SUB-IMAGES"


w = 350
id = 1
i = 0
while (i + w <= width + w):
    j = 0
    while (j + w <= hight + w):
        new_img = im.crop((i, j, i + w, j + w))

        new_img.save(newPath + str(id) +".jpg")
        id += 1
        j = j + w 
    i = i + w 

strA = ('python find_wally.py ' + imgPath)
p = os.system(strA)

ith = 1
while (ith < id):
    strA = ('python find_wally.py ' + newPath + str(ith) + '.jpg')
    p = os.system(strA)
    ith = ith + 1


ls = os.listdir(newPath)
for i in ls:
    c_path = os.path.join(newPath, i)
    if os.path.isdir(c_path):
        del_file(c_path)
    else:
        os.remove(c_path)





