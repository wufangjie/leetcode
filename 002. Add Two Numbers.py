'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def _get_value(ll):
            return ll.val if ll else 0

        def _get_next(ll):
            return ll.next if ll else None

        forward = 0
        pre_node = root = ListNode('root')
        while l1 or l2:
            temp = _get_value(l1) + _get_value(l2) + forward
            new_node = ListNode(temp % 10)
            pre_node.next = new_node
            pre_node = new_node
            forward = temp // 10
            l1 = _get_next(l1)
            l2 = _get_next(l2)

        if forward:
            pre_node.next = ListNode(forward)
        return root.next


if __name__ == '__main__':
    def iter_node(node):
        while node:
            yield node
            node = node.next
    ListNode.__iter__ = iter_node

    class Node(ListNode):
        def __init__(self, x, next=None):
            self.val = x
            self.next = next

    a = Node(2, Node(4, Node(6)))
    b = Node(5, Node(6, Node(4)))
    result = Solution().addTwoNumbers(a, b)

    for x, y in zip(result, (7, 0, 1, 1)):
        assert x.val == y
