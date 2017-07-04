#!/usr/bin/env python

T = int(raw_input().strip())

for _ in xrange(T):
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split(' '))

    l_ct, l_sum = 0, 0
