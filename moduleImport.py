__author__ = 'rdhek'
from inheritence import Person


class Employee(Person):
    def __init__(self,eid,first_name,last_name):
        self.eid= eid
        super(Employee,self).__init__(first_name,last_name)

    def get_info(self):
        print 'Derived : id : ',self.eid
        super(Employee,self).get_info()

if __name__ == '__main__':
    e= Employee('109','guido','rossum')
    e.get_info()