from numpy import *
import numpy as np
from ..utils.get_permissions import get_test_permission
from html import HTML
from datetime import datetime
from androguard.core.bytecodes import apk
import os

global p1
global p0
path = os.environ['root_dir']
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


def test_security():
    global p1
    global p0
    get_test_permission('android-debug.apk')

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
    wordList = textParse(open(rootdir + '/test/1.txt').read())
    docList.append(wordList)
    fullText.extend(wordList)

    vocabList = createVocabList(docList)
    trainingSet = range(500); testSet=[1000]
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(array(trainMat),array(trainClasses))
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector),p0V,p1V,pSpam) != 1:
            assert True
        else:
            assert False

    package = get_package(os.environ['app'])
    result_good = '%.2f' % p0
    result_bad = '%.2f' % p1
    gen_html_report(package, result_good, result_bad)


def gen_html_report(apk_file, result_good, result_bad):
    h = HTML()

    h.h2('Security Test Report')
    h.li(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    h.li(apk_file)

    h.br

    t = h.table(border='1')
    r = t.tr
    r.th('Probability to Good')
    r.th('Probability to Malware')

    r = t.tr
    r.td(result_good)
    r.td(result_bad)

    with open('security_test_report.html', 'w') as r:
        r.write(str(h))


def get_package(path):
    app = apk.APK(path)
    packname = app.get_package()
    return packname