#!/usr/bin/env python

import sys
import re

# We read from the standard input.
for line in sys.stdin:
    # Remove whitespaces at the beginning and the end of the line.
    line = line.strip()
    line = re.sub('[^a-zA-Z ]+', '', line)
    # Split the line into words.
    words = line.split()
    # Count!
    for word in words:
        # Write to stdout, using a tabulation between the key and the value.
        print '%s\t%s' % (word, 1)

