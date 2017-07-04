#!/usr/bin/env python3
import operator as op
import functools as ft

def nCr(n, r):
    if n < r: return 0
    r = min(r, n-r)
    if r == 0: return 1
    numer = ft.reduce(op.mul, range(n, n-r, -1))
    denom = ft.reduce(op.mul, range(1, r+1))
    return numer//denom


def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = 0
        ct_arr = [0]*3
        for i in range(n):
            arr[i] = arr[i]%3
            ct_arr[arr[i]] += 1

        result = result + ct_arr[0] * ct_arr[1] * ct_arr[2] + ct_arr[1] * ct_arr[2]
        result = result + nCr(ct_arr[0], 2) + nCr(ct_arr[0], 3)
        result = result + nCr(ct_arr[1], 3) + nCr(ct_arr[2], 3)

        print(result)


if __name__ == '__main__':
    main()
