class Solution:
    def trap(self, height: List[int]) -> int:
        ta, sta, see, end, bls, mh, mhi = 0, 0, 0, len(height)-1, 0, 0, 0
        
        for i, num in enumerate(height):
            if mh > num: continue
            elif mh < num: mh, mhi = num, i

        while see <= mhi:
            if height[sta] > height[see]: bls, see = bls+height[see], see+1
            else:
                ta += (min(height[sta], height[see])*max((see-sta-1), 0)) - bls
                bls, sta, see = 0, see, see+1

        see, sta, bls = end, end, 0

        while mhi <= see:
            if height[sta] > height[see]: bls, see = bls+height[see], see-1 
            else:
                ta += (min(height[sta], height[see])*max((sta-see-1), 0)) - bls
                bls, sta, see = 0, see, see-1
        
        return ta
