# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while head:
            if head.val != val:
                pre.next = head
                pre = head
            head = head.next
        pre.next = None
        return dummy.next


root = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(4, ListNode(5))))))
Solution().removeElements(root, 2)
