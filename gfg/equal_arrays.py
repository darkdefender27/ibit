#!/usr/bin/env python3
# Author: Shubham Utwal
# Link: http://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not/0


def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        b = list(map(int, input().strip().split(' ')))
        result = 1
        d = {}
        for i in a:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for ii in b:
            if ii in d:
                d[ii] -= 1
            else:
                result = 0
                break

        for k, v in d.items(): # Use d.iteritems() in Python 3
            if d[k] > 0:
                result = 0
                break

        print result


if __name__ == '__main__':
    main()
