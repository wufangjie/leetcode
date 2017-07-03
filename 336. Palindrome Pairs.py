class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        trie = {}
        for i, word in enumerate(words):
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = i

        def dfs(node, pre):
            for c in node:
                if c == '#':
                    if pre == pre[::-1]:
                        yield node['#']
                else:
                    # yield from dfs(node[c], pre + c) python2 not support
                    for j in dfs(node[c], pre + c):
                        yield j

        result = []
        for i, word in enumerate(words):
            rev = word[::-1]
            n = len(word)
            node = trie
            for j, c in enumerate(rev):
                if '#' in node:
                    mid = (n - j) >> 1
                    if rev[j:j+mid] == word[:mid]:
                        result.append([node['#'], i])
                if c not in node:
                    break
                node = node[c]
            else:
                for j in dfs(node, ''):
                    if i != j:
                        result.append([j, i])

        return result



assert sorted(Solution().palindromePairs(["bat", "tab", "cat"])) == [[0, 1], [1, 0]]
assert sorted(Solution().palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])) == [[0, 1], [1, 0], [2, 4], [3, 2]]
