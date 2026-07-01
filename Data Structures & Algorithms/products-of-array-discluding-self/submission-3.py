class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, n0, ln =  1, 0, 0

        for num in nums:
            if num == 0: n0+=1; ln+=1
            else: prod*=num; ln+=1
        
        if n0 >= 2: return [0] * ln
        
        if n0 == 1: return [0 if num != 0 else prod for num in nums]

        return [int(prod/num) for num in nums]
       