#!/usr/bin/env python

import math
from multiprocessing import Process, Lock

class NaturalResource(object):

    def __init__(self, amount):
        self.__resource = self.generatePrimes(amount)
        self.mutex = Lock()
    
    def generatePrimes(self, n):
        if n == 2:
            return [2]
        elif n < 2:
            return []
        s = range(3, n + 1, 2)
        mroot = n ** 0.5
        half = (n + 1) / 2 - 1
        i = 0
        m = 3
        while m <= mroot:
            if s[i]:
                j = (m * m - 3) / 2
                s[j] = 0
                while j < half:
                    s[j] = 0
                    j += m
            i = i + 1
            m = 2 * i + 3
        return [2] + [x for x in s if x]
    
    def generateMultiplesOfXUpToY(self, x, y):
        s = range(y / x)
        return [a * 2 for a in s]
    
    def checkPresence(self, n):
        return (n in self.__resource)

    def mine(self, prime):
        with self.mutex:
            if prime in self.__resource:
                self.removePrime(prime)
                return self._getValueOfPrime(prime)
            else:
                return 0

    def removePrime(self, prime):
        self.__resource.remove(prime)

    def _getValueOfPrime(self, prime):
        return int(math.ceil(math.log(prime, 2)))
