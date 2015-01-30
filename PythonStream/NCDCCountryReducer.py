#!/usr/bin/python

from operator import itemgetter
import sys
country_name = None
current_country = None
current_type = None


count = 0

# We read from the standard input.
for line in sys.stdin:
    # Remove whitespaces at the beginning and the end of the line.
    line = line.strip()
    # Split the line to extract the key and the value.
    # country store country short name, value store pairs of value
    # values format: (0, 'South Africa'), (1, 'TMAX')
    country, value = line.split('\t', 1)  
    typenumber, type = value.split(',')
    typenumber = int(typenumber)
    
    # Hadoop sorts the output by key before it is parsed by the reducer.
    # Therefore, we know that we are counting the number of occurences of the
    # same word until the current word changes.
    
    if current_country == country and current_type == type:
        count += typenumber
    else:
        # We are done for this country and record type. Write the result to the standard output.
        if country_name and count > 0:
            print '%s\t%s\t%s' % (country_name, current_type , count)
        if typenumber == 0: 
        	country_name = type 
        	current_type = None
        else: 
        	current_type = type
        count = typenumber
        current_country = country	
        
        

# This is needed to output the last word.
if current_country == country and current_type == type and country_name:
    print '%s\t%s\t%s' % (country_name, current_type , count)
