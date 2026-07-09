class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing, nums = 0, nums + [i for i in range(0, len(nums) + 1)]

        for num in nums:
            missing ^= num
        
        return missing
        