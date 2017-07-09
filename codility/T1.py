#!/usr/bin/env python
import math

def solution(N):
    len_short_seq, i = 1, 1
    k = int(math.ceil(N/2.0))

    if N%2 == 0: # For EVEN N
        while(i*2 <= k):
            i = i*2
            len_short_seq += 1
        while(i+1 <= k):
            i += 1
            len_short_seq += 1
        if(i == k):
            len_short_seq += 1
    else: # For ODD N
        while(i*2 <= N):
            i = i*2
            len_short_seq += 1
        while(i+1 <= N):
            i += 1
            len_short_seq += 1

    return len_short_seq


def main():
    T = int(raw_input().strip())
    for _ in xrange(T):
        N = int(raw_input().strip())
        print solution(N)


if __name__ == '__main__':
    main()
