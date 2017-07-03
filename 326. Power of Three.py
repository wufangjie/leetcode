return_true = {3 ** i for i in range(20)}


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n in return_true



# 垃圾题目, log 和求余, 其实是暗藏循环或递归的; 直接用 3 的 19次方是最大, 那我是不是直接穷举不就完了
# 靠限制明明很常用的东西来出题, 不过是奇技淫巧
# 写在类里慢很多, 可能是多次创建类
