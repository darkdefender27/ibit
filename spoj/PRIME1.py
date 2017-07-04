#!/usr/bin/env python


def mark_all_mults(num, i, arr):
    for j in xrange(i, len(arr)):
        if arr[j] != -1 and arr[j]%num == 0:
            arr[j] = -1


def main():
    from sys import stdin, stdout
    T = int(stdin.readline())

    for _ in xrange(T):
        n, k = map(int, stdin.readline().split(' '))
        a = range(2, k+1)

        for i in xrange(len(a)):
            if a[i] > 1: # Marked
                mark_all_mults(a[i], i+1, a)

        for ii in xrange(len(a)):
            if a[ii] >= n:
                print a[ii]
        print "\n"


if __name__ == '__main__':
    main()
