
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        

h11 = ListNode(15)
h12 = ListNode(22)
h13 = ListNode(35)

h21 = ListNode(1)
h22 = ListNode(6)
h23 = ListNode(12)
h24 = ListNode(40)
h25 = ListNode(46)

h31 = ListNode(3)
h32 = ListNode(8)
h33 = ListNode(16)
h34 = ListNode(33)

h11.next = h12
h12.next = h13

h21.next = h22
h22.next = h23
h23.next = h24
h24.next = h25

h31.next = h32
h32.next = h33
h33.next = h34

heads = [h11,h21,h31]
s = Solution()
finalHead = s.mergeKLists(heads)

tmp = finalHead
while tmp is not None:
    print tmp.val
    tmp = tmp.next

