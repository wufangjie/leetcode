'''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.
Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
'''

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        div = 1
        while x / div > 9:
            div *= 10

        while x > 0:  # not x > 9
            if x // div != x % 10:
                return False
            x -= div * (x // div)
            x //= 10
            div //= 100
        return True

if __name__ == '__main__':
    assert Solution().isPalindrome(0) == True
    assert Solution().isPalindrome(-3) == False
    assert Solution().isPalindrome(10001) == True
    assert Solution().isPalindrome(1000021) == False
    assert Solution().isPalindrome(7) == True
