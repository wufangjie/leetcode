'''
Write a function to find the longest common prefix string amongst an array of strings.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''

        i = 0
        for i, all_in_one in enumerate(zip(*strs), 1):
            for elem in all_in_one[1:]:
                if elem != all_in_one[0]:
                    break
            else:
                continue
            return strs[0][:i - 1]
        return strs[0][:i]


if __name__ == '__main__':
    assert Solution().longestCommonPrefix([]) == ''
    assert Solution().longestCommonPrefix(['', 'abc']) == ''
    assert Solution().longestCommonPrefix(['ab', '']) == ''
    assert Solution().longestCommonPrefix(['ababc', 'abcd']) == 'ab'
    assert Solution().longestCommonPrefix(['abcd', 'abcd']) == 'abcd'
    assert Solution().longestCommonPrefix(["abab","aba",""])
