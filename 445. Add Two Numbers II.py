# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lst1, lst2 = [], []
        while l1:
            lst1.append(l1.val)
            l1 = l1.next
        while l2:
            lst2.append(l2.val)
            l2 = l2.next

        pre, head = 0, None
        while lst1 or lst2 or pre:
            v = (lst1.pop() if lst1 else 0) + (lst2.pop() if lst2 else 0) + pre
            pre = 1 if v > 9 else 0
            temp = ListNode(v % 10)
            temp.next = head
            head = temp
        return head
