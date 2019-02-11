#!/usr/bin/python
import sys

for line in sys.stdin:
        line = line.strip().split('\t')
        name = line[1].strip().split(' ')
		type = line[6].strip().split(' ')
        print '\t'.join([line[0],name[0],name[1], \
			line[2], line[3], line[4], line[5], \
			type[0], type[1], type[2], line[7], \
			line[8]])

	
SELECT TRANSFORM (p_partkey, p_name, p_mfgr, p_category, p_brand1, p_color, p_type, p_size, p_container) USING 'assignment3.py' AS (p_partkey, p_name1, p_name2 ,p_mfgr, p_category, p_brand1, p_color, p_type1, p_type2, p_type3, p_size, p_container) FROM part;

INSERT OVERWRITE TABLE part2 SELECT TRANSFORM (p_partkey, p_name, p_mfgr, p_category, p_brand1, p_color, p_type, p_size, p_container) USING 'assignment3.py' AS (p_partkey, p_name1, p_name2 ,p_mfgr, p_category, p_brand1, p_color, p_type1, p_type2, p_type3, p_size, p_container) FROM part;





