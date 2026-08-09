def longestConsecutiveStreak(nums: list[int]) -> int:
    # 1. Handle duplicates since duplicates doesnt help
    nums_set = set(nums)
    longest_streak = 0 # to track longest seen
    
    # 2. Iterate each number
    for num in nums_set:
        
        # 2.1 Begin only if START of sequence
        # START means (num - 1) doesn't exist
        if (num - 1) not in nums_set:
            cur_num = num
            cur_streak = 1 # cur_num itself considered 1
            
            while (cur_num + 1) in nums_set:
                cur_num += 1
                cur_streak += 1
            
            # No more streak, update longest
            if cur_streak > longest_streak:
                longest_streak = cur_streak
        
    return longest_streak