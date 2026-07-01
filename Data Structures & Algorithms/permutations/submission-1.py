class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(current_path, avd_idx):
            if len(nums) - len(avd_idx) == 0:
                results.append(current_path[:])
                return

            for i in range(len(nums)):
                if i in avd_idx:
                    continue

                current_path.append(nums[i])
                avd_idx.append(i)

                backtrack(current_path, avd_idx)
                
                current_path.pop()
                avd_idx.pop()


        backtrack([], [])
        return results
