
# Definition for a binary tree node.
class TreeNode:
        a=5#test
        def __init__(self, x,left,right):
                self.val = x
                self.left = left
                self.right = right

        def maxDepth(self, root):
                """
                :type root: TreeNode
                :rtype: int
                """
                if not root:
                    return 0
                left = self.maxDepth(root.left)+1
                right = self.maxDepth(root.right)+1

                return max(left, right)

if __name__=="__main__":
        t4 = TreeNode(4, None, None)
        t2 = TreeNode(2, None, None)
        t3 = TreeNode(3, t4, None)
        t1=TreeNode(1,t2,t3)
        print(t1.maxDepth(t1))




