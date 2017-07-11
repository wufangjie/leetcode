class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        left, right = equation.split('=')
        a1, b1 = self._parse(left)
        a2, b2 = self._parse(right)
        if a1 == a2:
            if b1 == b2:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            return 'x={}'.format((b2 - b1) // (a1 - a2))

    @staticmethod
    def _parse(experession):
        ret = [0, 0]
        pre, pre_idx, add_idx, sign = 0, 0, 1, '+'
        for i, c in enumerate(experession + '+'):
            if c in ('+', '-'):
                ret[add_idx] += pre if sign == '+' else -pre
                pre, pre_idx, add_idx, sign = 0, i + 1, 1, c
            elif c == 'x':
                add_idx = 0
                if pre_idx == i:
                    pre = 1
            else:
                pre = pre * 10 + int(c)
        return ret


assert Solution().solveEquation("x+5-3+x=6+x-2") == "x=2"
assert Solution().solveEquation("x=x") == "Infinite solutions"
assert Solution().solveEquation("2x=x") == "x=0"
assert Solution().solveEquation("x=x+2") == "No solution"
assert Solution().solveEquation("2x+3x-6x=x+2") == "x=-1"
