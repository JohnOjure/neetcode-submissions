class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(0, 32):
            if (n >> i) & 1 : 
                #if that is that, then we wanna construct the 1 in the (31-i)th position
                #so we shift a 1 to that side
                res |= 1 << (31 - i)
        
        return res
        








