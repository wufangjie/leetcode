'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.
'''


from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = defaultdict(list)
        for elem in strs:
            #result[''.join(sorted(elem))].append(elem)  # 1.5 times
            result[tuple(sorted(elem))].append(elem)
        return [elem for elem in result.values()]

if __name__ == '__main__':
    Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
