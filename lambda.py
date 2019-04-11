__author__ = 'rdhek'
#syntax
#lambda arg1,arg2,.....:exprsession


power = lambda x, n:x **n
print power
print power(2,3)

ascii_values=[112,113,114,115,116,117]
#
#def tag_it(av):
#    return '<ascii char="{}">{}</ascii>'.format(chr(av),av)

temp=map(lambda av : '<ascii char="{}">{}</ascii>'.format(chr(av),av),ascii_values )
print temp

items = range(1,89)
temp = filter(lambda x: x%7==0 ,items)
temp1 =map(lambda x: x if x%7==0 else 0,items)

import re
#for line in filter(lambda line:re.search('root',line),open('password.txt')):
#    print line


#reduce
print reduce (lambda a,b:a+b,[1,3,5,7,9])
