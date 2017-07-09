class Solution:
    # @param A : tuple of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        result = []
        dir = 0
        m = len(A)
        n = len(A[0])
        t, b, l, r = 0, m-1, 0, n-1

        while(t<=b and l<=r):
            if(dir == 0):
                for i in xrange(l, r+1, 1):
                    result.append(A[t][i])
                dir = 1
                t = t + 1
            elif(dir == 1):
                for i in xrange(t, b+1, 1):
                    result.append(A[i][r])
                dir = 2
                r = r - 1
            elif(dir == 2):
                for i in xrange(r, l-1, -1):
                    result.append(A[b][i])
                dir = 3
                b = b - 1
            elif(dir == 3):
                for i in xrange(b, t-1, -1):
                    result.append(A[i][l])
                dir = 0
                l = l + 1

        return result
