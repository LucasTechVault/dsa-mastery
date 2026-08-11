def threeSum(nums: list[int]) -> list[list[int]]:
    # 1. Sort array
    nums.sort()
    
    # 2. initialize required
    anchor = 0
    result = []
    n = len(nums)
    
    # 3. iterate each element
    while anchor < n:
        # 3.1 optimization clause - no way to sum to 0 since sorted
        if nums[anchor] >= 0: 
            break
    
        # 3.2 duplicate check
        if anchor > 0 and nums[anchor] == nums[anchor-1]:
            anchor += 1
            continue
            
        # 3.3 begin 2-sum engine
        l, r = anchor + 1, n - 1
        while l < r:
            cur_sum = nums[anchor] + nums[l] + nums[r]
            
            if cur_sum > 0:
                r -= 1
            elif cur_sum < 0:
                l += 1
            else:
                result.append([nums[anchor], nums[l], nums[r]])
                l += 1
                # duplicate check
                while l < r and nums[l] == nums[l-1]:
                    l += 1
        
        # 4. increment anchor
        anchor += 1
        
    return result
    