#!/usr/bin/python

from operator import itemgetter
import sys

current_date = None
current_type = None
current_value = 0
date = None
type = None

# We read from the standard input.
for line in sys.stdin:
    # Remove whitespaces at the beginning and the end of the line.
    line = line.strip()

    # Split the line to extract the key and the value.
    word, value = line.split('\t', 1)
    date, type = word.split(',')
    # Since we're using the standard input, everything is text. We have to
    # convert the count variable to an integer (we ignore the value if it cannot
    # be parsed).
    try:
        value = float(value)
    except ValueError:
        continue

    # Hadoop sorts the output by key before it is parsed by the reducer.
    # Therefore, we know that we are counting the number of occurences of the
    # same word until the current word changes.
    if current_date == date and current_type == type:
        current_value = min(current_value, value) if type == "TMAX" else max(current_value, value)
    else:
        # We are done for this word. Write the result to the standard output.
        if current_date:
            print '%s\t%s' % ((current_date, current_type) , current_value)
        current_date = date
        current_type = type
        current_value = value

# This is needed to output the last word.
if current_date == date and current_type == type:
    print '%s\t%s' % ((current_date, current_type) , current_value)
