class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force O(n^2) try to find the inxes that would have best area
        #area formula = min(height[i], height[j]) * (j-i)

        max_area = 0 
        i = 0
        j = len(heights) -1 

        while i < j:
            #calc the area and find the max 
            area = (j-i) * min(heights[i], heights[j])  
            max_area = max(max_area, area)

            #move the pointer with smallest value..
            if heights[i] < heights[j]:
                #move the left pointer
                i+=1
            else:
                j-=1

        return max_area
