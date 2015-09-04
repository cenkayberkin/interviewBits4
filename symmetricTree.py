
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 1
        else:
            return self.traverseTree(root.left,root.right)

    def traverseTree(self,root1,root2):
        if root1 == None and root2 == None:
            return 1
        elif root1 != None and root2 == None:
            return 0
        elif root1 == None and root2 != None:
            return 0


        if root1.val != root2.val:
            return 0

        if self.traverseTree(root1.left,root2.right) and self.traverseTree(root1.right,root2.left):
            return 1
        else:
            return 0


t1 = TreeNode(1)
t21 = TreeNode(2)
t22 = TreeNode(2)
t31 = TreeNode(3)
t32 = TreeNode(3)
t41 = TreeNode(4)
t42 = TreeNode(4)

t1.left = t21
t1.right = t22

t21.left = t31
t21.right = t41

t22.left = t42
t22.right = t32

s = Solution()
print s.isSymmetric(t1)