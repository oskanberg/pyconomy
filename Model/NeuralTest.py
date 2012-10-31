#!/usr/bin/env python
# A simple feedforward neural network that attempts to learn Primes

from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

class PrimesDataSet(ClassificationDataSet):
    """ A dataset for primes """

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

    def binaryString(self, n):
        return [int(c) for c in "{0:04b}".format(n)]

    def __init__(self):
        ClassificationDataSet.__init__(self, 4, 1)
        primes = self.generatePrimes(15)
        for prime in primes:
            b = self.binaryString(prime)
            self.addSample(b, [1])
        for n in range(15):
            if n not in primes and len(primes) <= 2 * len(self.generatePrimes(15)):
                b = self.binaryString(n)
                self.addSample(b, [0])
        self.randomize()

def testTraining():
    d = PrimesDataSet()
    d._convertToOneOfMany()
    n = buildNetwork(d.indim, 8, d.outdim, recurrent=True)
    t = BackpropTrainer(n, learningrate = 0.01, momentum = 0.99, verbose = True)
    t.trainOnDataset(d, 1000)
    t.testOnData(verbose=True)
    for i in range(15):
        print "Guess: %s || Real: %s" % (str(n.activate(i)), str(i in d.generatePrimes(10)))
    print d


if __name__ == '__main__':
    testTraining()
