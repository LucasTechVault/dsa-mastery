def twoSum(nums: list[int], target: int) -> list[int]:
    # 1. hashmap to track seen val & idx
    idx_tracker = {}
    
    # 2. iterate each val
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in idx_tracker:
            return [i, idx_tracker[complement]]

        idx_tracker[nums[i]] = i
    
    
    