class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        if m == 1:
            return sum(nums)

        n = len(nums)
        cumsum = nums[:] # nums.copy() python2's list no copy
        for i in range(n - 2, -1, -1):
            cumsum[i] += cumsum[i + 1]
        best = [min(max(max(nums[:m-1]), cumsum[m-1]),
                    max(max(nums[-m+1:]), sum(nums[:-m+1])))]

        def dfs(i, k, current_max, best):
            if n - i <= k:
                best[0] = min(current_max, best[0])
            if current_max < best[0]:
                if k == 1:
                    current_max = max(current_max, cumsum[i])
                    if current_max < best[0]:
                        best[0] = current_max
                else:
                    acc = nums[i]
                    for j in range(i + 1, n):
                        if acc + nums[j] < current_max:
                            acc += nums[j]
                            j += 1
                        else:
                            break

                    dfs(j, k - 1, max(current_max, acc), best)
                    for j in range(j, n - k + 1):
                        acc += nums[j]
                        if acc < best[0]:
                            dfs(j + 1, k - 1, acc, best)
                        else:
                            break

        dfs(0, m, max(max(nums), cumsum[0] // m), best)
        return best[0]


print(Solution().splitArray([7,2,5,10,8], 2))
