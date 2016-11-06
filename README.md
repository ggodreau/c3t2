# c3t2
Course 3 Task 2 updates

Mapper.py
---
To run the Mapper.py file locally, use the following syntax to place the output in 'out_mapper.txt'

cat <CC-MAIN-XXX.ec2.internal.warc.wet> | python <Mapper.py> > out_mapper.txt

to determine the number of rows in the output file:

wc -l out.txt

Reducder_New.py
---
To run the Reducer_NEW.py file locally, use the following syntax too place the outut in 'out_reducer.csv'

cat out_mappper.txt | python Reducer_New.py > out_reducer.txt


