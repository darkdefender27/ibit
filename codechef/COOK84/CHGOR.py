#!/usr/bin/env python

T = int(raw_input().strip())

for _ in xrange(T):
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    res = 0
    for i in arr:
        res = res | i

    print res
