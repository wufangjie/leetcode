from utils import memo


class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}

        for word in words:
            node = trie
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node['#'] = '#'

        trie.pop('#', '#')

        @memo
        def find_match(string, parted=False):
            node = trie
            for i, w in enumerate(string):
                if '#' in node and find_match(string[i:], True):
                    return True
                if w not in node:
                    return False
                node = node[w]

            if parted and '#' in node:
                return True
            return False

        return [word for word in words if find_match(word)]




print(Solution().findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
