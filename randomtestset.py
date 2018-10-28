import os, random, shutil

#randomly choose a number of xml files to obtain the test set
def copyFile(fileDir):

    pathDir = os.listdir(fileDir)

    sample = random.sample(pathDir, 44)


    for name in sample:
        shutil.copyfile(fileDir + name, tarDir + name)


if __name__ == '__main__':
    fileDir = "PATH TO ORIGINAL XML FOLDER"
    tarDir = "PATH TO NEW SUB XML"
    copyFile(fileDir)
