#!/usr/bin/python
import sys
 
# input comes from STDIN (standard input)
for line in sys.stdin:
         
    line = line.strip()
    split = line.split(',')
         
    if split[0].endswith(' AM') or split[0].endswith(' PM'):
        if len(split[3]) > 0: # There are some blank licenses
            firstThree = split[3][:3]
            print firstThree, '\t', 'RelocatedVehicle'
    else: 
        if len(split[5]) > 0: # There are some blank licenses
            firstThree = split[5][:3]
            print firstThree, '\t', 'TowedVehicle'

