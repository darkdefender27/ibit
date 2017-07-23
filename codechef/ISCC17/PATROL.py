#!/usr/bin/env python

T = int(raw_input().strip())

for _ in xrange(T):
    u, v, x = map(int, raw_input().strip().split(' '))
    print '{0:.10f}'.format(x/((u+v)*1.0))
