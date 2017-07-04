#!/usr/bin/env python
# Author :: Shubham Utwal
# Alias :: darkdefender27


def f(d):
    if d == 0:
        return 1
    elif d == 1:
        return 2
    else:
        return d**2 - (d**2-d)/2 + 1


def main():
    T = int(raw_input().strip())

    for _ in xrange(T):
        u, v = map(int, raw_input().strip().split(' '))
        ans = f(u+v)
        print ans + u


if __name__ == '__main__':
    main()
