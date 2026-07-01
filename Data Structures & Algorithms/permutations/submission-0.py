class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        # def backtrack(start, current_path):
            
        #     if len(current_path) == len(nums):
        #         results.append(current_path[:])
        #         return

        #     for i in range(start, len(nums)):
        #         current_path.append(nums[i])
        #         backtrack((i + 1), current_path)
        #         current_path.pop()


        # def backtrack(current_path, skip_idx):
            
        #     if len(current_path) == len(nums):
        #         results.append(current_path[:])
        #         return

        #     for idx, num in enumerate(nums):
        #         if idx == skip_idx: 
        #             continue
        #         current_path.append(nums)
        #         backtrack(current_path, idx)
        #         current_path.pop()

        # def backtrack(current_path, remaining_options):
        #     if len
            
        #     for num in nums:
        #         current_path.append(nums)
        #         backtrack(current_path, remaining_options)
        #         current_path.pop()


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

            





        