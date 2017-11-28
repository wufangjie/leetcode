class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ret = []
        for elem in asteroids:
            if elem > 0:
                ret.append(elem)
            else:
                while ret:
                    if 0 < ret[-1] <= -elem:
                        temp = ret.pop()
                        if temp == -elem:
                            break
                    else:
                        if ret[-1] < 0:
                            ret.append(elem)
                        break
                else:
                    ret.append(elem)
        return ret


print(Solution().asteroidCollision([5, 10, -5]))
print(Solution().asteroidCollision([8, -8]))
print(Solution().asteroidCollision([10, 2, -5]))
print(Solution().asteroidCollision([-2, -1, 1, 2]))
