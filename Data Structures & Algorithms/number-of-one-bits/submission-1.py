class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        # while n > 0:
        #     count += n & (n - 1)
            
        # erase the rightmost 1
        # then check if the number still greater than 0:
        #     count += 1
        #     if so, repeat again
        
        # n = n & (n - 1)
        while n > 0:
            n = n & (n - 1)
            count += 1
        return count