class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        
        rest = 0

        for i in range(1, k + 1):
            rest = (rest * 10 + 1) % k
            if rest == 0:
                return i

        return -1