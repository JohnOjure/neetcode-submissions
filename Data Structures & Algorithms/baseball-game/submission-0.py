class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        ans = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                res.append(res[-1] + res[-2])
                ans += res[-1]

            elif operations[i] == "C":
                ans -= res[-1]
                del res[-1]

            elif operations[i] == "D":
                res.append(2 * res[-1])
                ans += res[-1]       

            else:
                res.append(int(operations[i]))
                ans += res[-1]
        
        return ans
            
        