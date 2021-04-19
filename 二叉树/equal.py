# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        # 前提条件是两个节点不同时为空 一个为空，一个非空，显然不同
        if p == None or q == None:
            return False
        # 中间发现值不相等，也不为空
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


