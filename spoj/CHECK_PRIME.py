#!/usr/bin/env python
import math


def check_if_prime(num):
    i, ii, sq, res = 2, num, math.sqrt(num), True
    while i <= sq and res:
        if ii%i == 0:
            res = False
        i += 1
    return res


def main():
    from sys import stdin, stdout
    T = int(stdin.readline())

    for _ in xrange(T):
        n, k = map(int, stdin.readline().split(' '))

        while n <= k:
            if n > 1:
                is_prime = check_if_prime(n)
                if is_prime:
                    print n
            n = (n + 1) if n==2 or n==1 else (n + 2)
        # print "\n"


if __name__ == '__main__':
    main()
