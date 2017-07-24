'''
Created on 2017-7-8

@author: Kevins
'''
from math import log
import operator

class DecisionTree(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def calcShannonEntropy(self, dataSet):
        numEntries = len(dataSet)
        labelCounts = {}
        for featVec in dataSet:
            currentLabel = featVec[-1]    
            labelCounts[currentLabel] = labelCounts.get(currentLabel,0) + 1
            # if currentLabel no in labelCounts.keys():
            #     labelCounts[currentLabel] = 0
            # labelCounts[currentLabel] += 1
        shannonEntropy = 0.0
        for key in labelCounts:
            prob = float(labelCounts[key])/numEntries
            shannonEntropy -= prob * log(prob, 2)
        return shannonEntropy

    def splitDataSet(self, dataSet, axis, value):
        retDataSet = []
        for featVec in dataSet:
            if featVec[axis] == value:
                reducedFeatVec = featVec[:axis]
                reducedFeatVec.extend(featVec[axis+1:])
                retDataSet.append(reducedFeatVec)
        return retDataSet

    def chooseBestFeatureToSplit(self, dataSet):
        numFeatures = len(dataSet[0]) - 1
        baseEntropy = self.calcShannonEntropy(dataSet)
        bestGain = 0.0
        bestFeature = -1
        for i in range(numFeatures):
            featList = [example[i] for example in dataSet]
            uniqueVals = set(featList)
            newEntropy = 0.0
            for value in uniqueVals:
                subDataSet = self.splitDataSet(dataSet, i, value)
                prob = len(subDataSet)/float(len(dataSet))
                newEntropy += (prob * self.calcShannonEntropy(subDataSet))
            InfoGain = baseEntropy - newEntropy
            if InfoGain > bestGain:
                bestGain = InfoGain
                bestFeature = i
        return bestFeature

    def majorityCnt(self, classList):
        classCount = {}
        for vote in classList:
            # if vote not in classCount.keys: classCount[vote] = 0
            classCount[vote] = classCount.get(vote, 0) + 1
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    def createDecisionTree(self, dataSet, labels):
        classList = [example[-1] for example in dataSet]
        if classList.count(classList[0]) == len(classList):
            return classList[0]
        if len(dataSet[0]) == 1:
            return self.majorityCnt(classList)
        bestFeat = self.chooseBestFeatureToSplit(dataSet)
        bestFeatLabel = labels[bestFeat]
        decTree = {bestFeatLabel:{}}
        del(labels[bestFeat])
        featValues = [example[bestFeat] for example in dataSet]
        uniqueVals = set(featValues)
        for value in uniqueVals:
            subLabels = labels[:]
            decTree[bestFeatLabel][value] = self.createDecisionTree(self.splitDataSet(dataSet, bestFeat, value), subLabels)
        return decTree
    