# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 破题目, 意思都说不明白, 不是把倒数第二个元素删除, 而是把当前的结点删除, 想骂人

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        # if not node or not node.next:
        #     pass
        # elif not node.next.next:
        #     node.val = node.next.val
        #     node.next = None
        # else:
        #     while node.next.next.next:
        #         node = node.next
        #     node.next = node.next.next
