#!/usr/bin/python

from operator import itemgetter
import sys
country_name = None
current_country = None
current_type = None
name_table = {}

count = 0

# We read from the standard input.
for line in sys.stdin:
    # Remove whitespaces at the beginning and the end of the line.
    line = line.strip()
    # Split the line to extract the key and the value.
    # country store country short name, value store pairs of value
    # values format: (0, 'South Africa'), (1, 'TMAX')
    country, typenumber = line.split('\t', 1)  
    country, type = country.split(',')
    
    
    
    # Hadoop sorts the output by key before it is parsed by the reducer.
    # Therefore, we know that we are counting the number of occurences of the
    # same word until the current word changes.
    if len(type) < 2:
    	name_table[country] = typenumber
    
    if current_country == country and current_type == type:
		count += int(typenumber)
    else:
		# We are done for this country and record type. Write the result to the standard output.
		if current_country in name_table and count > 0:
			print '%s\t%s\t%s' % (name_table[current_country], current_type , count)
		
		count = 0 if not typenumber.isdigit() else int(typenumber) 
		current_country = country
		current_type = type	

# This is needed to output the last word.
if country in name_table and count > 0:
    print '%s\t%s\t%s' % (name_table[country], current_type , count)