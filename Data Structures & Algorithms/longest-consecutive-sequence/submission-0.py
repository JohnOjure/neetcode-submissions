class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, i, j = 0, 0, 0

        nums = list(set(nums))
        nums.sort()

        while i < len(nums) and j < len(nums):
            if (j + 1) < len(nums) and nums[j + 1] == 1 + nums[j]:
                j += 1
                continue
            
            if j - i + 1 > longest:
                longest = j - i + 1

            i = j + 1
            j += 1
        
        return longest
                    






            #dont forget to reset temp and update i