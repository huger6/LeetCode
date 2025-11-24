class Solution:
    def romanToInt(self, s: str) -> int:
        if 1 <= len(s) <= 15:
            values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

            res = 0
            len_s = len(s)
            i = 0

            while i < len_s:
                if s[i] not in list(values.keys()):
                    return 0
                if i < len_s - 1:
                    if s[i] == 'I' and s[i+1] in ['V', 'X']:
                        res += values[s[i+1]] - values[s[i]]
                        i += 2
                    elif s[i] == 'X' and s[i+1] in ['L', 'C']:
                        res += values[s[i+1]] - values[s[i]]
                        i += 2
                    elif s[i] == 'C' and s[i+1] in ['D', 'M']:
                        res += values[s[i+1]] - values[s[i]]
                        i += 2
                    else:
                        res += values[s[i]]
                        i += 1
                else:
                    res += values[s[i]]
                    i += 1

            return res
        return 0