class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights)-1
        max_area = 0

        ans = 0
        while(s<e):
            max_area = max(max_area,((e-s)*min(heights[s],heights[e])))
            if heights[s]<heights[e]:
                s+=1
            else:
                e-=1
            
        
        return max_area
