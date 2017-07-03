'''
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p = root = ListNode('root')
        root.next = head
        count = 1
        while count < m:
            count += 1
            p = p.next

        pre, left = p.next, p
        p = pre.next
        while count < n:
            count += 1
            temp = p.next
            p.next = pre
            pre = p
            p = temp
        left.next.next = p
        left.next = pre

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

    a = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7)))))))
    result = Solution().reverseBetween(a, 7, 7)
    for p in result:
        print(p.val)
