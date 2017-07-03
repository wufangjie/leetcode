'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p_unique = root = ListNode('root')
        p_pre = p_cur = head
        count = 1
        pre_val = None
        while p_cur:
            if p_cur.val != pre_val:
                if count == 0:
                    p_unique.next = p_pre
                    p_unique = p_pre
                count = 0
                p_pre, p_cur = p_cur, p_cur.next
                pre_val = p_pre.val
            else:
                count += 1
                p_cur = p_cur.next
        if count == 0:
            p_unique.next = p_pre
            p_unique = p_pre
        p_unique.next = None
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

    node = Node(1, Node(1, Node(3, Node(4, Node(4, Node(5))))))
    node = Node(1, Node(1))
    for p in Solution().deleteDuplicates(node):
        print(p.val)
