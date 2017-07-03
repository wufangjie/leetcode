class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        no_next, theNext = set(), {}
        for elem in nums:
            remove = set()
            for k in no_next:
                if elem > k:
                    theNext[k] = elem
                    remove.add(k)
            no_next.add(elem)
            no_next.difference_update(remove)
        return [theNext.get(n, -1) for n in findNums]
