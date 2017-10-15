from utils import memo


class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 1:
            return True

        total = sum(nums)
        if total % k:
            return False

        theMean = total // k
        nums.sort()
        if nums[-1] > theMean:
            return False
        while nums and nums[-1] == theMean:
            k -= 1
            nums.pop()

        n = len(nums)
        nums.reverse()

        def find_company(current, left, result):
            if current[0] == theMean:
                result.add(tuple(current[1:]))
            elif left and (current[0] < theMean):
                left2 = left[1:]
                find_company(current, left2, result)
                temp = current[:]
                temp[0] += left[0]
                temp.append(left[0])
                find_company(temp, left2, result)

        @memo
        def dfs(k, *nums):
            if k == 1:
                return True
            k -= 1
            result = set()
            left = nums[1:]
            find_company([nums[0]], left, result)
            for comb in result:
                left2 = []
                i = j = 0
                while i < len(comb):
                    if left[j] != comb[i]:
                        left2.append(left[j])
                    else:
                        i += 1
                    j += 1
                left2.extend(left[j:])
                if dfs(k, *left2):
                    return True
            return False

        return dfs(k, *nums)


        # # TLE 85 / 139
        # if k == 1:
        #     return True

        # total = sum(nums)
        # if total % k:
        #     return False

        # theMean = total // k
        # nums.sort()
        # if nums[-1] > theMean:
        #     return False
        # while nums and nums[-1] == theMean:
        #     k -= 1
        #     nums.pop()

        # n = len(nums)
        # nums.reverse()

        # @memo
        # def dfs(i, *each_left):
        #     if i == n:
        #         return True
        #     for j, left in enumerate(each_left):
        #         if left >= nums[i]:
        #             temp = list(each_left)
        #             temp[j] -= nums[i]
        #             if dfs(i + 1, *temp):
        #                 return True
        #     return False

        # return dfs(0, *([theMean] * k))


#NOTE: my way is slow when there are many repeat nums
print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))
print(Solution().canPartitionKSubsets([7628,3147,7137,2578,7742,2746,4264,7704,9532,9679,8963,3223,2133,7792,5911,3979], 6))
