#!/usr/bin/env python
# Author :: Shubham Utwal
# Alias :: darkdefender27


def number_needed(a, b):
    a_dict = {}
    b_dict = {}
    number_needed = 0

    for _ in xrange(len(a)):
        key = a[_]
        if key in a_dict:
            a_dict[key] += 1
        else:
            a_dict[key] = 1

    for _ in xrange(len(b)):
        key = b[_]
        if key in b_dict:
            b_dict[key] += 1
        else:
            b_dict[key] = 1

    for k, v in a_dict.iteritems():
        if k in b_dict:
            number_needed += abs(b_dict[k] - v)
            b_dict[k] = 0
        else:
            number_needed += v

    for k, v in b_dict.iteritems():
        number_needed += v

    return number_needed


def main():
    a = raw_input().strip()
    b = raw_input().strip()

    print number_needed(a, b)


if __name__ == '__main__':
    main()
