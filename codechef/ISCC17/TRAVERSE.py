#!/usr/bin/env python

T = int(raw_input().strip())

for _ in xrange(T):
    m = int(raw_input().strip())
    x, y = 0, 0

    if m > 0:
        x, y = m/3, 2*(m%3)
        if (m%3) == 1:
            x += 1
        elif (m%3) == 2:
            x += 1
            y += 1

    print x, y
