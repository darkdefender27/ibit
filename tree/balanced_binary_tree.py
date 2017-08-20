# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        return 1 if self.treeDepth(A)>0 else 0

    def treeDepth(self, A):

        if A is None:
            return 0

        l_depth = self.treeDepth(A.left)
        r_depth = self.treeDepth(A.right)

        if l_depth == -1 or r_depth == -1:
            return -1
        else:
            return 1+max(l_depth, r_depth) if abs(l_depth-r_depth)<=1 else -1
