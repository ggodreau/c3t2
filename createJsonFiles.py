#!/usr/bin/env python
# reducer.py

import sys
import re
import os

def main():
    inputFileName = getUserInputFile()
    outputFileName = getUserOutputFile()
    if not detectExistingOutputFile(outputFileName):
        with open("./" + inputFileName) as infile:
            with open("./" + outputFileName + '.json', 'w+') as outfile:

                # Begin a boolean flag
                isFirstLine = True
                # Print the JSON file header markup
                outfile.write("[\n")
                lineCounter = 0
                # Check for non-URL entries in input file
		for line in infile:
                    if len(line) < 10:
                        print "Short line in input file, please check/rid your input file of extra blank lines. Exiting..."
                        sys.exit()
                    # Parse the elements out of the line
                    linesplit=line.split("/")
                    segmentnumber = linesplit[6]
                    filerange = linesplit[8].rstrip()

                    if(isFirstLine == False):
			outfile.write (",\n")
                    isFirstLine = False
                    # Print the markup for each line
                    outfile.write ("{\n")
                    outfile.write ("\"Name\": \"segment_" + segmentnumber + "_file_" + filerange.split("-")[3] + "\",\n")
                    outfile.write ("\"ActionOnFailure\": \"CONTINUE\",\n")
                    outfile.write ("\"Jar\": \"/home/hadoop/contrib/streaming/hadoop-streaming.jar\",\n")
                    outfile.write ("\"Args\":\n")
                    outfile.write ("[\n")
                    outfile.write ("\"-files\", \"s3://[S3 Bucket]/[Scripts Folder]/Mapper.py,s3://[S3 Bucket]/[Scripts Folder]/Reducer.py\",\n")
                    outfile.write ("\"-mapper\", \"Mapper.py\",\n")
                    outfile.write ("\"-reducer\", \"Reducer.py\",\n")
                    outfile.write ("\"-input\", \"s3://aws-publicdatasets/common-crawl/parse-output/segment/" + segmentnumber + "/" + filerange + "\",\n")
                    outfile.write ("\"-output\", \"s3://[S3 Bucket]/[Script Output Folder]/RR_1_" + segmentnumber + "_" + filerange + "\",\n")
                    outfile.write ("\"-inputformat\", \"SequenceFileAsTextInputFormat\"\n")
                    outfile.write ("]\n")
                    outfile.write ("}")
                    # Print the JSON file footer markup
                    outfile.write("]\n")
                    lineCounter += 1
                exitMessage()


def getUserInputFile():
    file = raw_input("Enter input file: ")
    return file

def getUserOutputFile():
    file = raw_input("Enter output file: ")
    return file

def detectExistingOutputFile(file):
    if os.path.isfile(file + '.json'):
        decision = raw_input("\nWARNING! If you proceed, you will overwrite your output file. Are you sure?\n[y/n]\n")
        if decision == "n":
            print "Exiting...\n"
            sys.exit()
        elif decision =="y":
            return False
    else:
        return False

def exitMessage():
    print "\nSuccessfully wrote", lineCounter, "lines to output file:", outputFileName

if __name__ == "__main__":
        main()

