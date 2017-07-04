#!/usr/bin/env python

def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        n = int(raw_input().strip())
        if n==0:
            result = False
        else:
            result = True

        while n>0:
            if n&1 == 0:
                result = False
                break
            n = n >> 1

        if result:
            print "Yes"
        else:
            print "No"


if __name__ == "__main__":
    main()
