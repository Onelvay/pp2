import os
path='C:\\pp2\\lab6_mine\\test_case'
list=os.listdir(path)
dirlist=[]
filelist=[]
for name in list:
    if os.path.isdir(os.path.join(path,name)):
        dirlist.append(name)
    elif os.path.isfile(os.path.join(path,name)) :
        filelist.append(name)
print("Directories",dirlist,"\n""Files",filelist, "\n""All", list)
