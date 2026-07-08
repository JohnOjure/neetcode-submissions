class Solution:
    def countBits(self, n: int) -> List[int]:
        output, x = [], 0
        
        for i in range(0, n + 1):

            output.append(0)
            x = i 
            while (x) > 0:
                x &= (x - 1)
                output[i] += 1
        
        return output
        