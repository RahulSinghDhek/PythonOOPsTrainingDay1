__author__ = 'rdhek'

class Demo(object):
    def __init__(self):
        print "Here I am",self

    def __del__(h):
        print"Got destroyed",h

d = Demo()
print d