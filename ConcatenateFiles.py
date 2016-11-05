#!/usr/bin/env python
# reducer.py

import sys
import re
import os

# associates URLs with to the term frequency counts
frequencyCount = {}

# Open/Create the output file
with open(sys.argv[1] + '/Concatenated.csv', 'w+') as outfile:

    try:
        with open(sys.argv[1] + '/MatrixHeader.csv') as headerfile:
            for line in headerfile:
                outfile.write(line + '\n')
    except:
        print 'No Header File'

    # Get the current directory's info with os.walk
    for dirname, dirnames, filenames in os.walk(sys.argv[1]):
        # For each sub folder
        for subdirname in dirnames:
            
            subdirpath = os.path.join(dirname, subdirname)
            
            for fileName in os.listdir(subdirpath):
                with open(subdirpath + "/" + fileName) as infile:
                    for line in infile:
                        line = re.sub(r'\s*?\(',r',',line)
                        line = re.sub(r'\)',r'',line)
                        outfile.write(line)
                        