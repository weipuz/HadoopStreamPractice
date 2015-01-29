#!/usr/bin/python
#


#Using the Hadoop Streaming API, write a Mapper and a Reducer that will
#find the maximum of the minimum daily temperatures, and the minimum of
#the maximum daily temperatures, for each day. 
# The data looks like this:
# AE000041196,20130101,TMAX,250,,,S,
# AG000060390,20130101,PRCP,0,,,S,
# AG000060390,20130101,TMAX,171,,,S,
# AG000060590,20130101,PRCP,0,,,S,
# AG000060590,20130101,TMAX,170,,,S,
# The output looks like this: 
#
# 

#
import sys 
import re

# We read from the standard input.
for line in sys.stdin:
    # Remove whitespaces at the beginning and the end of the line.
    #line = line.strip() 
    #line = re.sub('[^a-zA-Z ]+', '', line)
    # Split the line into words.
    words = line.split(',')
    # Count!
    if words[2]=="TMAX" or words[2]=="TMIN":
        # Write to stdout, using a tabulation between the key and the
        # value.
        if -79.0 <= float(words[3])/10 <= 59.0 :
        	print '%s\t%s' % (','.join(words[1:3]), float(words[3])/10)

