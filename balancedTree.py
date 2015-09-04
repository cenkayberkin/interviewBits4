__author__ = 'cenk'

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 1
        if abs(self.maxDepth(root.left) - self.maxDepth(root.right)) > 1:
            return 0

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def maxDepth(self, root):
        if root == None:
            return 0

        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return max(left,right)


