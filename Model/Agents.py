#!/usr/bin/env python

class Agent(object):
    
    def __init__(self, messenger, value, land, goods):
        self.__value = value
        self.__land = land
        self.__goods = goods
        self.__messenger = messenger
        
    def _appreciateValue(self, value):
        self.value += value
    
    def _depreciateValue(self, value):
        self.value -= value
        
    def _addGoods(self, goods, amount):
        self.goods[goods] = self.goods.get(goods, 0) + amount
    
    def _bequeathLand(self, land):
        self.land += land
        
    def _sendMessage(self, message):
        self.__messenger.put(message)


class Kepler(Agent):
    
    def __init__(self, messenger, value, land, goods, education, labour, food):
        Agent.__init__(self, messenger, value, land, goods)
        self.__education = education
        self.__labour = labour
        self.__food = food
        self.__alive = True
        
    def isAlive():
        return self.__alive

    def educate(self, amount):
        self.__education += amount

    def rest(self, amount):
        self.__labour += amount
        
    def appreciate(self, value):
        self._appreciate(self, value)
    
    def depreciate(self, value):
        self._depreciate(self, value)
        
    def addGoods(self, goods, amount):
        self._addGoods(self, goods, amount)
    
    def bequeathLand(self, land):
        self._bequeathLand(self, land)
    
    def eat(self):
        if self.__food > 0:
            self.__food -= 1
            assert food >= 0, "Kepler food less than 0"
            return True
        else:
            return False
    
    def findFood(self):
        # check market        

    def necessities(self):
        if self.eat():
            if self.__food < 10:
               self.findFood()
            else:
                
        else:
            if self.findFood():
                if not self.eat():
                    self.die()
    
    def die():
        self.__alive = False
    
    def run(self):
        while self.__alive:
            if self.necessities()


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
