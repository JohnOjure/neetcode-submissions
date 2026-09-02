class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []

        hm = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(start, current_path):
            if len(current_path) == len(digits):
                output.append(current_path[:])
                return 

            #choose
            for char in hm[digits[start]]: 
                #for character at every level of the 
                #particular digit we're considering, choose
                #one of the possible characters that it could reporesent 
                current_path += char

                backtrack(start + 1, current_path)

                current_path = current_path[:-1]

        backtrack(0, "")

        return output if digits else []


