#!/usr/bin/env python

from sets import Set

w = eval(raw_input())

for i in range(w):
	result = "similar"
	
	r1 = raw_input().split(' ')
	r2 = raw_input().split(' ')
	
	if len(set(r1).intersection(r2)) < 2:
		result = "dissimilar"

	print result
