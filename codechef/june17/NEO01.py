#!/usr/bin/env python
# Author: Shubham Utwal :: darkdefender27
# Incomplete

def main():
    T = int(raw_input().strip())

    for _ in xrange(T):
        n = int(raw_input().strip())
        a = map(int, raw_input().strip().split(' '))
        a.sort()
        happiness, sum, ct = 0, 0, 0

        for _ in xrange(len(a)-1, -1, -1):
            if(a[_] >= 0):
                sum += a[_]
                ct += 1
                happiness = sum * ct
            else:
                temp_happiness = (sum + a[_])*(ct + 1) # Included the -ve element
                if temp_happiness > happiness:
                    sum += a[_]
                    ct += 1
                    happiness = temp_happiness
                else:
                    happiness += a[_]*1

        print happiness


if __name__ == '__main__':
    main()
