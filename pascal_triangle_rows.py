#!/usr/bin/env python

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        res = []
        prev = [1]
        
        for i in xrange(A):
            curr = []
            for ii in xrange(i+1):
                if(ii==0):
                    curr.append(prev[ii])
                elif(ii==len(prev)):
                    curr.append(prev[ii-1])
                else:
                    curr.append(prev[ii] + prev[ii-1])
            res.append(curr)
            prev = curr
            
        return res