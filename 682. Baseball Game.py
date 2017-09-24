class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        result = []
        for c in ops:
            if c == '+':
                result.append(result[-2] + result[-1])
            elif c == 'D':
                result.append(result[-1] * 2)
            elif c == 'C':
                result.pop()
            else:
                result.append(int(c))
        return sum(result)


print(Solution().calPoints(["5","-2","4","C","D","9","+","+"]), 27)
