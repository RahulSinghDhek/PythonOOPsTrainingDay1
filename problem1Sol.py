__author__ = 'rdhek'

from os import  listdir, stat
from os.path import join , isfile
from time import ctime
from pprint import pprint as pp


class DirectoryListing(object):
    def __init__(self,*args):
        self.directory_names = args
        self.container = dict()
        self.__read_directories()

    def get_fileproperties(self,file_name):
        file_stat=stat((file_name))
        return [file_stat.st_size,file_stat.st_mtime]

    def __read_directories(self):
        for dir_name in self.directory_names:
            for file_item in listdir(dir_name):
                abs_path= join(dir_name,file_item)
                if isfile(abs_path):
                    self.container.setdefault(dir_name,dict())[file_item]=self.get_fileproperties(abs_path)
if __name__ == '__main__':
    d = DirectoryListing('C:/Users/rdhek/Django/mysite','C:/Users/rdhek/Downloads/temp')
    pp(d.container)