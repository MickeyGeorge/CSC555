#!/usr/bin/python

import sys

currId = None  # this is the "current" key
currXs = []
currYs
id = None

# The input comes from standard input (line by line)
for line in sys.stdin:

    line = line.strip()
    ln = line.split('\t')
    id = ln[0]

    if curr_id == id:
        currXs.append(ln[1])
		currYs.append(ln[2])
    else:
        if curr_id:
		
			#calculate center
			centerX = sum(currXs)/len(currXs)
			centerY = sum(currYs)/len(currYs)
            print '%s %s' % (centerX, centerY)

        curr_id = id
        currXs.append(ln[1])
		currYs.append(ln[2])


# output the last key
if curr_id == id:
	#calculate center
	centerX = sum(currXs)/len(currXs)
	centerY = sum(currYs)/len(currYs)
	print '%s %s' % (centerX, centerY)
