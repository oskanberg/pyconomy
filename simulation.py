#!/usr/bin/env python

from agents import Kepler 
from messaging import PostOffice
from multiprocessing import Process, Queue

def k(kepler):
    kepler.run()

def p(post):
    post.run()

if __name__ == '__main__':
    depot = Queue()
    
    royalMail = PostOffice(depot)
    
    a = Kepler(name="Kepel", messenger=depot, value=10, land=0, goods={}, education=0, labour=0, food=10)
    
    
    print "create/start mail process"
    Process(target = p, args = (royalMail,)).start()
    
    print "create/start Kepler process"
    Process(target = k, args = (a,)).start()
