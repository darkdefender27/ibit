#!/usr/bin/env python
# Author: @darkdefender27 :: Link: https://tinyurl.com/yaufvncm
# Below solution is an O(n^2) solution.
# O(nlog(n)) solution - Link: https://tinyurl.com/k8nrwtd


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        result = 0
        inc_list = [0 for _ in xrange(len(A))]
        dec_list = [0 for _ in xrange(len(A))]

        for i in xrange(len(A)):
            max_till_now = 0
            for ii in xrange(i):
                if A[ii] < A[i]:
                    if inc_list[ii] > max_till_now:
                        max_till_now = inc_list[ii]

            inc_list[i] = 1 + max_till_now

        for j in xrange(len(A)-1, -1, -1):
            max_till_now = 0
            for jj in xrange(len(A)-1, j-1, -1):
                if A[j] > A[jj]:
                    if dec_list[jj] > max_till_now:
                        max_till_now = dec_list[jj]

            dec_list[j] = 1 + max_till_now

        max_length = 0
        for k in xrange(len(A)):
            inc_list[k] += dec_list[k]
            if inc_list[k] > max_length:
                max_length = inc_list[k]

        return max_length - 1 if max_length > 1 else 0
