class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        left = [TreeNode(nums[0])]
        for elem in nums[1:]:
            temp = None
            while left and elem > left[-1].val:
                temp = left.pop()
            node = TreeNode(elem)
            if left:
                left[-1].right = node
            left.append(node)
            if temp:
                node.left = temp
        return left[0]


# brute force recursive seems like faster
