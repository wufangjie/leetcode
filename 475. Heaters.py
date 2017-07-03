class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters = [float('-inf')] + sorted(heaters) + [float('inf')]
        i, j = 0, 1
        r = 0
        for i in range(len(houses)):
            while houses[i] > heaters[j]:
                j += 1
            r = max(r, min(houses[i] - heaters[j - 1], heaters[j] - houses[i]))
        return r
