#!/usr/bin/python
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
         
    line = line.strip().split('|')
         
    if line[1].startswith('Customer#'):
        if line[5] == 'AMERICA': # Return on matching records
            print line[0], '\t', line[4], '\t', 'customer'
	# lineorder
    else: 
        if 3 <= line[11] <= 5: # Return on matching records
            print line[2], '\t', line[8], '\t', line[12], '\t', 'lineorder'

