'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        theBest = pre_length = 0
        for i, elem in enumerate(s):
            try:
                j = s.index(elem, i - pre_length, i)
                theBest = max(theBest, pre_length)
                pre_length = i - j
            except:
                pre_length += 1
        return max(theBest, pre_length)


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
    assert Solution().lengthOfLongestSubstring('') == 0
    assert Solution().lengthOfLongestSubstring('pwwkewabcd') == 7
    assert Solution().lengthOfLongestSubstring('b') == 1
