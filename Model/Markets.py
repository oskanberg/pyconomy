#!/usr/bin/env python

##
# Abstract class for differnt markets (e.g. factor, product)
##

class Market(object):

    def __init__(self):
        self.__all = dict()
    
    ## Add a new commodity type to the market
    ## Return false if type already exists, true if success
    def _addType(self, typeName):
        if typeName not in self.__all:
            self.__all[typeName] = []
            return True
        else:
            return False
    
    ## Add a listing to a given type table
    def _addListing(self, typeName, entry):
        if typeName in self.__all:
            self.__all[typeName].append(entry)
            return True
        else:
            return False
    
    ## Remove a listing if it exists
    def _removeListing(self, typeName, entry):
        if typeName in self.__all:
            self.__all[typeName].remove(entry)
        return True
    
    ## Get all listings of the given type
    def _getAllListings(self, typeName):
        if typeName in self.__all:
            return self.__all[typeName]
        else:
            return []
    
    def _getAllTypes(self):
        return self.__all.keys()



##
# All labour gets negotiated through one'a these
##

class LabourMarket(Market):

    def __init__(self):
        Market.__init__(self)
        self._addType("labour")
    
    def addListing(self, labour):
        self._addListing("labour", labour)
    
    




        
a = LabourMarket()
if a.addListing("Hello"):
    print "yay"
types = a._getAllTypes()
print types

