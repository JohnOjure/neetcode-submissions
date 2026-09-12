class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i think, 

        # start at an index (i0), add to seen, try to extend window (r+=1). 
        # get to new elem s[r]
        # run backgenic check
        # r += 1
        
        # while s[r] in seen: #backgenic check
        #     seen.remove(s[l])
        #     l += 1

        #we run backgenic checks in each windowing process

        longest, tl, l, r = 0, 0, 0, 0
        seen = set()

        while r < len(s): #windowing process
            
            while s[r] in seen: #backgenic check
                seen.remove(s[l])
                tl -= 1
                l += 1

            seen.add(s[r]) 
            tl += 1
            r += 1 
            longest = tl if tl > longest else longest
        
        return longest



