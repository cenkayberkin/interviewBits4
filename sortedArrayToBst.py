# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    root = None

    def __init__(self):
        root = None

    def insert(self,num):
        if self.root == None:
            self.root = TreeNode(num)
        else:
            self.insertHelper(self.root,num)

    def insertHelper(self,node,num):
        if num < node.val:
            if node.left != None:
                self.insertHelper(node.left,num)
            else:
                node.left = TreeNode(num)
        else:
            if node.right != None:
                self.insertHelper(node.right,num)
            else:
                node.right = TreeNode(num)
    def printTree(self):
        self.printTreeHelper(self.root)

    def printTreeHelper(self,node):
        if node == None:
            return
        self.printTreeHelper(node.left)
        print node.val
        self.printTreeHelper(node.right)

    def sortedArrayToBST(self, nums):
        self.sortedArrayToBSTHelper(nums)
        return self.root
    def sortedArrayToBSTHelper(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        if length == 0:
            return
        mid = length/2
        self.insert(nums[mid])
        self.sortedArrayToBSTHelper(nums[:mid])
        self.sortedArrayToBSTHelper(nums[mid + 1:])


nums = []
s = Solution()
# s.insertNode(10)
# s.insertNode(5)
# s.insertNode(8)
# s.insertNode(1)
# s.insertNode(15)
# s.insertNode(12)
# s.insertNode(20)
s.sortedArrayToBST(nums)
s.printTree()