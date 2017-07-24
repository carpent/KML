'''
Created on 2017-7-7-

@author: Kevins
'''
import numpy as np
from operator import itemgetter

'''
K nearest Neighbors
'''
class KNN(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def knnClassfy(self, inX, dataSet, labels, k):
        # print(dataSet, labels)
        
        # dataSetSize = dataSet.shape[0]
        # print(dataSetSize)
        
        # diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
        # print(diffMat)
        
        # sqDiffMat = (np.tile(inX, (dataSetSize, 1)) - dataSet)**2
        # print(sqDiffMat)
        
        # sqDistances =((np.tile(inX, (dataSetSize, 1)) - dataSet)**2).sum(axis=1)
        # print(sqDistances)
        '''
        d=sqrt(sum((X-X0)**2))
        '''
        distances = (((np.tile(inX, (dataSet.shape[0], 1)) - dataSet)**2).sum(axis=1))**0.5
        # print(distances)
        
        sortedDistIndicies = distances.argsort()
        # print(sortedDistIndicies)
        
        classCount = {}
        for i in range(k):
            voteLabel = labels[sortedDistIndicies[i]]
            classCount[voteLabel] = classCount.get(voteLabel,0) + 1
        
        sortedClassCount = sorted(classCount.items(), 
                                  key = itemgetter(1), reverse = True)
        print(sortedClassCount)
        return sortedClassCount[0][0]