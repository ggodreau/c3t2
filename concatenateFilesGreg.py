#!/usr/bin/python

import pandas as pd


def main():
    df = pd.read_csv(getUserInputFile(), delimiter=',', quotechar='"')
    df.columns = ['url','iphone','samsunggalaxy','sonyxperia','nokialumina','htcphone','ios','googleandroid','iphonecampos','samsungcampos','sonycampos','nokiacampos','htccampos','iphonecamneg','samsungcamneg','sonycamneg','nokiacamneg','htccamneg','iphonecamunc','samsungcamunc','sonycamunc','nokiacamunc','htccamunc','iphonedispos','samsungdispos','sonydispos','nokiadispos','htcdispos','iphonedisneg','samsungdisneg','sonydisneg','nokiadisneg','htcdisneg','iphonedisunc','samsungdisunc','sonydisunc','nokiadisunc','htcdisunc','iphoneperpos','samsungperpos','sonyperpos','nokiaperpos','htcperpos','iphoneperneg','samsungperneg','sonyperneg','nokiaperneg','htcperneg','iphoneperunc','samsungperunc','sonyperunc','nokiaperunc','htcperunc','iosperpos','googleperpos','iosperneg','googleperneg','iosperunc','googleperunc']
    for i in df['googleperunc']:
        df.ix[:,"googleperunc"]=i.rstrip('\)')
    for i in df['iphone']:
        df.ix[:,'iphone']=i.lstrip('\(')
    print df #df['googleperunc','iphone']

def getUserInputFile():
    file = raw_input("Enter input file: ")
    if file == "":
        file = "out_reducer.csv"
    return file

if __name__ == "__main__":
    main()


