class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def backtrack(current_path, o_count, c_count):

            if len(current_path) == 2 * n and o_count == n and c_count == n:
                output.append("".join(current_path[:]))
                return

            # if o_count > n:
            #     return

            # if c_count > o_count:
            #     return
            
            # for i in range(1):
            if o_count < n:
                current_path.append("(")
                backtrack(current_path, o_count + 1, c_count)
                current_path.pop()

            if c_count < o_count:
                current_path.append(")")
                backtrack(current_path, o_count, c_count + 1)
                current_path.pop()
            
        backtrack([], 0, 0)
        return output



