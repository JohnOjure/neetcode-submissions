class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_possible_combinations = []

        def backtrack(start, current_path):

            all_possible_combinations.append(list(current_path))

            for i in range(start, len(nums)):
                current_path.append(nums[i])
                
                backtrack((i + 1), current_path)

                current_path.pop()

        backtrack(0, [])
        return all_possible_combinations