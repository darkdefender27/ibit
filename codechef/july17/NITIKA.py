#!/usr/bin/env python

def stripAndCap(n):
    n = n[:1]
    return n.capitalize() + '.'


def main():
    T = int(raw_input().strip())

    for _ in xrange(T):
        res = ''
        names = raw_input().split(' ')
        for i in xrange(len(names)-1):
            res = res + stripAndCap(names[i]) + ' '
            i += 1

        res = res + names[len(names)-1].capitalize()

        print res


if __name__ == '__main__':
    main()
