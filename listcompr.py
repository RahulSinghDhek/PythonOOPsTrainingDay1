__author__ = 'rdhek'
mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]

print [row for row in mat]
print
print [ col for row in mat for col in row]
print
print [col for row in mat for col in row if col%2]

#transpose the matrix

print [[row[i] for row in mat ]for i in range(3)]

from os import listdir
from os.path import isfile , join

#dir_name="/tmp"
#list
#file = [item for item in listdir(dir_name) if isfile(join(dir_name,item))]

#set
#file = {item for item in listdir(dir_name) if isfile(join(dir_name,item))}

#dict
print {item:bin(item) for item in range(1,5)}

#generatot

from timeit import timeit

def demo():
    itemss=[1,2,3,4]
    temp=list()
    for item in itemss:
        temp.append(hex(item))
    return temp

def demo2():
    itemss=[1,2,3,4]
    temp2 = [hex(item) for item in itemss]
    return temp2

if __name__ == '__main__':
     print timeit('demo()',setup='from __main__ import demo', number=10000)
     pass

