def maxArea(heights: list[int]) -> int:
    l, r = 0, len(heights) - 1
    max_area = 0 # to track max area
    
    # 1. iterate each element
    while l < r:
        l_height = heights[l]
        r_height = heights[r]
        
        cur_height = min(l_height, r_height) # height bounded by lower 
        cur_width = r - l
        cur_area = cur_height * cur_width
        
        # 2. Update max area
        max_area = max(max_area, cur_area)
        
        # 3. update iteration
        if l_height < r_height:
            l += 1
        else:
            r -= 1
    
    return max_area