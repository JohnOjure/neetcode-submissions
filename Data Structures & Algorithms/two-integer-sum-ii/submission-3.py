class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, j = 0, len(numbers) - 1

        while i < j:
            addtn = numbers[i] + numbers[j]
            
            if addtn == target:
                return [i + 1, j + 1]
            elif addtn < target:
                i += 1
            elif addtn > target:
                j -= 1
        
