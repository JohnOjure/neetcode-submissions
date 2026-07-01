class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def backtrack(start, current_path):
            results.append(current_path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                current_path.append(nums[i])
                backtrack((i + 1), current_path)
                current_path.pop()
        
        backtrack(0, [])
        return results
        