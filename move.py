
import os
import os.path
import sys
import shutil
import re

source = 'D:\\document\\result\\'
target = 'D:\\document\\new\\'


def getFileList(path):
    filenames_set = set()
    for dirpath,dirname,filename in os.walk(source):
        for file in filename :
             filenames_set.add(dirpath+'\\'+file)
    return filenames_set


def copy(substr, filenames_set) :
    for filename in filenames_set:
        dir, strfile = os.path.split(filename)
        if strfile.find(substr) >= 0:
            oldname = filename
            newname = target + strfile
            shutil.copyfile(oldname,newname)
            print(newname)
            print("Success")
            print (oldname)
            break


if __name__ == '__main__':
    if not os.path.exists(target):
        os.makedirs(target)
    filenames_set = getFileList(source)
    file = open("run.log")
    # var = ['2','3']
    # result = []
    # for int(list) in var:
    #     res = str(list).find('Ia_store')
    #     if res >= 0:
    #         print res
    #         res1 = str(list).split('-')
    #
    #         result.append(res1[1])
    #         print result

    # while 1:
    #     str = file.readline()
    #
    #     wantstr = str[str.find('0x'):str.find('txt')]
    #     copy(wantstr,filenames_set)
    #     if not str:
    # #         break
    # cnt = 0
    while 1:
        str = file.readline()
        cnt += 1
        #find "Reentrancy bug: 	 True"
        if str.find('Reentrancy bug: 	 True') != -1:
            #print(str)
            str = file.readline()
            cnt += 1
            print('%d:%s' % (cnt, str))
            wantstr = str[str.find('0x'):str.find('txt')]
            copy(wantstr, filenames_set)
            #print or output
        if not str:
            break
    for list in var:
        list= str(list)
        print (list)
        wantstr = list[str.find('Ia_store'):find(')')]
        print (wantstr)
