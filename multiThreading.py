__author__ = 'rdhek'

import threading

from time import  sleep

def worker():
    tname = threading.current_thread().getName()
    tid = threading.currentThread().ident
    print "{} : {}".format(tname,tid)
    return

def main():
    thread_objs = list()
    for item in range(5):
        t = threading.Thread(target=worker)
        thread_objs.append(t)
        t.start()

    for t in thread_objs:
        t.join()
    print "main thread"

if __name__ == "__main__":
    main()
