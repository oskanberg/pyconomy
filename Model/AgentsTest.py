#!/usr/bin/env python

import unittest
from Agents import Kepler

class KeplerTest(unittest.TestCase):
    
    def testEducation(self):
        kepler = Kepler(0, 0, {}, 0, 0)
        kepler.educate(10)
        self.assertEqual(kepler.education, 10)
        
    def testLabour(self):
        kepler = Kepler(0, 0, {}, 0, 0)
        kepler.rest(10)
        self.assertEqual(kepler.labour, 10)

    def testLand(self):
        kepler = Kepler(0, 0, {}, 0, 0)
        kepler.bequeathLand(10)
        self.assertEqual(kepler.land, 10)

    def testGoods(self):
        kepler = Kepler(0, 0, {}, 0, 0)
        kepler.addGoods('food', 10)
        self.assertEqual(kepler.goods['food'], 10)

    def testDepreciateValue(self):
        kepler = Kepler(100, 0, {}, 0, 0)
        kepler.depreciate(10)
        self.assertEqual(kepler.value, 90)

    def testAppreciateValue(self):
        kepler = Kepler(100, 0, {}, 0, 0)
        kepler.appreciate(10)
        self.assertEqual(kepler.value, 110)

if __name__ == '__main__':
    unittest.main()
