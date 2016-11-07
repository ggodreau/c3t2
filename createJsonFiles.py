#!/usr/bin/env python
# reducer.py

import sys
import re
import os

#for fileName in os.listdir(sys.argv[1]):
#for filename in os.getcwd():
#fileName = "input.bdf"

def main():
    fileName = detectExistingFile()
    if fileName == "input.bdf":
        with open("./" + fileName) as infile:
            with open("./" + fileName[:-4] + '.json', 'w+') as outfile:

                # Begin a boolean flag
                isFirstLine = True
                # Print the JSON file header markup
                outfile.write("[\n")
                for line in infile:
                    # Parse the elements out of the line
                    linesplit=line.split("/")

                    segmentnumber = linesplit[6]
                    filerange = linesplit[8].rstrip()
		    print "filerange: %s", filerange

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


def getUserInputFile():
    file = raw_input("Enter input file: ")
    print "you entered ", file
    return file

def detectExistingFile():
    if os.path.isfile("input.bdf"):
        decision = raw_input("file \"input.bdf\" detected, do you want to use it for input?\n[y/n]")
	if decision == "n":
	    getUserInputFile()
	elif decision == "y":
            file = "input.bdf"
            return file
        else:
            sys.exit()

if __name__ == "__main__":
        main()

