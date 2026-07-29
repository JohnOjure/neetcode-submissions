class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ans = 0

        for char in operations:
            if char == "+":
                res.append(res[-1] + res[-2])
                ans += res[-1]

            elif char == "C":
                ans -= res[-1]
                del res[-1]

            elif char == "D":
                res.append(2 * res[-1])
                ans += res[-1]       

            else:
                res.append(int(char))
                ans += res[-1]
        
        return ans
            
        