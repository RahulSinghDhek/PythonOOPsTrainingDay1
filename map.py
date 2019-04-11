__author__ = 'rdhek'

items = [5,4,3,2,1]
temp = map(bin,items)

print temp


ascii_values=[112,113,114,115,116,117]
#
from pprint import pprint as p
def tag_it(av):
    return '<ascii char="{}">{}</ascii>'.format(chr(av),av)

p(map(tag_it,ascii_values))
