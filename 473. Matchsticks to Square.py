class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        theSum = sum(nums)
        if theSum % 4 != 0:
            return False

        edge = theSum // 4
        nums.sort(reverse=True)
        def dfs(i, current_sum, current, nums):
            if current_sum == edge:
                if sum(nums) == 2 * edge:
                    return True
                else:
                    ii = jj = 0
                    left = []
                    while ii < len(current):
                        if current[ii] == nums[jj]:
                            ii += 1
                        else:
                            left.append(nums[jj])
                        jj += 1
                    left += nums[jj:]
                    return dfs(1, left[0], left[:1], left)
            elif current_sum > edge:
                return False

            if i >= len(nums):
                return False
            return (dfs(i+1, current_sum+nums[i], current+nums[i:i+1], nums)
                    or dfs(i+1, current_sum, current, nums))
        return dfs(1, nums[0], nums[:1], nums)



assert Solution().makesquare([1,1,2,2,2])
assert not Solution().makesquare([3,3,3,3,4])
