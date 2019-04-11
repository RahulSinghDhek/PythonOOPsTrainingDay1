__author__ = 'rdhek'
import threading
import logging
import requests
from Queue import Queue
res = requests.get("http://www.google.com")
print res

def curl(q):
    url=q.get()

def main():
    urls=['http://google.com','http://python.org']
    for url in urls:
        t =threading.Thread(target=curl)