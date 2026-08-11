def removeDuplicates(nums: list[int]) -> int:
    # Guard clause - empty list
    if not nums:
        return 0

    # first element always unique, start from idx 1
    anchor, explorer = 1, 1
    
    # Begin exploration
    while explorer < len(nums):
        
        # If mismatch from previous element (since sorted)
        if nums[explorer] != nums[anchor - 1]:
            nums[anchor] = nums[explorer]
            anchor += 1
        
        explorer += 1
    
    # Because arr 0-idx, anchor is exactly equals total number of items behind it
    # return anchor will do
    return anchor