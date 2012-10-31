#!/usr/bin/env python
# A simple feedforward neural network that learns Primes

from pybrain.datasets import ClassificationDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised import BackpropTrainer

class EightBitBrain(object):
    
    def __init__(self, dataset, inNodes, outNodes, hiddenNodes, classes):
        self.__dataset = ClassificationDataSet(inNodes, classes-1)
        for element in dataset:
            self.addDatasetSample(self._binaryList(element[0]), element[1])
        self.__dataset._convertToOneOfMany()
        self.__network = buildNetwork(inNodes, hiddenNodes, self.__dataset.outdim, recurrent=True)
        self.__trainer = BackpropTrainer(self.__network, learningrate = 0.01, momentum = 0.99, verbose = True)
        self.__trainer.setData(self.__dataset)

    def _binaryList(self, n):
        return [int(c) for c in "{0:08b}".format(n)]
    
    def addDatasetSample(self, argument, target):
        self.__dataset.addSample(argument, target)

    def train(self, epochs):
        self.__trainer.trainEpochs(epochs)
    
    def activate(self, information):
        result = self.__network.activate(self._binaryList(information))
        highest = (0,0)
        for resultClass in range(len(result)):
            if result[resultClass] > highest[0]:
                highest = (result[resultClass], resultClass)
        return highest[1]
