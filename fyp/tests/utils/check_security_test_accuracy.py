from numpy import *
import numpy as np
import os

global p1
global p0
global numBad2Good
global numGood2Bad
global Accuracy_Rate
Accuracy_Rate = 0
numBad2Good = 0
numGood2Bad = 0

path = '/Users/MasterYideng/fyp/FYP/fyp'
rootdir = os.path.join(path, 'permissions')


def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = ones(numWords); p1Num = ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num/p1Denom)
    p0Vect = np.log(p0Num/p0Denom)
    return p0Vect, p1Vect, pAbusive


def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    global p1
    global p0
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok for tok in listOfTokens if len(tok) > 2]


def spamTest():
    global numBad2Good
    global numGood2Bad
    global Accuracy_Rate

    docList=[]; classList = []; fullText =[]
    for i in range(1,501):
        wordList = textParse(open(rootdir + '/bad/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open(rootdir + '/good/%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = range(500); testSet=[]
    for i in range(100):
        randIndex = int(random.uniform(0,len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex])
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    errorCount = 0;  GoodToBad = 0;BadToGood = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            if classifyNB(array(wordVector),p0V,p1V,pSpam) != 1:
                GoodToBad += 1
                numGood2Bad += 1
            else:
                BadToGood += 1
                numBad2Good += 1
            errorCount += 1
    Accuracy_Rate = Accuracy_Rate+((1-float(errorCount)/len(testSet))*100)
    print 'Accuracy Rate:%d%% ' % ((1-float(errorCount)/len(testSet))*100)


if __name__ == "__main__":
    for i in range(0, 10):
        spamTest()
    print 'Overall Accuracy Rate:%d%% ' % (Accuracy_Rate/10)
    print 'BadToGood: ', (numBad2Good/10)
    print 'GoodToBad: ', (numGood2Bad/10)
