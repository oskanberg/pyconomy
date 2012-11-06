#!/usr/bin/env python

import unittest
from Brains import EightBitBrain
from Resource import NaturalResource
from random import shuffle

DATASIZE = 255

class BrainTest(unittest.TestCase):
    
    global DATASIZE
    
    def test(self):
        dataset = []
        
        resource = NaturalResource(DATASIZE)
        e = 0
        for i in range(DATASIZE):
            if resource.checkPresence(i):
                dataset.append((i, 1))
            else:
                dataset.append((i, 0))
        shuffle(dataset)
        brain = EightBitBrain(dataset, 8, 1, 16, 2)
        
        print "training"
        brain.train(1000)
        for i in range(DATASIZE):
            print "Guess: %d || Real: %s" % (brain.activate(i), str(resource.checkPresence(i)))
        
if __name__ == '__main__':
    unittest.main()
