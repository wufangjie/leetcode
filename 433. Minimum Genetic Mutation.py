from collections import deque


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        if end not in bank:
            return -1

        two_part = [{start: 0}, {end: 1}] # start part, end part

        def bfs(start, part, suspend=500):
            other = part ^ 1
            Q = deque([start])
            count = 0
            while Q:
                if count % suspend == 0:
                    yield -1
                count += 1
                gene = Q.popleft()
                step = two_part[part][gene]
                for i in range(8):
                    for c in 'ACGT':
                        if c != gene[i]:
                            new = gene[:i] + c + gene[i+1:]
                            if new in two_part[other]:
                                yield step + two_part[other][new]
                                return # this return is faster? 46ms vs 32ms
                            elif new in bank:
                                two_part[part][new] = step + 1
                                Q.append(new)

        g1, g2 = bfs(start, 0), bfs(end, 1)
        while True:
            try:
                ret = next(g1)
                if ret > 0:
                    return ret
                ret = next(g2)
                if ret > 0:
                    return ret
            except StopIteration:
                return -1


assert Solution().minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]) == 1
assert Solution().minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]) == 2
assert Solution().minMutation("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]) == 3
