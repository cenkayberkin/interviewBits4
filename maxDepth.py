# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left,right)


t1 = TreeNode(10)
t2 = TreeNode(5)
t3= TreeNode(15)
t1.left = t2
t1.right = t3

t21 = TreeNode(3)
t22 = TreeNode(8)
t2.left = t21
t2.right = t22
t21.left = TreeNode(1)
s = Solution()
print s.maxDepth(t1)