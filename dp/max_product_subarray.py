#!/usr/bin/env python
# Author: @darkdefender27
# Link: https://www.interviewbit.com/problems/max-product-subarray/


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):

        max_p, l_max, l_min = 0, 1, 1

        for i in xrange(len(A)):
            if A[i] < 0:
                l_min = l_min * A[i]
                if l_min > 0:
                    l_max = l_min
                    l_min = A[i]
                    if l_max > max_p:
                        max_p = l_max
            elif A[i] > 0:
                l_max = l_max * A[i]
                l_min = l_min * A[i]
                if l_max > max_p:
                    max_p = l_max
            else:
                l_max, l_min = 1, 1

        return max_p
