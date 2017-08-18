#!/usr/bin/env python
T = int(raw_input().strip())

for _ in xrange(T):
    n, d = map(int, raw_input().strip().split(' '))
    arr = map(int, raw_input().strip().split(' '))

    possible, arr_sum = True, 0
    for i in xrange(n):
        arr_sum += arr[i]

    if arr_sum%n == 0:
        avg, no_of_ops = (arr_sum/n), 0
        for i in xrange(d):
            d_sum, d_ct = 0, 0
            for ii in xrange(i, n, d):
                d_sum += arr[ii]
                d_ct += 1

            if d_sum%d_ct == 0 and (d_sum/d_ct) == avg:
                d_avg, ops = (d_sum/d_ct), 0
                for iii in xrange(i, n, d):
                    if arr[iii] != d_avg and (iii + d) >= n:
                        possible = False
                        break
                    else:
                        diff = abs(arr[iii] - d_avg)
                        if arr[iii] - d_avg > 0:
                            arr[iii] -= diff
                            arr[iii+d] += diff
                        elif arr[iii] - d_avg < 0:
                            arr[iii] += diff
                            arr[iii+d] -= diff
                        ops += diff
                no_of_ops += ops
            else:
                possible = False
                break
    else:
        possible = False

    if possible:
        print no_of_ops
    else:
        print -1
