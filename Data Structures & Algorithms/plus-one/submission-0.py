class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = ""
        output = []
        
        for digit in digits:
            num += str(digit)
            
        num = str(int(num) + 1)
        
        for digit in num:
            output.append(int(digit))
            
        return output
