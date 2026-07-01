class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ma = 0, len(height)-1, 0
        while l < r:
            ma = max((r-l)*min(height[l], height[r]), ma)
            if height[l]<height[r]: l+=1
            else: r-=1
        return ma