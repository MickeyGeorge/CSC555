#!/usr/bin/python

import sys

currentKey = None
quantity = None
revenue = None
nation = None

# input comes from STDIN
for line in sys.stdin:

    split = line.strip().split('\t')
    key = split[0]
    value = '\t'.join(split[1:])

    if currentKey == key: # Same key
        if value.endswith('lineorder'):
            quantity = split[1]
	    revenue = split[2]
        if value.endswith('customer'):
            nation = split[1]
    else:
        if currentKey:
            lenQuantity = len(quantity)
            lenRevenue = len(revenue)
	    lenNation = len(nation)
            if (lenQuantity*lenRevenue*lenNation > 0):
                # Join means that there have to be rows on each side
                print quantity, '\t', nation, '\t', revenue

        quantity = ''
        revenue = ''
        nation = ''
	currentKey = key

        if value.endswith('lineorder'):
            quantity = split[1]
            revenue = split[2]
	    nation = ''
        elif value.endswith('customer'):
            quantity = ''
            revenue = ''
	    nation = split[1]

            lenQuantity = len(quantity)
            lenRevenue = len(revenue)
	    lenNation = len(nation)

            if (lenQuantity*lenRevenue*lenNation > 0):
                # Join means that there have to be rows on each side
                print quantity, '\t', nation, '\t', revenue

lenQuantity = len(quantity)
lenRevenue = len(revenue)
lenNation = len(nation)

if (lenQuantity*lenRevenue*lenNation > 0):
    # Join means that there have to be rows on each side
    print quantity, '\t', nation, '\t', revenue
