'''
A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

    For 1-byte character, the first bit is a 0, followed by its unicode code.
    For n-bytes character, the first n-bits are all one's, the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

'''


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        count = 0
        for elem in data:
            if count:
                if elem & 0b11000000 != 0b10000000:
                    return False
                count -= 1
            elif elem & 0b10000000 == 0b00000000:
                pass
            elif elem & 0b11100000 == 0b11000000:
                count = 1
            elif elem & 0b11110000 == 0b11100000:
                count = 2
            elif elem & 0b11111000 == 0b11110000:
                count = 3
            else:
                return False
        return count == 0


        # count = 0
        # for elem in data:
        #     test = '{:08b}'.format(elem)
        #     if count:
        #         if not test.startswith('10'):
        #             return False
        #         count -= 1
        #     elif test.startswith('0'):
        #         pass
        #     elif test.startswith('110'):
        #         count = 1
        #     elif test.startswith('1110'):
        #         count = 2
        #     elif test.startswith('11110'):
        #         count = 3
        #     else:
        #         return False
        # return count == 0



# use & will faster




print(Solution().validUtf8([197,130,1]))
