# c3t2
Course 3 Task 2 updates

This is a collection of scripts to map/reduce and process a hadoop streaming job within AWS run against common crawl textData files.

Note the dependent libraries in requirements.txt.

createJsonFiles.py
---
This script takes a CR+LF delimited list of paths to warc.wet.gz files within AWS and outputs a json file that can be passed to the AWS CLI within a hadoop job step.

Use:
'''bash
python createJsonFiles.py
'''
The script will ask you for the input and output file names upon execution.

mapper.py
---
To run the Mapper.py file locally, use the following syntax to place the output in 'out_mapper.txt'. Note that you will have to gunzip the warc.wet.gz file prior to processing it.

Use (locally):

'''python
cat CC-MAIN-XXX.ec2.internal.warc.wet | python Mapper.py > out_mapper.txt
'''
to determine the number of rows in the output file:
'''bash
wc -l out.txt
'''
reducer.py
---
To run the Reducer_NEW.py file locally, use the following syntax too place the outut in 'out_reducer.csv'

Use (locally):
'''bash
cat out_mappper.txt | python Reducer_New.py > out_reducer.txt
'''
concatenate.py
---
This script will automatically walk through a list of folders (one level deep only) and look for the output files of the AWS map/reduce job. It looks into the files to see if they have an http URL within the file before adding them to the job to be concatenated.
'''bash
python concatenate.py
'''
The script will ask you the root location from which to start the walk of directories. If nothing is entered, it will begin walking from the current working directory. The output will be two files: 'concatenated_websites.csv' and 'concatenated_factors.csv'. They can be joined with the first column in each file, 'id'.

robolabel.py
---
This script automatically assigns sentiment labels to both the iphone and galaxy datasets. The weights of different factors can be varied, as can the noise induced into the labels. The labels are positive integers for positive sentiment, and negative integers for negative sentiment. There is no limit to the value of this label, and it is not normalized within the dataset.

Use:
'''bash
python robolabel.py
'''
The script will ask you for an input file. If none is given, it will default to './concatenated_factors.csv'. The output (non-configurable) is './sentiment.csv'. The output csv file has three columns: id, iphoneSentiment, and galaxySentiment. Note that the id field can be keyed to the id field of both concatenated_websites.csv and concatenated_factors.csv (output files from concatenate.py) to obtain the origin factor and URL information.
