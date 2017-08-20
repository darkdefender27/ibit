# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):

        if A is None:
            return None

        l_depth, r_depth = None, None
        if A.left is not None:
            l_depth = self.minDepth(A.left)
        if A.right is not None:
            r_depth = self.minDepth(A.right)

        if l_depth is not None and r_depth is not None:
            return (1+l_depth) if l_depth < r_depth else (1+r_depth)
        elif l_depth is not None:
            return (1+l_depth)
        elif r_depth is not None:
            return (1+r_depth)
        else:
            return 1
