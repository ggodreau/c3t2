#!/usr/bin/env python
# reducer.py

import sys
import re
import os
        
for fileName in os.listdir(sys.argv[1]):
    if(fileName.endswith(".bdf")):
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
                    filerange = linesplit[7].rstrip()

                    if(isFirstLine == False):
                        outfile.write (",\n") 
                    isFirstLine = False
                    # Print the markup for each line
                    outfile.write ("{\n")
                    outfile.write ("\"Name\": \"BM_2_" + segmentnumber + "_" + filerange + "\",\n")
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
