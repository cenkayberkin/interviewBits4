
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        levelNum = 1
        queue = [root]
        currentCount = 1
        nextCount = 0
        while len(queue) > 0:
            current = queue.pop(0)
            # print current.val
            if current.left == None and current.right == None:
                return levelNum

            if current.left != None:
                queue.append(current.left)
                nextCount += 1
            if current.right != None:
                queue.append(current.right)
                nextCount += 1
            currentCount -= 1
            if currentCount == 0:
                levelNum += 1
                # print "level",levelNum
                currentCount = nextCount
                nextCount = 0

t1 = TreeNode(10)
t2 = TreeNode(5)
t1.left = t2

t21 = TreeNode(3)
t22 = TreeNode(8)
t2.left = t21
t2.right = t22

s = Solution()
print s.minDepth(t1)
