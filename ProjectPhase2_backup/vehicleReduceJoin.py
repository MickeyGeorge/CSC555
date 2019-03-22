#!/usr/bin/python
  
import sys
  
currentKey = None
valsTowed = None
valsReloc = None
TotalCount = 0

# input comes from STDIN
for line in sys.stdin:

    split = line.strip().split('\t')
    key = split[0]
    value = '\t'.join(split[1:])

    if currentKey == key: # Same key
        if value.endswith('TowedVehicle'):
            valsTowed.append(value)
        if value.endswith('RelocatedVehicle'):
            valsReloc.append(value)
    else:
        if currentKey:
            lenTowed = len(valsTowed)
            lenReloc = len(valsReloc)
            if (lenTowed*lenReloc > 0):
                # Join means that there have to be rows on each side
                print currentKey, '\t', lenTowed*lenReloc
        valsTowed = []
        valsReloc = []
        currentKey = key
        if value.endswith('TowedVehcile'):
            valsTowed = [value]
            valsReloc = []
        elif value.endswith('RelocatedVehicle'):
            valsTowed = []
            valsReloc = [value]

            lenTowed = len(valsTowed)
            lenReloc = len(valsReloc)
            if (lenTowed*lenReloc > 0):
                # Join means that there have to be rows on each side
                print currentKey, '\t', lenTowed*lenReloc

lenTowedLast = len(valsTowed)
lenRelocLast = len(valsReloc)
if (lenTowedLast*lenRelocLast > 0):
    # Join means that there have to be rows on each side
    print currentKey, '\t', lenTowedLast*lenRelocLast