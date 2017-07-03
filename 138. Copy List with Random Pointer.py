# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

#### because label may not be unique?
# and A linked list is given such that each node contains an additional random pointer which could point to **any node in the list** or null.

from collections import defaultdict


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head

        node_dict = defaultdict(lambda : RandomListNode(0))
        node_dict[None] = None
        node = head
        while node:
            node_dict[node].label = node.label
            node_dict[node].next = node_dict[node.next]
            node_dict[node].random = node_dict[node.random]
            node = node.next
        return node_dict[head]
        # node_dict = {head.label: RandomListNode(head.label)}
        # Q = [head]
        # while Q:
        #     current = Q.pop()
        #     for attr in ('next', 'random'):
        #         nd = current.__getattribute__(attr)
        #         if nd is not None:
        #             if nd.label not in node_dict:
        #                 node_dict[nd.label] = RandomListNode(nd.label)
        #                 Q.append(nd)
        #             node_dict[nd.label].__setattr__(attr, node_dict[nd.label])
        # return node_dict[head.label]


a = RandomListNode(-1)
b = RandomListNode(-1)

class Test:
    def __init__(self, a=1):
        self.a = 1
