# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 18:08:57 2018

@author: wangz
"""
import os
from PIL import Image
import csv

def checkCsv (numOfLine, img, csvList, originalPath, newPath, i = 0):
    while numOfLine > 0:
        if csvList[i][0] == img:
            x = int(csvList[i][4])
            y = int(csvList[i][5])
            xmax = int(csvList[i][6])
            ymax = int(csvList[i][7])
        
            im = Image.open(originalPath + img)
            region = im.crop((x - 20, y - 20, xmax + 180, ymax + 180))
            region.save(newPath + str(i) + ".jpg")
            region = im.crop((x - 180, y - 20, xmax + 20, ymax + 180))
            region.save(newPath + str(i + 0.25) + ".jpg")
            region = im.crop((x - 20, y - 180, xmax + 180, ymax + 20))
            region.save(newPath + str(i + 0.5) + ".jpg")
            region = im.crop((x - 180, y - 180, xmax + 20, ymax + 20))
            region.save(newPath + str(i + 0.75) + ".jpg")
            print("img saved")
        i = i + 1
        numOfLine = numOfLine - 1


csvFile = open("PATH TO CSV")
originalPath = "PATH TO ORIGINAL IMAGES"
newPath = "PATH TO SAVE NEW SUB-IMAGES"

csv_reader = csv.reader(csvFile)
numOfLine = 0
for root, dirs, files in os.walk(originalPath):
    imgList = files
    
i = 0
csvList = []

for row in csv_reader:
    csvList.append(row)
    numOfLine += 1 

 

for img in imgList:
    checkCsv(numOfLine, img, csvList, originalPath, newPath)
  

    
    
    

