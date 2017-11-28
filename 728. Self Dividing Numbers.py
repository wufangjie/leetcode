class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for num in range(left, right + 1):
            poss = set(str(num))
            if '0' not in poss:
                poss.discard('1')
                for p in poss:
                    if num % int(p) != 0:
                        break
                else:
                    ret.append(num)
        return ret


print(Solution().selfDividingNumbers(1, 22))
