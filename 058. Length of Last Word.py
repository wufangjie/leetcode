'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
'''

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for elem in s[::-1]:
            if elem == ' ':
                if count != 0:
                    break
            else:
                count += 1
        return count


if __name__ == '__main__':
    assert Solution().lengthOfLastWord('a ') == 1
    assert Solution().lengthOfLastWord('hello world') == 5
