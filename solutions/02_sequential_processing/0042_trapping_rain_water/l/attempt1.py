def trapRainWater(heights: list[int]) -> int:
    # 1. Guard clause - if < 3 - cannot trap water
    if len(heights) < 3:
        return 0

    # 2. Init required var
    l, r = 0, len(heights) - 1
    seen_max_l, seen_max_r = 0, 0 # to track highest seen, for calculating 'trapped' water
    total_water = 0 # accumulate water
    
    # 3. Iterate
    while l < r:
        # 3.1 - specify left to right processing
        ## We can also specify right to left, if so desired. No difference (i.e if height[r] < height[l])
        if heights[l] < heights[r]:
            
            # First update highest seen to track, for purpose of accumulating trapped water
            if heights[l] >= seen_max_l:
                seen_max_l = heights[l]
            else:
                total_water += (seen_max_l - heights[l]) # compute water trapped at current idx
                
            l += 1
        
        # Else, process right side (cannot just keep evaluating left side)
        else:
            # Similarly, track highest seen for right side for purpose of finding trapped water
            if heights[r] >= seen_max_r:
                seen_max_r = heights[r]
            
            else:
                total_water += (seen_max_r - heights[r])
            
            r -= 1  
    
    return total_water