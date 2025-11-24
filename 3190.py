class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if (1 <= len(nums) <= 50):
            nOps = 0

            for num in nums:
                if not (1 <= num <= 50):
                    return 0
                if (num % 3) != 0:
                    nOps += 1
            
            return nOps
        return 0