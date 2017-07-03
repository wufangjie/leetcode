'''
Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.
Have you thought about this?

Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Update (2014-11-10):
Test cases had been added to test the overflow behavior.
'''

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            rx = -int(str(x)[:0:-1])
        else:
            rx = int(str(x)[::-1])

        limit = 0xffffffff >> 1
        if rx > limit or rx < -limit - 1:
            return 0
        return rx


if __name__ == '__main__':
    assert Solution().reverse(1000000003) == 0
    assert Solution().reverse(-10100) == -101
