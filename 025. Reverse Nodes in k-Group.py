'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or head is None:
            return head

        root = pb = ListNode('root')
        pb.next = head
        while True:
            p = pb.next
            for i in range(k - 1):
                if p is None:
                    break
                p = p.next
            if p is None:
                break

            pl = pre = pb.next
            pr = pl.next
            for _ in range(k - 1):
                p = pr
                pr = p.next
                p.next = pre
                pre = p
            pl.next = pr
            pb.next = p
            pb = pl
        return root.next


    def reverseKGroup_include_last_block(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1 or head is None:
            return head

        root = pb = ListNode('root')   # pointer to block
        pb.next = head
        while True:
            pl = pre = pb.next         # left most pointer in block, pre node
            pr = pl.next               # right most pointer every step
            for _ in range(k - 1):
                p = pr
                if p is None:
                    break
                pr = p.next
                p.next = pre
                pre = p
            pl.next = pr               # link pl to None or next block
            pb.next = p if p else pre  # link previous block and this block
            if pr is None:
                break                  # reach end
            pb = pl                    # move to next block
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

    a = Node(2, Node(4, Node(6, Node(5, Node(7, Node(4, Node(1, Node(8))))))))
    result = Solution().reverseKGroup(a, 4)

    for p in result:
        print(p.val)
