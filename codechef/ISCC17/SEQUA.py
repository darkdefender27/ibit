#!/usr/bin/env python

T = int(raw_input().strip())

for _ in xrange(T):
    n, m = map(int, raw_input().strip().split(' '))
    ans = 1 + (((n*(n+1)) * ((2*n)+1))/6)
    print ans%m
