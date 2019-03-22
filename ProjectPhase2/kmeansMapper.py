#!/usr/bin/python

import sys

fd = open('centers.txt', 'r')
centers = []
for line in fd:
	line = line.strip()
    vals = line.split(' ')
	centers.extend([vals])
fd.close()

for line in sys.stdin:
    line = line.strip()
	vals = line.split(' ')
	
	clusterNum = None
	distance = None
	i = 0
	
	#compare to each center and store the smallest distance
	for center in centers:
	
		euclidDist = sqrt( (vals[0]-center[0])**2 + (vals[1]-center[1])**2)
		
		if clusterNum:
			if euclidDist < distance:
				custerNum = i+1
				distance = euclidDist				
		else: #always record the first cluster
			custerNum = i+1
			distance = euclidDist
		
		i += 1
	
	print(clusterNum, '/t', vals[0], '/t', vals[1])

