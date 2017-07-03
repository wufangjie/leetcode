# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from 000 import ListNode

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = dummy = ListNode(float('-inf'))
        while head:
            if p.val > head.val:
                p = dummy
            while p.next and p.next.val < head.val:
                p = p.next
            head.next, head, p.next = p.next, head.next, head
        return dummy.next



#head = ListNode(3, ListNode(1, ListNode(2, ListNode(0))))
node = head = ListNode(0)
for i in range(1, 5000):
    node.next = ListNode(i)
    node = node.next

head2 = Solution().insertionSortList(head)

head2 = head
while head2:
    print(head2)
    head2 = head2.next
