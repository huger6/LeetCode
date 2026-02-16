class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        len_strs = len(strs)

        if not 1 <= len_strs <= 200:
            return ""
        
        for i in range(1, len_strs):
            current_s = strs[i]

            if not 0 <= len(current_s) <= 200:
                return ""

            while not current_s.startswith(prefix):
                prefix = prefix[:-1] # Cut last letter

                if not prefix:
                    return ""
                
        return prefix
