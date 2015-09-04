class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if root == None:
            return []
        queue = [root]

        while len(queue) > 0:
            current = queue.pop(0)
            if current.val != -1:
                result.append(current.val)
                if current.left != None:
                    queue.append(current.left)
                if current.left == None:
                    queue.append(TreeNode(-1))
                if current.right != None:
                    queue.append(current.right)
                if current.right == None:
                    queue.append(TreeNode(-1))
            else:
                result.append(-1)
        return result

t1 = TreeNode(1)
t2 = TreeNode(2)
t3 = TreeNode(3)
t4 = TreeNode(4)
t5 = TreeNode(5)
t1.right = t3
t1.left = t2

t3.left = t4
t4.right = t5
# {1 2 3 -1 -1 4 -1 -1 5 -1 -1}

s = Solution()
print s.preorderTraversal(t1)