#!/usr/bin/env python3

n = int(input().strip())
arr = [int(x) for x in input().strip().split()]
res = 0

# i,j,k,l such that i<=j<k<=l
for i in range(0, n-1):
    max_ij = arr[i]
    for j in range(i, n-1):
        if arr[j]>max_ij:
            max_ij = arr[j]
        for k in range(j+1, n):
            min_kl = arr[k]
            for l in range(k, n):
                if arr[l]<min_kl:
                    min_kl = arr[l]
                res += (max_ij * min_kl)

res = res % ((10**9) + 7)
print res
