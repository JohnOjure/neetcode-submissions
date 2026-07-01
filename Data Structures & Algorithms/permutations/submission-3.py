# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         results = []

#         def backtrack(current_path, avd_idx):
#             if len(current_path) == len(nums):
#                 results.append(current_path[:])
#                 return

#             for i in range(len(nums)):
#                 if i in avd_idx:
#                     continue

#                 current_path.append(nums[i])
#                 avd_idx.append(i)

#                 backtrack(current_path, avd_idx)

#                 current_path.pop()
#                 avd_idx.pop()


#         backtrack([], [])
#         return results


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtrack(current_path, used):
            if len(current_path) == len(nums):
                results.append(current_path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                current_path.append(nums[i])
                used[i] = True

                backtrack(current_path, used)

                current_path.pop()
                used[i] = False


        backtrack([], [False]*len(nums))
        return results
