# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from utils import ListNode


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        even = even_head = head.next

        while even:
            if even.next is None:
                break
            odd.next = even.next
            odd = even.next

            even.next = odd.next
            even = odd.next
        odd.next = even_head
        return head


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
#head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
#head = ListNode(1)
head = Solution().oddEvenList(head)

p = head
while p:
    print(p)
    p = p.next
