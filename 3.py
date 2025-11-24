class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    
        # found = []
        # max_len = 0
        # i = 0
        # last_i = 0
        # count = 0

        # while i < len(s):
        #     if s[i] not in found:
        #         found.append(s[i])
        #         count += 1
        #         i += 1
        #     else:
        #         if count > max_len:
        #             max_len = count
        #         count = 0
        #         last_i += 1
        #         i = last_i
        #         found = []

        # if count > max_len:
        #     max_len = count

        # return max_len

        last_pos = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in last_pos and last_pos[char] >= left:
                left = last_pos[char] + 1
            last_pos[char] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len