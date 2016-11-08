#!/usr/bin/python

import pandas as pd
import sys
#import re
#import os

def main():
    alpha = []
    alpha = ['i', 'j', 'k']
    newcol = 'newcolname'
    colnames = ['id', 'googleperunc', 'samsunggalaxy']
    sumCol(alpha, colnames, newcol)
#    df = pd.read_csv(getUserInputFile(), delimiter=',')
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
    file = raw_input("Enter input file (leave blank for './concatenated_factors'): ")
    if file == "":
        file = "./concatenated_factors.csv"
    return file

def sumCol(alpha, colnames, newcolname):
    df = pd.read_csv('./concatenated_factors.csv', delimiter=',')
    print "colnames before:", colnames
#    print df[colnames]
    colnames =  map(lambda x: 'df[\'' + x + '\']', colnames)
    print "colnames after:", colnames
    print colnames[0], colnames[1], colnames[2]
    for i, j, k in zip(*colnames):
    #for i, j, k in zip(df['id'], df['googleperunc'], df['samsunggalaxy']):
        df['newcolname'] = i + j + k
    print df
 

if __name__ == "__main__":
    main()


