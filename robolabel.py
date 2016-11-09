#!/usr/bin/python

import pandas as pd
import numpy as np
import random
import sys

def main():

    # initialize global variables
    getUserInputFile()
    setWeight()
    setIdx()
    random.seed()

    # calculate sentiment for galaxy
    galaxySentIdx = ['samsunggalaxy']
    outputColLabelGal = ['galaxySentiment']
    galaxySentFactors = ['samsungcampos', 'samsungcamneg', 'samsungcamunc',
        'samsungdispos', 'samsungdisneg', 'samsungdisunc', 'samsungperpos',
        'samsungperneg', 'samsungperunc', 'googleperpos', 'googleperneg',
        'googleperunc']

    dfGalaxy = sumCol(galaxySentIdx, galaxySentFactors, outputColLabelGal).ix[:,outputColLabelGal[0]]

    # calculate sentiment for iphone
    iphoneSentIdx = ['iphone']
    outputColLabelIp = ['iphoneSentiment']
    iphoneSentFactors = ['iphonecampos', 'iphonecamneg', 'iphonecamunc',
        'iphonedispos', 'iphonedisneg', 'iphonedisunc', 'iphoneperpos',
        'iphoneperneg', 'iphoneperunc', 'iosperpos', 'iosperneg',
        'iosperunc']

    dfIphone = sumCol(iphoneSentIdx, iphoneSentFactors, outputColLabelIp).ix[:,outputColLabelIp[0]]

    # concatenate galaxy and iphone dataframes, write to file
    sentiment = pd.concat([dfGalaxy, dfIphone], axis=1)
    sentiment.to_csv('./sentiment.csv')

    print "All tasks successful, output file is \'sentiment.csv\'"
    sys.exit()

def getUserInputFile():
    global file
    file = raw_input("Enter input file (leave blank for './concatenated_factors'): ")
    if file == "":
        file = "./concatenated_factors.csv"
    return file

def sumCol(sentIdx, colnames, sentimentColName):
    df = pd.read_csv(file, delimiter=',')
    colIndiciesToParse = []
    for i in range(0,len(colnames)):
        colIndiciesToParse.append(colIndex.get(colnames[i]))
    for i, j, k in zip(colIndiciesToParse, range(0,len(colIndiciesToParse)), colnames):
        if j == 0:
            print "i = ", i
#            print "LOOP WEIGHT =", getWeight(k)
            df[sentimentColName[0]] = df.ix[:,i] * getWeight(k)
        if j > 0:
            df[sentimentColName[0]] = df[sentimentColName[0]] + (df.ix[:,i] * getWeight(k))

    # zero sentiment values where sentIdx == 0, add noise
    for i, j, k in zip(df[sentimentColName[0]], df.ix[:,colIndex.get(sentIdx[0])], df.ix[:,0]):
        if j == 0:
#            df.iloc[k,sentimentColName[0]] = 0
            df.iloc[k][sentimentColName[0]] = 0
        else:
            df.iloc[k][sentimentColName[0]] = df.iloc[k][sentimentColName[0]] + random.randrange(-2,2,1)
    return df

def getIdx(colname):
    return colIndex[colname]

def setIdx():
    df = pd.read_csv(file, delimiter=',')
    global colIndex
    colIndex = {}
    for i, j in zip(df.columns.values, range(0,len(df.columns.values))):
        colIndex[i] = j

def getWeight(colname):
    return weightDict.get(colname)

def setWeight():
    df = pd.read_csv(file, delimiter=',')
    #initialize column indicies, set all weights to 0
    weightList = [0] * len(df.columns.values)
    global weightDict
    weightDict = {}
    for i, j in zip(df.columns.values, weightList):
        weightDict[i] = j

    # device
    weightDict['iphone'] = 0
    weightDict['samsunggalaxy'] = 0

    # OS
    weightDict['ios'] = 0
    weightDict['googleandroid'] = 0

    # camera
    weightDict['iphonecampos'] = 10
    weightDict['samsungcampos'] = 10
    weightDict['iphonecamneg'] = -10
    weightDict['samsungcamneg'] = -10
    weightDict['iphonecamunc'] = 1
    weightDict['samsungcamunc'] = 1

    # display
    weightDict['iphonedispos'] = 10
    weightDict['samsungdispos'] = 10
    weightDict['iphonedisneg'] = -10
    weightDict['samsungdisneg'] = -10
    weightDict['iphonedisunc'] = 1
    weightDict['samsungdisunc'] = 1

    # device performance
    weightDict['iphoneperpos'] = 10
    weightDict['samsungperpos'] = 10
    weightDict['iphoneperneg'] = -10
    weightDict['samsungperneg'] = -10
    weightDict['iphoneperunc'] = 1
    weightDict['samsungperunc'] = 1

    # OS performance
    weightDict['iosperpos'] = 10
    weightDict['googleperpos'] = 10
    weightDict['iosperneg'] = -10
    weightDict['googleperneg'] = -10
    weightDict['iosperunc'] = 1
    weightDict['googleperunc'] = 1

    print "DIS WEIGHT", weightDict['iosperneg']
if __name__ == "__main__":
    main()


