def twoSumii(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    
    while l < r:
        cur_sum = nums[l] + nums[r]
        
        if cur_sum == target:
            return [l+1, r+1]
        elif cur_sum < target:
            l += 1
        else:
            r -= 1
