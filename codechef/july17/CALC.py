#!/usr/bin/env python


def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        n, b = map(int, raw_input().strip().split(' '))
        result = 0
        if n%b == 0:
            aux_size = (n/b)
            if aux_size%2 == 0:
                c_sum = b*(aux_size/2)
                c_mult = (aux_size/2)
                result = c_sum * c_mult
            else:
                aux_ceil = (aux_size/2) + 1
                c_sum = aux_ceil*b
                c_mult = aux_size - aux_ceil
                result = c_sum * c_mult
        else:
            result = (n/b) * (n%b)

        print int(result)


if __name__ == '__main__':
    main()
