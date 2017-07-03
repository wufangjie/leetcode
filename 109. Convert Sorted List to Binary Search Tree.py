'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def build_rec(lo, hi):
            if hi < lo:
                return None
            mid = (lo + hi) >> 1
            node = TreeNode(nums[mid])
            node.left = build_rec(lo, mid - 1)
            node.right = build_rec(mid + 1, hi)
            return node

        return build_rec(0, len(nums) - 1)
