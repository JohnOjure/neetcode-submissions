from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hm = {}
        
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
            
            if hm[num] > len(nums)//2:
                return num
