class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        output = []

        def isPalindrome(s):
            l, r = 0, (len(s)-1)
            while l < r: 
                if s[l] == s[r]: l+=1; r-=1
                else: return False
            return True

        def backtrack(start, current_path):
            
            if start == len(s):
                output.append(current_path[:])
                return

            for end in range(start, len(s)):
                subs = s[start:end+1]
                
                if not isPalindrome(subs): continue

                current_path.append(subs)

                backtrack(end + 1, current_path)

                current_path.pop()
            
        backtrack(0, [])

        return output