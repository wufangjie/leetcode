from itertools import product


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = count = 0
        for elem in s:
            if elem == '(':
                left += 1
            elif elem == ')':
                if left > 0:
                    count += 1
                    left -= 1

        if not count:
            return ''.join(c for c in s if c not in {'(', ')'})

        n = len(s)

        def check(s, left):
            for elem in s:
                if elem == '(':
                    left += 1
                elif elem == ')':
                    if left > 0:
                        left -= 1
                    else:
                        return False
            return True

        def dfs(result, i, left, l, r):

            # import pdb
            # pdb.set_trace()

            if l == r == 0:
                if check(s[i:], left):
                    return {r + s[i:] for r in result}
                else:
                    return set()
            if i == n:
                return set()

            results = set()
            if s[i] == ')' and r > 0:
                results.update(dfs(result, i+1, left, l, r-1))
            elif s[i] == '(' and l > 0:
                results.update(dfs(result, i+1, left, l-1, r))

            if s[i] == ')':
                if left > 0:
                    result = {r + ')' for r in result}
                    results.update(dfs(result, i+1, left-1, l, r))
            else:
                result = {r + s[i] for r in result}
                results.update(dfs(result, i+1, left+(s[i]=='('), l, r))
            return results

        count_left, count_right = s.count('('), s.count(')')
        return list(dfs({''}, 0, 0, count_left-count, count_right-count))





assert sorted(Solution().removeInvalidParentheses(")()(")) == ['()']
assert sorted(Solution().removeInvalidParentheses("()())())")) == sorted(["()()()","()(())","(())()","(()())"])
assert sorted(Solution().removeInvalidParentheses("(a()()")) == sorted(["(a())","(a)()","a()()"])
