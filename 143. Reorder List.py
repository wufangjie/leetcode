# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        node_dict = {}
        count = -1
        node = head

        while node is not None:
            count += 1
            node_dict[count] = node
            node = node.next

        seq = []
        mid = (count + 1) >> 1
        for i in range(mid):
            seq.append(i)
            seq.append(count - i)
        if mid << 1 == count:
            seq.append(mid)

        node_dict[seq[-1]].next = None
        for i in range(count-1, -1, -1):
            node_dict[seq[i]].next = node_dict[seq[i+1]]


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))#, ListNode(5)))))

Solution().reorderList(head)
