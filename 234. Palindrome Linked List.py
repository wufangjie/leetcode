# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# break the structure
from utils import ListNode


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True

        tail = head
        count = 1
        while tail.next:
            count += 1
            tail = tail.next

        if count == 1:
            return True
        elif count == 2:
            return head.val == head.next.val

        node = head
        for _ in range((count - 1) >> 1):
            node = node.next

        if count & 1:
            pre = node
            node = node.next
            pre.next = None
        else:
            pre = node.next
            node = pre.next
            pre.next = None

        while node:
            next = node.next
            node.next = pre
            pre, node = node, next

        while tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        return True



# print(Solution().isPalindrome(ListNode(1, ListNode(1, ListNode(2, ListNode(1))))))

print(Solution().isPalindrome(ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))))
# print(Solution().isPalindrome(ListNode(0, ListNode(2))))
# print(Solution().isPalindrome(ListNode(0)))
