class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST(object):
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

    def delete(self,num):
        pass

    def search(self,num):
        pass

    def printTree(self):
        self.printTreeHelper(self.root)

    def printTreeHelper(self,node):
        if node == None:
            return
        self.printTreeHelper(node.left)
        print node.val
        self.printTreeHelper(node.right)

tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(8)
tree.insert(1)
tree.insert(15)
tree.insert(12)

tree.printTree()