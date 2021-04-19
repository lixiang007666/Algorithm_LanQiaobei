# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        def dfs(left,right):
            if (left == None and right == None):
                return True
            if (left == None or right == None):
                return False
            if left.val!=right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
        return dfs(root.left,root.right)


