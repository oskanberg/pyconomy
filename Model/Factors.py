#!/usr/bin/env python

##
# Abstract class for differnt factor listing (labour, land, etc.)
##

class Factor(object):

    def __init__(self, amount, value):
        self.__amount = amount
        self.__value  = value


class Labour(Factor):
    
    def __init__(self, amount, value):
        Factor.__init__(self, amount, value)
        factorType = "labour"

