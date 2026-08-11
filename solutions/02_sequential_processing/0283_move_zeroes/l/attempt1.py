def moveZeroes(nums: list[int]) -> None:
    # 1. start read & write in same pos.
    read, write = 0, 0
    
    # 2. iterate every element
    while read < len(nums):
        
        # if element is not 0, perform a swap
        if nums[read] != 0:
            nums[read], nums[write] = nums[write], nums[read]
            write += 1 # increment write for next non-zero write
        
        # increment read to continue exploration
        read += 1
