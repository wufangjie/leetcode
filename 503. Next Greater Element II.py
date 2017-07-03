class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        no_next, theNext = [], [-1] * len(nums)
        for i, elem in enumerate(nums):
            while no_next:
                if elem > nums[no_next[-1]]:
                    theNext[no_next.pop()] = elem
                else:
                    break
            no_next.append(i)
        for i, elem in enumerate(nums):
            while no_next:
                if elem > nums[no_next[-1]]:
                    theNext[no_next.pop()] = elem
                else:
                    break
            else:
                break
        return theNext


        # TLE
        # no_next, theNext = set(), [-1] * len(nums)
        # for i, elem in enumerate(nums):
        #     remove = set()
        #     for k in no_next:
        #         if elem > nums[k]:
        #             theNext[k] = elem
        #             remove.add(k)
        #     no_next.add(i)
        #     no_next.difference_update(remove)
        # for i, elem in enumerate(nums):
        #     if not no_next:
        #         break
        #     remove = set()
        #     for k in no_next:
        #         if elem > nums[k]:
        #             theNext[k] = elem
        #             remove.add(k)
        #     no_next.difference_update(remove)
        # return theNext

# with duplicate
Solution().nextGreaterElements([100,1,11,1,120,111,123,1,-1,-100])
