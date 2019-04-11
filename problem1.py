__author__ = 'rdhek'
from os import listdir , stat
from os.path import isfile , isdir, join
from time import ctime

#print listdir('C:/Users/rdhek/Django/mysite')
#print stat('C:/Users/rdhek/Django/mysite/manage.py').st_ctime

class DirectoryListing:
    def listFiles(self,listOfDirectories):
        temp={}
        for directory in listOfDirectories:
            listTemp = listdir(directory)
            for el in listTemp:
                if isfile(el):
                    fullPath = join(directory,el)
                    print fullPath
                    filestat = [stat(fullPath).st_ctime,stat(fullPath).st_size]
                    temp[el]=filestat
        print temp

d=DirectoryListing()
listDict=['C:/Users/rdhek/Django/mysite']
d.listFiles(listDict)