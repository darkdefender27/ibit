#!/usr/bin/env python

S = int(raw_input().strip())

for i in xrange(S):
	is_valid_strip = "yes"
	ni = int(raw_input().strip())
	ii = map(int, raw_input().strip().split(' '))

	if(ni%2==0 or ii[0]!=1 or ii[-1]!=1):
		is_valid_strip = "no"
	else:
		j = 1
		while(j < (ni/2)+1):
			if(ii[j] != ii[-j-1] or ii[j] != ii[j-1]+1):
				is_valid_strip = "no"
				break
			j += 1

	print is_valid_strip