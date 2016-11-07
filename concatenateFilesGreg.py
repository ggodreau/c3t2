#!/usr/bin/python

import pandas as pd


def main():
    df = pd.read_csv(getUserInputFile(), delimiter=',', quotechar='"')
    headerLabels = ['url','iphone','samsunggalaxy','sonyxperia','nokialumina','htcphone','ios','googleandroid','iphonecampos','samsungcampos','sonycampos','nokiacampos','htccampos','iphonecamneg','samsungcamneg','sonycamneg','nokiacamneg','htccamneg','iphonecamunc','samsungcamunc','sonycamunc','nokiacamunc','htccamunc','iphonedispos','samsungdispos','sonydispos','nokiadispos','htcdispos','iphonedisneg','samsungdisneg','sonydisneg','nokiadisneg','htcdisneg','iphonedisunc','samsungdisunc','sonydisunc','nokiadisunc','htcdisunc','iphoneperpos','samsungperpos','sonyperpos','nokiaperpos','htcperpos','iphoneperneg','samsungperneg','sonyperneg','nokiaperneg','htcperneg','iphoneperunc','samsungperunc','sonyperunc','nokiaperunc','htcperunc','iosperpos','googleperpos','iosperneg','googleperneg','iosperunc','googleperunc']
    df.columns = headerLabels
    df.index.name = 'id'
    for i in df['googleperunc']:
        df.ix[:,"googleperunc"]=i.rstrip('\)').replace(" ", "")
    for i in df['iphone']:
        df.ix[:,'iphone']=i.lstrip('\(')
    print df #df['googleperunc','iphone']
    df.to_csv('concatenated_websites.csv', columns=headerLabels[:1], quotechar='"', sep=',',header=True)
    df.to_csv('concatenated_factors.csv', columns=headerLabels[1:], quotechar='"', sep=',',header=True)

def getUserInputFile():
    file = raw_input("Enter input file: ")
    if file == "":
        file = "out_reducer.csv"
    return file

if __name__ == "__main__":
    main()


