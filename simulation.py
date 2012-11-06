#!/usr/bin/env python

from agents import Kepler 
from messaging import PostOffice
from multiprocessing import Process, Queue
from random import randint
from time import sleep

def runKepler(kepler):
    kepler.run()

def runPostOffice(post):
    post.run()

if __name__ == '__main__':
    depot = Queue()
    keplers = [Kepler(name=str(i), messenger=depot, value=10, land=0, goods={}, education=0, labour=0, food=10) for i in range(10)]
    royalMail = PostOffice(depot)

    print "create/start mail process"
    Process(target = runPostOffice, args = (royalMail,)).start()

    for kepler in keplers:
        print "create/start Kepler process"
        sleep(randint(1,100)*0.01)
        Process(target = runKepler, args = (kepler,)).start()
