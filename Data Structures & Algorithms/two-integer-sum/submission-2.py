class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} #mapping of numbers to their indices 
        seen = set() #O(1) lookups for all seen numbers

        for i in range(len(nums)):
            if target - nums[i] in seen:
                return [hm[target - nums[i]], i]
            seen.add(nums[i])
            hm[nums[i]] = i
        