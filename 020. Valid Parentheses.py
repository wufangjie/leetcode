'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        close_dict = {')': '(', ']': '[', '}': '{'}
        for elem in s:
            if elem in {'(', '[', '{'}:
                stack.append(elem)
            else:
                try:
                    if close_dict[elem] != stack.pop():
                        raise Exception('invalid')
                except Exception:
                    return False
        return True if stack == [] else False


if __name__ == '__main__':
    assert Solution().isValid('[{}]')
