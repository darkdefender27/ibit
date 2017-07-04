#!/usr/bin/env python

T = int(raw_input().strip())

for _ in xrange(T):
    s = list(raw_input().strip())
    u, d, prev = 0, 0, None
    for i in s:
        if i == 'U':
            if prev == 'D':
                prev = 'U'
                u += 1
            elif prev is None:
                prev = 'U'
                u += 1
        elif i == 'D':
            if prev == 'U':
                prev = 'D'
                d += 1
            elif prev is None:
                prev = 'D'
                d += 1

    if d < u:
        print d
    else:
        print u
