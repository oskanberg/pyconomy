#!/usr/bin/env python

import time
import sys


## Abstract for sending messages
class MessengerObject(object):
    
    def __init__(self, name, depot):
        self.__depot = depot
        self.__name = name
    
    def _postMessage(self, message, priority):
        self.__depot.put((self.__name, message, priority))

## To read the messages in depot
class PostOffice(object):
    
    def __init__(self, depot):
        self.__depot = depot
    
    def run(self):
        while True:
            if self.__depot.empty():
                time.sleep(0.1)
            else:
                (name, message, priority) = self.__depot.get()
                print name + " (" + str(priority) + ") : " + message
                sys.stdout.flush()
