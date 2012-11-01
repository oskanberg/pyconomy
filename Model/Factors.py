#!/usr/bin/env python

##
# Abstract class for differnt factor listing (labour, land, etc.)
##

class Factor(object):

    def __init__(self):
        self.__all = dict
    

class Labour(Factor):
    
    def __init__(self):
        Factor.__init__(self)
