import re
from collections import defaultdict


reg_single = re.compile('([A-Z][a-z]*)([0-9]*)')


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        n = len(formula)
        i = 0
        stack = [defaultdict(int)]
        while i < n:
            c = formula[i]
            if 'A' <= c <= 'Z':
                elem, count = reg_single.match(formula, i).groups()
                i += len(elem) + len(count)
                count = int(count) if count else 1
                stack[-1][elem] += count
            elif c == '(':
                stack.append(defaultdict(int))
                i += 1
            elif c == ')':
                j = i + 1
                while j < n:
                    if '0' <= formula[j] <= '9':
                        j += 1
                    else:
                        break
                count = 1 if j == i + 1 else int(formula[i+1:j])
                i = j
                temp = stack.pop()
                for key, val in temp.items():
                    stack[-1][key] += val * count
        return ''.join(sorted([key if val == 1 else key + str(val)
                               for key, val in stack[0].items()]))


print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
