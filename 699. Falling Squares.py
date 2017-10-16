import bisect


class Solution(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        pos = [float('-inf'), float('inf')]
        height = [0, 0]
        n = len(positions)
        ret = [0] * n
        for k, (l, w) in enumerate(positions):
            i = bisect.bisect_right(pos, l) - 1       # pos[i] <= l
            j = bisect.bisect_left(pos, l + w, i + 1) # pos[j] >= l + w
            newH = max(height[i:j]) + w

            if pos[i] == l:
                if pos[j] == l + w:
                    j += 1 # NOTE important
                if j - 1 > i:
                    height[i] = newH
                    pos[j - 1] = l + w
                    if j - 1 > i + 1:
                        pos = pos[:i+1] + pos[j-1:]
                        height = height[:i+1] + height[j-1:]
                else:
                    pos.insert(i + 1, l + w)
                    height.insert(i, newH)
            elif pos[j] == l + w:
                if i + 1 < j:
                    pos[i + 1] = l
                    height[i + 1] = newH
                    if i + 2 < j:
                        pos = pos[:i+2] + pos[j:]
                        height = height[:i+2] + height[j:]
                else:
                    pos.insert(i + 1, l)
                    height.insert(i + 1, newH)
            else:
                pos = pos[:i+1] + [l, l + w] + pos[j:]
                height = height[:i+1] + [newH] + height[j-1:]

            ret[k] = max(newH, ret[k - 1])

        return ret


print(Solution().fallingSquares([[1, 2], [2, 3], [6, 1]]))
print(Solution().fallingSquares([[100, 100], [200, 100]]))
print(Solution().fallingSquares([[46,18],[34,1],[77,40],[38,90],[16,5],[1,11],[70,79],[2,56],[67,14],[19,67]]))
