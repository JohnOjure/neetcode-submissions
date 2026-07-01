class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start, current_path, current_sum):
            if current_sum > target:
                return

            if current_sum == target:
                result.append(current_path[:])
                return
                
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                current_path.append(candidates[i])

                backtrack((i + 1), current_path, (current_sum + candidates[i]))  
                
                current_path.pop()  
        
        backtrack(0, [], 0)
        return result