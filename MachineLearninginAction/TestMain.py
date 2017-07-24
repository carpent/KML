'''
Created on 2017-7-7

@author: Kevins
'''
import numpy as np
from MLRepo import KNN
from MLRepo import DecisionTree

def createKNNDataSet():
    group = np.array([[1,1.1],[1,1],[1,0.9],[0.9,1],[0,0],[0,0.1],[0.1,0.1],[0.1,0]])
    labels = ['A', 'A', 'A','A','B', 'B','B','B']
    return group, labels

def createDecTreeDataSet():
    dataSet = [[1,1,'yes'], [1,1,'yes'], [1,0,'no'], [0,1,'no'], [0,0,'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

if __name__ == '__main__':
    
    # group, labels = createKNNDataSet()
    # kNN = KNN.KNN()
    # kNN.knnClassfy([0,0], group, labels, 3)

    dataSet, labels = createDecTreeDataSet()
    DTree = DecisionTree.DecisionTree()
    decTree = DTree.createDecisionTree(dataSet, labels)
