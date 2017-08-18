class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):

        if len(A) <= 1:
            return 0

        minima, max_profit = A[0], 0
        for i in xrange(1, len(A)):
            if A[i] < minima:
                minima = A[i]
            if max_profit < (A[i]-minima):
                max_profit = A[i]-minima

        return max_profit
