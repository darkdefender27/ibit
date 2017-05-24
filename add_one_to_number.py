#!/usr/bin/env python

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        
        for ii in xrange(len(A)):
            if(A[ii]!=0):
                A = A[ii:]
                break
        
        sum = 0
        carry = 1
        for i in xrange(len(A)-1, -1, -1):
            sum = A[i] + carry
            if sum == 10:
                carry = 1
                A[i] = 0
            else:
                carry = 0
                A[i] = sum
                break
            
        if carry == 1:
            A.insert(0, 1)
            
        return A