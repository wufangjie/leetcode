'''
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
A solution set is:

[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
'''

def comb_sum_rec2(candidates, target, result=[]):
    if target == 0:
        return [result]
    elif candidates == [] or candidates[0] > target:
        return []
    else:
        temp = comb_sum_rec2(
            candidates[1:], target - candidates[0], result + candidates[:1])
        i = 0
        for i, val in enumerate(candidates[1:], 1):
            if val != candidates[0]:
                break
        else:
            i += 1
        return temp + comb_sum_rec2(candidates[i:], target, result)


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return comb_sum_rec2(sorted(candidates), target)



if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
