#!/usr/bin/env python

def solution(A):
    MAX = 1000000
    A.sort()
    n, i, min_dist = len(A), 0, MAX
    while(i<n-1):
        if(A[i+1] - A[i] < min_dist):
            min_dist = A[i+1] - A[i]
        i +=1

    return min_dist


def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        A = map(int, raw_input().strip().split(' '))
        print A
        print solution(A)


if __name__ == '__main__':
    main()
