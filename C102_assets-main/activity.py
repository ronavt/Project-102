import os
import shutil


source = "images"
destination = "organized-files"

list_of_files = os.listdir(source)
# print(list_of_files)
for i in list_of_files:
    name,ext = os.path.splitext(i)
    if ext == '':
        continue
    if ext in ['.gif','.png','.jpg', '.jfif']:
        path1 = source + '/' + i
        path2 = destination + '/' + 'images_files'
        path3 = destination + '/' + 'images_files' + "/" + i

        if os.path.exists(path2):
            print("Image Folder Exists")
            shutil.move(path1,path3)
            print("The file",i, "moved....")
        else:
            print("folder doesn't exist")
            os.mkdir(path2)
            print("folder created")
            shutil.move(path1,path3)
            print("File moved")