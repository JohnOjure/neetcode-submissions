class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        #slots is available slots left in the string to be filled

        def backtrack(current_path, o_count, c_count, slots):
            print(f"Current Path: {"".join(current_path[:])}, {o_count}, {c_count}")
            if len(current_path) == 2 * n and o_count == n and c_count == n:
                output.append("".join(current_path[:]))
                return
            if o_count > n:
                return
            if c_count > o_count:
                return
            
            # for i in range(1):
            current_path.append("(")
            backtrack(current_path, o_count + 1, c_count, slots-1)
            current_path.pop()

            current_path.append(")")
            backtrack(current_path, o_count, c_count + 1, slots-1)
            current_path.pop()
        
        backtrack([], 0, 0, 2 * n)
        return output