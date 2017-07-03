'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
'''

# the answer with stack is more elegant

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        flag = [False] * len(s)
        for i, elem in enumerate(s):
            if elem == ')':
                for j in range(i - 1, -1, -1):
                    if not flag[j]:
                        if s[j] == '(':
                            flag[j] = True
                            flag[i] = True
                        break
        longest = i = 0
        while True:
            try:
                while not flag[i]:
                    i += 1
                j = i
                while flag[i]:
                    i += 1
            except IndexError:
                break
            longest = max(longest, i - j)
        if flag[-1]:
            longest = max(longest, i - j)
        return longest


if __name__ == '__main__':
    assert Solution().longestValidParentheses(')(()()())') == 8
    assert Solution().longestValidParentheses('(()()())(') == 8
    assert Solution().longestValidParentheses('') == 0
