#!/usr/bin/env python
# Author: @darkdefender27 :: Link: https://tinyurl.com/y8oxy4km
# Below solution is an O(n^2) solution.
# O(nlog(n)) solution - Link: https://tinyurl.com/k8nrwtd


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        inc_list = [0 for i in xrange(len(A))]

        for i in xrange(len(A)):
            max_till_now = 0
            for ii in xrange(i):
                if A[ii] < A[i]:
                    if inc_list[ii] > max_till_now:
                        max_till_now = inc_list[ii]
            inc_list[i] = 1 + max_till_now

        max_length = 0
        for j in xrange(len(inc_list)):
            if inc_list[j] > max_length:
                max_length = inc_list[j]

        return max_length
