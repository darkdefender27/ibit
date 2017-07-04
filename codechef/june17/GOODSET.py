#!/usr/bin/env python

T = int(raw_input().strip())

for ii in xrange(T):
    n = int(raw_input().strip())
    res = []
    bad_set = []

    for _ in xrange(1, n+1):
        if _ == 1:
            res.append(1)
        elif _ == 2:
            res.append(2)
        elif _ == 3:
            res.append(4)
            bad_set.append(3)
        else:
            res.append(res[-1]+bad_set[0])

    for i in res:
        print i,
