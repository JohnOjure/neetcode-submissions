class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xored, xored_2 = 0, 0
        for i in range(0, len(nums) + 1):
            xored ^= i
        
        for num in nums:
            xored_2 ^= num
        
        xored ^= xored_2

        return xored        

        