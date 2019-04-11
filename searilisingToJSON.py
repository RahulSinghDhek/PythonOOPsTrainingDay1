__author__ = 'rdhek'

from problem1Sol import DirectoryListing
from json import dump

class DirectoryListingToJSON(DirectoryListing):
    def to_json(self,json_file):
        dump(self.container,open(json_file,'wb'),indent=4)

if __name__ == '__main__':
    try:
        DirectoryListingToJSON('C:/Users/rdhek/Django/mysite','C:/Users/rdhek/Downloads/temp').to_json('tmp.json')
    except IOError,err_obj:
        print err_obj