#!/usr/bin/env/python3
# Author: Shubham Utwal
# Link: http://practice.geeksforgeeks.org/problems/count-the-elements/0

def main():
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        a = list(map(int, input().strip().split(' ')))
        b = list(map(int, input().strip().split(' ')))

        # Find the MAX in Array A
        # maxy = a[0]
        # for i in a:
        #     if i>maxy:
        #         maxy = i

        # Auxiliary array of size MAX
        aux = [0]*(101)
        # Update frequency count
        for ii in b:
            aux[ii] += 1
        # Cummulative sum calculation
        j = 1
        while j<101:
            aux[j] += aux[j-1]
            j += 1

        result = []
        result.append(aux[a[0]])
        k = 1
        while k<n:
            result.append(aux[a[k]])
            k += 1

        print(','.join(str(x) for x in result))


if __name__ == '__main__':
    main()
