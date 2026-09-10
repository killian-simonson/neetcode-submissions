class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        vol = volume(l, r, heights)
        max_vol = vol

        while l < r:
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            new_vol = volume(l, r, heights)
            
            if new_vol > max_vol:
                max_vol = new_vol
        
        return max_vol

def volume(l, r, heights):
    return (r - l) * min(heights[l], heights[r])
