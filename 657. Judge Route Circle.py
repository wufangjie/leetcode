class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        pos = [0, 0]
        for step in moves:
            if step == 'U':
                pos[1] += 1
            elif step == 'D':
                pos[1] -= 1
            elif step == 'L':
                pos[0] -= 1
            else:
                pos[0] += 1
        return pos[0] == 0 and pos[1] == 0

print(Solution().judgeCircle('UD'))
print(Solution().judgeCircle('LL'))
