#!/usr/bin/python

import pandas as pd
import sys
#import re
#import os

def main():

    getUserInputFile()
    setWeight()
    galaxySentIdx = ['samsunggalaxy']
    galaxySentCols = ['googleandroid']

    coltest = ['id', 'googleperunc', 'samsunggalaxy']
    df = pd.read_csv(file, delimiter=',')
    global colIndex
    colIndex = {}
    for i, j in zip(df.columns.values, range(0,len(df.columns.values))):
        colIndex[i] = j

#    sumCol(coltest)
    print getWeight(coltest)
    sys.exit()

def getUserInputFile():
    global file
    file = raw_input("Enter input file (leave blank for './concatenated_factors'): ")
    if file == "":
        file = "./concatenated_factors.csv"
    return file

def sumCol(colnames):
    df = pd.read_csv('./concatenated_factors.csv', delimiter=',')
    #for i, j, k in zip(*colnames
    colIndiciesToParse = []
    for i in range(0,len(colnames)):
        #print colIndex.get(colnames[i])
        colIndiciesToParse.append(colIndex.get(colnames[i]))
    #print colIndiciesToParse

    for i in colIndiciesToParse:
        print "i =", i
        if i == 0:
            df['newcolname'] = df.ix[:,i]
        if i > 0:
            df['newcolname'] = df['newcolname'] + df.ix[:,i]
    #print df['newcolname']
    print colIndex[20]

def getWeight(index):
    weights = []
    for i in index:
        weights.append(weightDict[i])
    return weights

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


if __name__ == "__main__":
    main()


