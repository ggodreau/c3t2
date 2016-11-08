#!/usr/bin/python

import pandas as pd
import sys
#import re
#import os

def main():

#    alpha = []
#    alpha = ['i', 'j', 'k']
#    newcol = 'newcolname'
#    colnames = ['id', 'googleperunc', 'samsunggalaxy']
#    sumCol(alpha, colnames, newcol)
    coltest = ['id', 'googleperunc', 'samsunggalaxy']
    df = pd.read_csv(getUserInputFile(), delimiter=',')
    global colIndex
    colIndex = {}
    for i, j in zip(df.columns.values, range(0,len(df.columns.values))):
        colIndex[i] = j
#    print df.ix[:,colIndex.get(coltest[0])]

    sumCol(coltest)
    setWeight()
#    for i, j, k in zip(df['id'], df['googleperunc'], df['samsunggalaxy']):
#        df['newcol'] = i+j+k
#    print df

    #headerLabels = ['url','iphone','samsunggalaxy','sonyxperia','nokialumina','htcphone','ios','googleandroid','iphonecampos','samsungcampos','sonycampos','nokiacampos','htccampos','iphonecamneg','samsungcamneg','sonycamneg','nokiacamneg','htccamneg','iphonecamunc','samsungcamunc','sonycamunc','nokiacamunc','htccamunc','iphonedispos','samsungdispos','sonydispos','nokiadispos','htcdispos','iphonedisneg','samsungdisneg','sonydisneg','nokiadisneg','htcdisneg','iphonedisunc','samsungdisunc','sonydisunc','nokiadisunc','htcdisunc','iphoneperpos','samsungperpos','sonyperpos','nokiaperpos','htcperpos','iphoneperneg','samsungperneg','sonyperneg','nokiaperneg','htcperneg','iphoneperunc','samsungperunc','sonyperunc','nokiaperunc','htcperunc','iosperpos','googleperpos','iosperneg','googleperneg','iosperunc','googleperunc']
    #df.columns = headerLabels
    #df.index.name = 'id'
    #for i in df['googleperunc']:
    #    df.ix[:,"googleperunc"]=i.rstrip('\)').replace(" ", "")
    #for i in df['iphone']:
    #    df.ix[:,'iphone']=i.lstrip('\(')

    # output factor and url files
    #df.to_csv('concatenated_websites.csv', columns=headerLabels[:1], quotechar='"', sep=',',header=True)
    #df.to_csv('concatenated_factors.csv', columns=headerLabels[1:], quotechar='"', sep=',',header=True)

    # cleanup
    #os.remove('combinedFile.csv')
    #print "Sucessfully processed " + str(fileCount) + " files"
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
        if i == 0:
            df['newcolname'] = df.ix[:,i]
        if i > 0:
            df['newcolname'] = df['newcolname'] + df.ix[:,i]
    #print df['newcolname']


def getWeight(index):
    pass
def setWeight():
    df = pd.read_csv(file, delimiter=',')
    weightList = [0] * len(df.columns.values)
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

    print weightDict


"""
def sumCol(alpha, colnames, newcolname):
    df = pd.read_csv('./concatenated_factors.csv', delimiter=',')
    print "colnames before:", colnames
#    print df[colnames]
    colnames =  map(lambda x: 'df[\'' + x + '\']', colnames)

    print type(colnames)
    print colnames[-1][-1]
#    colnames[-1] = colnames[-1][:-1]
    print "COLNAMES =", colnames
    print colnames[0], colnames[1], colnames[2]
    for i in colnames:
        print i
    colnames += map(lambda x: 'df[\'' + x + '\']', colnames[-1])

    for i, j, k in colnames:
#    for i, j, k in zip("df['id']", "df['googleperunc']", "df['samsunggalaxy']"):
      #  print i
     #   print j
    #    print k
        df['newcolname'] = i + j + k
    print df
"""

if __name__ == "__main__":
    main()


