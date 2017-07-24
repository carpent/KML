'''
K nearest Neighbors
'''

import matplotlib.pyplot as plt

class TreePlotter(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.decisionNode = dict(boxstyle = "sawtooth", fc = "0.8")
        self.leafNode = dict(boxstyle = "round4", fc = "0.8")
        self.arrow_args = dict(boxstyle = "<-")
        return

    def plotNode(self, nodeTxt, centerPt, ParentPt, nodeType):
        self.createPlot.ax1.annotate(nodeTxt, xy = ParentPt, xycoords = 'axes fraction', \
            xyText = centerPt, textcoords = 'axec fraction',\
            va = "center", ha = "center", bbox = nodeType, arrowprops = self.arrow_args)
        return

    def createPlot(self):
        fig = plt.figure(1, facecolor='white')
        fig.clf()
        self.createPlot.ax1 = plt.subplot(111, frameon = False)
        self.plotNode(U'DecisionNode', (0,5, 0.1), (0.1, 0.5),self.decisionNode)
        self.plotNode(U'LeafNode', (0.8, 0.1), (0.3, 0.8), self.leafNode)
        plt.show()
        return

    def getNumLeaafs(self, myTree):
        numLeafs = 0
        firstStr = myTree.keys()[0]
        secondDict = myTree[firstStr]
        for key in secondDict.keys():
            if type(secondDict[key]).__name__ == 'dict':
                numLeafs += self.getNumLeaafs(secondDict[key])
            else:
                numLeafs += 1
        return numLeafs

    def getTreeDepth(self, myTree):
        maxDepth = 0
        firstStr = myTree.keys()[0]
        secondDict = myTree[firstStr]
        for key in secondDict.keys():
            if type(secondDict[key]).__name__ == 'dict':
                thisDepth = 1 + self.getTreeDepth(secondDict[key])
            else:
                thisDepth = 1
            if thisDepth > maxDepth:
                maxDepth = thisDepth
        return maxDepth

    def retrieveTree(self, i):
        listOfTrees = [{'no surfacing': {0: 'no', 1:{'flippers':{0:'no', 1:'yes'}}}}, \
            {'no surfacing': {0: 'no', 1:{'flippers':{0:{'head':{0: 'no', 1:'yes'}}, 1:'no'}}}}]
        return listOfTrees[i]

    def plotMidText(self, cntrPt, parentPt, txtString):
        xMid = (parentPt[0]-cntrPt[0])/2.0 + cntrPt[0]
        yMid = (parentPt[1]-cntrPt[1])/2.0 + cntrPt[1]
        self.createPlot.ax1.text(xMid, yMid, txtString)
        return
    
    def plotTree(self, myTree, parentPt, nodeTxt):
        numLeafs = self.getNumLeaafs(myTree)
        depth = self.getTreeDepth(myTree)
        firstStr = myTree.keys()[0]
        numLeafs = self.getNumLeaafs(myTree)
        cntrPt = (self.plotTree.xOff + (1.0 + float(numLeafs))/2.0/self.plotTree.totalW, \
            self.plotTree.yOff)
        self.plotMidText(cntrPt, parentPt, nodeTxt)
        self.plotNode(firstStr, cntrPt, parentPt, self.decisionNode)
        secondDict = myTree[firstStr]
        self.plotTree.xOff = self.plotTree.yOff - 1.0/self.plotTree.totalD
        for key in secondDict.keys():
            if type(secondDict[key]).__name__ == 'dict':
                self.plotTree(secondDict[key], cntrPt, str(key))
            else:
                self.plotTree.xOff = self.plotTree.xOff + 1.0/self.plotTree.totalW
                self.plotNode(secondDict[key], (self.plotTree.xOff, self.plotTree.yOff), \
                cntrPt, self.leafNode)
                self.plotMidText((self.plotTree.xOff + self.plotTree.yOff), cntrPt, str(key))
        self.plotTree.yOff = self.plotTree.yOff + 1.0/self.plotTree.totalD
        return

    def createPlot2(self, inTree):
        fig = plt.figure(1, facecolor='white')
        fig.clf()
        axprops = dict(xticks=[], yticks=[])
        self.createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
        self.plotTree.totalW = float(self.getNumLeaafs(inTree))
        self.plotTree.totalD = float(self.getTreeDepth(inTree))
        self.plotTree.xOff = -0.5/self.plotTree.totalW;
        self.plotTree.yOff = 1.0
        self.plotTree(inTree, (0.5,1.0),'')
        plt.show()
        return