from numpy import *
import numpy as np
from ..utils.get_permissions import get_test_permission
from html import HTML
from datetime import datetime
from androguard.core.bytecodes import apk
import os

path = os.environ['root_dir']
rootdir = os.path.join(path, 'permissions')


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
    numWords = len(trainMatrix[0])  # each trainee how many permissions
    pNum = zeros(numWords)
    for i in range(numTrainDocs):
        pNum += trainMatrix[i]
    return pNum/numWords


def test_security():

    get_test_permission('android-debug.apk')
    docList = []  # the permissions of each app seperately
    for i in range(1,501):
        wordList = textParse(open(rootdir + '/good/%d.txt' % i).read())
        docList.append(wordList)
    for i in range(1, 501):
        wordList = textParse(open(rootdir + '/bad/%d.txt' % i).read())
        docList.append(wordList)
    wordList = textParse(open(rootdir + '/test/1.txt').read())
    docList.append(wordList)
    vocabList = createVocabList(docList)  # include all the permissions

    trainingSet = range(500)
    trainMat=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
    pMat_good = trainNB0(array(trainMat))
    # print pMat_good

    trainingSet = range(500, 1000)
    trainMat=[]
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
    pMat_bad = trainNB0(array(trainMat))
    # print pMat_bad

    wordList = textParse(open(rootdir + '/test/1.txt').read())
    docList.append(wordList)

    testVec = setOfWords2Vec(vocabList, docList[1001])
    result1 = 1; result2 = 1
    for i in range(len(vocabList)):
        if testVec[i] != 0 and pMat_good[i] != 0:
            result1 += (np.log(testVec[i]) + np.log(pMat_good[i]))
        if testVec[i] != 0 and pMat_bad[i] != 0:
            result2 += (np.log(testVec[i]) + np.log(pMat_bad[i]))
    package = get_package(os.environ['app'])
    result_good = '%.2f%%' % (100*result1/(result1+result2))
    result_bad = '%.2f%%' % (100*result2/(result1+result2))
    gen_html_report(package, result_good, result_bad)
    assert result1 >= result2


def gen_html_report(apk_file, result_good, result_bad):
    h = HTML()

    h.h2('Security Test Report')
    h.li(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    h.li(apk_file)

    h.br

    t = h.table(border='1')
    r = t.tr
    r.th('Similarity to Good')
    r.th('Similarity to Malware')

    r = t.tr
    r.td(result_good)
    r.td(result_bad)

    with open('security_test_report.html', 'w') as r:
        r.write(str(h))


def get_package(path):
    app = apk.APK(path)
    packname = app.get_package()
    return packname
