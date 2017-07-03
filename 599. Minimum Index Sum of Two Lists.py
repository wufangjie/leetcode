class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dct2 = dict(zip(list2, range(len(list2))))
        theMin = len(list1) + len(list2)
        result = []
        for i, r in enumerate(list1):
            theSum = i + dct2.get(r, theMin)
            if theSum < theMin:
                theMin = theSum
                result = [r]
            elif theSum == theMin:
                result.append(r)
        return result


print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))
