import bisect


class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        odd = k & 1
        mid = (k - 1) >> 1
        window = sorted(nums[:k])
        n = len(nums) - k + 1
        result = [0.] * n
        result[0] += window[mid] if odd else sum(window[mid:mid+2]) / 2.
        for i in range(n - 1):
            if nums[i] > nums[i + k]:
                j = bisect.bisect_left(window, nums[i])
                l = bisect.bisect_right(window, nums[i + k], hi=j+1)
                if j != l:
                    window[l+1:j+1] = window[l:j]
                window[l] = nums[i + k]
            elif nums[i] < nums[i + k]:
                j = bisect.bisect_right(window, nums[i]) - 1
                l = bisect.bisect_left(window, nums[i + k], lo=j+1)
                if j < l - 1:
                    window[j:l-1] = window[j+1:l]
                window[l-1] = nums[i + k]
            result[i+1] += window[mid] if odd else sum(window[mid:mid+2]) / 2.
        return result


# float required
print(Solution().medianSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(Solution().medianSlidingWindow([1,4,2,3], 4))
