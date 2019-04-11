__author__ = 'rdhek'

def demo():
    print "first"
    yield 11
    print "second"
    yield 12
    print "third"
    yield 13

g = demo()
print g.next()
print g.next()
print g.next()

#other way
for item in demo():
    print item
    