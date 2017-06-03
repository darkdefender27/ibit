#!/usr/bin/env python

T = int(raw_input().strip())

for i in xrange(T):
	N, Q = map(int, raw_input().strip().split(' '))
	snakes = map(int, raw_input().strip().split(' '))
	sr_snakes = sorted(snakes)
	
	for ii in xrange(Q):
		K = int(raw_input().strip())
		count = 0
		R = N-1
		L = 0

		while(sr_snakes[R]>=K):
			count += 1
			R -= 1
		
		while(L<=R):
			m = K - sr_snakes[R]
			if(m <= R-L):
				count += 1
			L += m
			R -= 1

		print count 