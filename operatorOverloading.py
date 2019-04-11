__author__ = 'rdhek'


class Box(object):
    def __init__(self,size):
        self.size=size

    def __add__(self, other):
        return Box(self.size+other.size)

    def __mul__(self, other):
        return Box(self.size*other)

    __rmul__=__mul__


from collections import deque

class CustomeFile(file):
    def __lshift__(self, other):
        content=""
        self.seek(0,0)
        while other:
            content += self.readline()
            other -= 1

        return content

    def __rshift__(self, other):
        self.seek(0,0)
        content = " ".join(deque(self,other))
        return content

if __name__ == '__main__':
    b1=Box(10)
    b2=Box(11)
    b3=b1+b2
    b4= b3 * 3
    print b4.size

    with CustomeFile('tmp.json') as fp:
        print fp>>2
        print ""
        print fp<<2
