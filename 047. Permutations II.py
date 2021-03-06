def permute_rec(nums):
    if nums:
        pre = None
        for i, elem in enumerate(nums):
            if elem != pre:
                pre = elem
                for p in permute_rec(nums[:i] + nums[i+1:]):
                    p.append(elem)
                    yield p
                    # yield [elem] + p  # about twice times
    else:
        yield []


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(permute_rec(sorted(nums)))


if __name__ == '__main__':
    assert Solution().permuteUnique([1, 1, 2]) == [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
