#!/usr/bin/env python
import sys


def solution(a, N):
    i, j, rainbow_ct, prev = 0, N-1, 1, 1
    while(i<=j):
        if(a[i] == a[j] and (a[i] == prev+1 or a[i] == prev)):
            if(a[i] != prev):
                rainbow_ct += 1
                prev = a[i]
        else:
            break
        i += 1
        j -= 1

    if rainbow_ct == 7:
        return "yes"
    else:
        return "no"


def read_from_file():
    sys.stdin = open('rainbowa.in', 'r')

    T = int(sys.stdin.readline().strip())

    for _ in xrange(T):
        N = int(sys.stdin.readline().strip())
        arr = map(int, sys.stdin.readline().strip().split(' '))

        print solution(arr, N)


def read_from_console():
    T = int(raw_input().strip())

    for _ in xrange(T):
        N = int(raw_input().strip())
        arr = map(int, raw_input().strip().split(' '))

        print solution(arr, N)


def main():
    read_from_file()
    # read_from_console()


if __name__ == '__main__':
    main()
