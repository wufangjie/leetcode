'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        result = [[] for _ in xrange(numRows)]
        cursor, direct = 0, 1
        for elem in s:
            result[cursor].append(elem)
            cursor += direct
            if cursor == numRows:
                cursor, direct = numRows - 2, -1
            elif cursor == -1:
                cursor, direct = 1, 1
        temp = [''.join(x) for x in result]
        return ''.join(temp)


    def convert_too_slow(self, s, numRows):
        from itertools import izip_longest, chain
        # for python2, zip_longest otherwise
        if numRows == 1:
            return s
        step = 2 * numRows - 2
        result = s[::step]
        shift = 2 * numRows - 3
        for i in range(1, numRows - 1):
            result += ''.join(chain(*izip_longest(
                s[i::step], s[shift::step], fillvalue='')))
            shift -= 1
        return result + s[numRows - 1::step]



if __name__ == '__main__':
    assert Solution().convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
