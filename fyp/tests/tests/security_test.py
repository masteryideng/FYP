from numpy import *
import numpy as np
from ..utils.get_permissions import *

path = os.environ['root_dir']
rootdir = os.path.join(path, 'apk_samples', 'result')


def textParse(bigString):    # input is big string, output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok for tok in listOfTokens if len(tok) > 2]


def createVocabList(dataSet):
    vocabSet = set([])  # create empty set
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # union of the two sets
    return list(vocabSet)


def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
    return returnVec


def trainNB0(trainMatrix):
    numTrainDocs = len(trainMatrix)  # how many trainees
    numWords = len(trainMatrix[0])  #each trainee how many permissions
    pNum = zeros(numWords)
    for i in range(numTrainDocs):
        pNum += trainMatrix[i]
    return pNum/numWords


def test_security():
    good_num, bad_num = get_permissions_main()

    docList = []  # the permissions of each app seperately
    for i in range(1,good_num+1):
        wordList = textParse(open(rootdir + '/good%d.txt' % i).read())
        docList.append(wordList)
    for i in range(1, bad_num+1):
        wordList = textParse(open(rootdir + '/bad%d.txt' % i).read())
        docList.append(wordList)
    wordList = textParse(open(rootdir + '/test1.txt').read())
    docList.append(wordList)
    vocabList = createVocabList(docList)  # include all the permissions

    trainingSet = range(good_num)
    trainMat=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
    pMat_good = trainNB0(array(trainMat))
    # print pMat_good

    trainingSet = range(good_num, good_num+bad_num)
    trainMat=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
    pMat_bad = trainNB0(array(trainMat))
    # print pMat_bad

    wordList = textParse(open(rootdir + '/test1.txt').read())
    docList.append(wordList)

    testVec = setOfWords2Vec(vocabList, docList[good_num+bad_num+1])
    result1 = 1; result2 = 1
    for i in range(len(vocabList)):
        if testVec[i] != 0 and pMat_good[i] != 0:
            result1 += (np.log(testVec[i]) + np.log(pMat_good[i]))
        if testVec[i] != 0 and pMat_bad[i] != 0:
            result2 += (np.log(testVec[i]) + np.log(pMat_bad[i]))
    print result2, result1
    assert result1 >= result2
