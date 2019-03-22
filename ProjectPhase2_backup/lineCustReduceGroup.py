#!/usr/bin/python
import sys

curr_id = None
curr_tot = 0
id = None

# The input comes from standard input (line by line)
for line in sys.stdin:
	# parse the line and split it by '\t'
	line = line.strip().plit('\t')

	# grab the key
	id = line[0] + ' ' + line[1]
		
	# grab the value (int)
	val = int(line[2])

	if curr_id == id:
		curr_tot += val
	else:
		if curr_id: # output the sum, single key completed
			print '%s\t%s\t%d' % (line[0], line[1], curr_tot)

			curr_id = id
			curr_tot = val

# output the last key
if curr_id == id:
    print '%s\t%s\t%d' % (line[0], line[1], curr_tot)
