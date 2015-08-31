
class CacheNode(object):
    key = 0
    value = 0
    Prev = None
    Next = None
    def __init__(self,key,value):
        self.key = key
        self.value = value

class LRUCache(object):
    capacity = 0
    dict = None
    head = None
    tail = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}


    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.dict:
            return -1

        node = self.dict[key]
        self.moveToTop(node)
        return node.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.moveToTop(node)

        else:
            if len(self.dict) < self.capacity:
                newNode = self.insertToTop(key,value)
                self.dict[key] = newNode

            else:
                newNode = self.insertToTop(key,value)
                self.dict[key] = newNode
                self.removeLast()

    def removeLast(self):

        key = self.tail.key
        del self.dict[key]

        prev =  self.tail.Prev
        self.tail.Prev = None
        self.tail = prev
        self.tail.Next = None

    def insertToTop(self,key,value):
        if self.head == None:
            self.head = CacheNode(key,value)
            self.tail = self.head
        else:
            tmp = CacheNode(key,value)
            tmp.Next = self.head
            self.head.Prev = tmp
            self.head = tmp
        return self.head

    def moveToTop(self,node):
        if self.head == node:
            return

        lastNode = False

        if self.tail == node:
            prevNode = node.Prev
            node.Prev = None
            prevNode.Next = None
            self.tail = prevNode
        else:
            prevNode = node.Prev
            nextNode = node.Next
            prevNode.Next = nextNode

            if nextNode != None:
                nextNode.Prev = prevNode

        node.Next = self.head
        self.head.Prev = node
        node.Prev = None
        self.head = node


s = LRUCache(10)

s.set(10,13)
s.set(3,17)
s.set(6,11)
s.set(10,5)
s.set(9,10)
s.get(13)
s.set(2,19)
s.get(2)
s.get(3)
s.set(5,25)
s.get(8)
s.set(9,22)
s.set(5,5)
s.set(1,30)
s.get(11)
s.set(9,12)
s.get(7)
s.get(5)
s.get(8)
s.get(9)
s.set(4,30)
s.set(9,3)
s.get(9)
s.get(10)
s.get(10)
s.set(6,14)
s.set(3,1)
s.get(3)
s.set(10,11)
s.get(8)
s.set(2,14)
s.get(1)
s.get(5)
s.get(4)
s.set(11,4)
s.set(12,24)
s.set(5,18)
s.get(13)
s.set(7,23)
s.get(8)
s.get(12)
s.set(3,27)
s.set(2,12)
s.get(5)
s.set(2,9)
s.set(13,4)
s.set(8,18)
s.set(1,7)
s.get(6)
s.set(9,29)
s.set(8,21)
s.get(5)
s.set(6,30)
s.set(1,12)
s.get(10)
s.set(4,15)
s.set(7,22)
s.set(11,26)
s.set(8,17)
s.set(9,29)
s.get(5)
s.set(3,4)
s.set(11,30)
s.get(12)
s.set(4,29)
s.get(3)
s.get(9)
s.get(6)
s.set(3,4)
s.get(1)
s.get(10)
s.set(3,29)
s.set(10,28)
s.set(1,20)
s.set(11,13)
s.get(3)
s.set(3,12)
s.set(3,8)
s.set(10,9)
s.set(3,26)
s.get(8)
s.get(7)
s.get(5)
s.set(13,17)
s.set(2,27)
s.set(11,15)
s.get(12)
s.set(9,19)
s.set(2,15)
s.set(3,16)
s.get(1)
s.set(12,17)
s.set(9,1)
s.set(6,19)
s.get(4)
s.get(5)
s.get(5)
s.set(8,1)
s.set(11,7)
s.set(5,2)
s.set(9,28)
s.get(1)
s.set(2,2)
s.set(7,4)
s.set(4,22)
s.set(7,24)
s.set(9,26)
s.set(13,28)
s.set(11,26)

