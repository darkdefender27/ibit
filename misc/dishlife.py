#!/usr/bin/env python

from sets import Set

t = int(raw_input().strip())

for a0 in xrange(t):
    a = map(int, raw_input().strip().split(' '))
    n = a[0]
    k = a[1]
    result = "all"

    bucket = set()
    for i in range(n):
    	ii = map(int, raw_input().strip().split(' '))
    	num_ing = ii[0]
    	ing = ii[1:]
    	bucket.update(set(ing))
    	if len(ing) == k:
    		result = "some"

    if len(bucket) != k:
		result = "sad"

    print result