class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        output = set()
        target = 0

        for i in range(len(nums)):
            hm = {}
            target = -1 * nums[i]

            for j in range(i + 1, len(nums)):
                if target - nums[j] in hm:
                    output.add(tuple(sorted([nums[i], target - nums[j], nums[j]])))
                else:
                    hm[nums[j]] = j
        
        return list(map(list, output))