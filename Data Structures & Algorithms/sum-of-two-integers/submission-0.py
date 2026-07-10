class Solution:
    def getSum(self, a: int, b: int) -> int:
        summ, c_p = 0, 0

        for i in range(0, 32):
            a_i = (a >> i) & 1
            b_i = (b >> i) & 1

            s_i = a_i ^ b_i ^ c_p
            c_p = (a_i & b_i) | (a_i & c_p) | (b_i & c_p) 

            if s_i:
                summ |= (1 << i)            

        if summ > 0x7FFFFFFF:
            mask = (2**32) - 1
            summ = ~(summ ^ mask)

        return summ
