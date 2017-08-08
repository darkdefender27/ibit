#!/usr/bin/env python
T = int(raw_input().strip())

for _ in xrange(T):
    n, d = map(int, raw_input().strip().split(' '))
    arr = map(int, raw_input().strip().split(' '))

    possible, arr_sum = True, 0
    for i in xrange(n):
        arr_sum += arr[i]

    avg = arr_sum/n

    if avg%n != 0:
        possible = False

    operations, i, j = 0, 0, d
    while(j<n and possible):
        avg_1 = arr[i] + arr[j]
        if avg_1%2 != 0:
            possible = False
        if(arr[i] <= arr[j]):
            ops = (avg - arr[i])
            operations += ops
            arr[j] -= ops
            arr[i] += ops
        else:
            ops = (avg - arr[j])
            operations += ops
            arr[j] += ops
            arr[i] -= ops
        i += 1
        j += 1

    for ii in xrange(len(arr)):
        if arr[ii] != avg:
            possible = False
            break

    if possible:
        print operations
    else:
        print -1
