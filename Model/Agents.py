#!/usr/bin/env python

class Agent(object):
    
    value = 0
    land  = 0
    goods = {}
    
    def __init__(self, value, land, goods):
        self.value = value
        self.land = land
        self.goods = goods
        
    def appreciate(self, value):
        self.value += value
    
    def depreciate(self, value):
        self.value -= value
        
    def addGoods(self, goods, amount):
        self.goods[goods] = self.goods.get(goods, 0) + amount
    
    def bequeathLand(self, land):
        self.land += land


class Kepler(Agent):
    
    education = 0
    labour    = 0
    
    def __init__(self, value, land, goods, education, labour):
        super(Kepler, self).__init__(value, land, goods)
        self.education = education
        self.labour = labour

    def educate(self, amount):
        self.education += amount

    def rest(self, amount):
        self.labour += amount
        
    def appreciate(self, value):
        Agent.appreciate(self, value)
    
    def depreciate(self, value):
        Agent.depreciate(self, value)
        
    def addGoods(self, goods, amount):
        Agent.addGoods(self, goods, amount)
    
    def bequeathLand(self, land):
        Agent.bequeathLand(self, land)


class Industry(Agent):
    
    def __init__(self, value, land, goods, education, labour):
        super(Industry, self).__init__(value, land, goods)
        
    def appreciate(self, value):
        Agent.appreciate(self, value)
    
    def depreciate(self, value):
        Agent.depreciate(self, value)
        
    def addGoods(self, goods, amount):
        Agent.addGoods(self, goods, amount)
    
    def bequeathLand(self, land):
        Agent.bequeathLand(self, land)
