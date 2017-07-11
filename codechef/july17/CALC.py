#!/usr/bin/env python
import math as mt


def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        n, b = map(int, raw_input().strip().split(' '))
        result = 0
        aux_size = (n/b)
        c_sum = (b*(aux_size/2)) + (n%b)
        c_mult = int(mt.ceil((aux_size/2.0)))
        result = c_sum * c_mult

        print int(result)


if __name__ == '__main__':
    main()
