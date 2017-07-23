#!/usr/bin/env python

def main():
    x, y = map(int, raw_input().strip().split(' '))
    i, j, count = 1, 0, 0

    while(i <= y):
        j = i + 1
        while(((i+j)*(j-i)) <= y):
            comp = (i+j)*(j-i)
            if(comp <= y and comp >= 1):
                count += 1
            j += 1
        i += 1

    print count

if __name__ == '__main__':
    main()
