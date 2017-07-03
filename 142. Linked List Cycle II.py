# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            slow = head
            fast = head.next
            while slow != fast:
                slow = slow.next
                fast = fast.next.next
        except AttributeError:
            return None

        slow = slow.next
        while head != slow:
            slow = slow.next
            head = head.next
        return head

# 按走的步数列一个方程, 通过走相同的步数使另一个走到目标位置
