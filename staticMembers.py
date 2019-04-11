__author__ = 'rdhek'

class Connections(object):
    max_count =5
    counter = 0

    def __init__(self,conn_id):
        self.conn_id =conn_id
        Connections.counter +=1


    #def check_limit():
    #    if Connections.counter>Connections.max_count:
    #        raise RuntimeError('reached max limit')

    @staticmethod #decrator similar to annotations in other language
    def check_limit():
        if Connections.counter>Connections.max_count:
            raise RuntimeError('reached max limit')
        return True
    #print check_limit()
    #check_limit=staticmethod(check_limit)
    print check_limit


    if __name__ == '__main__':
        for item in range(6):
            print Connections(item)