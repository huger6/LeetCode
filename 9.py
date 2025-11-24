import math

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True

        found = []
        
        len_x = math.floor(math.log10(abs(x))) + 1
        half_len = len_x // 2

        index = 0
        while (index < half_len):
            digit = x % 10
            x //= 10
            found.append(digit)
            index += 1

        same_x = 0
        found_len = len(found)
        for i, num in enumerate(found):
            same_x += num * pow(10, found_len - i - 1)
        
        # Remove middle number
        if len_x % 2 != 0:
            x //= 10

        if x == same_x:
            return True

        return False