# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         result = set()

#         def backtrack(current_path):
#             if sum(current_path) > target:
#                 return

#             if sum(current_path) == target and tuple(sorted(current_path)) not in result:
#                 result.add(tuple(sorted(current_path)))
#                 return
            
#             for num in nums:
#                 current_path.append(num)
#                 backtrack(current_path)
#                 current_path.pop()
        
#         backtrack([])
#         return [list(tuple_list) for tuple_list in result]









# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         result = []
#         seen_lists = set()

#         def backtrack(current_path: List[int]):
#             print(f"curr_path: {current_path}")
#             if sum(current_path) == target and tuple(sorted(current_path)) not in seen_lists:
#                 result.append(current_path[:])
#                 seen_lists.add(tuple(current_path))
#                 return
#             if sum(current_path) > target:
#                 return
            
#             for num in nums:
#                 current_path.append(num)
#                 backtrack(current_path)
#                 current_path.pop()
        
#         backtrack([0])
#         return result





# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         result = set()

#         def backtrack(current_path, current_sum):
#             if current_sum > target:
#                 return

#             if current_sum == target and tuple(sorted(current_path)) not in result:
#                 result.add(tuple(sorted(current_path)))
#                 return
            
#             for num in nums:
#                 current_path.append(num)
#                 current_sum += num
#                 backtrack(current_path, current_sum)
#                 current_path.pop()
#                 current_sum -= num
        
#         backtrack([], 0)
#         return [list(tuple_list) for tuple_list in result]



class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, current_path, current_sum):
            if current_sum > target:
                return

            if current_sum == target:
                result.append(current_path[:])
                return
            
            for i in range(start, len(nums)):
                current_path.append(nums[i])
                backtrack(i, current_path, current_sum + nums[i])
                current_path.pop()
        
        backtrack(0, [], 0)
        return result


