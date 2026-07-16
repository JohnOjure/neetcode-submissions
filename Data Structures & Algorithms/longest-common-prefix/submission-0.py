class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        first_str = strs[0]
        
        for i in range(len(first_str)):
            for string in strs[1:]:
                if i >= len(string) or string[i] != first_str[i]:
                    return first_str[:i]
                    
        return first_str
