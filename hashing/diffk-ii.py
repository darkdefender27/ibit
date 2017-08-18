#!/usr/bin/env python
# Author @darkdefender27
# Link: https://www.interviewbit.com/problems/diffk-ii/


class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        my_dict = {}

        for i in xrange(len(A)):
            if A[i] not in my_dict:
                my_dict[A[i]] = 1
            else:
                my_dict[A[i]] += 1

        found = False
        for i in xrange(len(A)):
            candidate = A[i]+B
            if candidate in my_dict:
                if B > 0:
                    found = True
                    break
                else:
                    if my_dict[candidate] > 1:
                        found = True
                        break


        return 1 if found else 0
