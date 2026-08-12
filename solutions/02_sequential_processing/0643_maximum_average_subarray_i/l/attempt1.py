def findMaxAvg(nums: list[int], k: int) -> float:
    # 1. init cur_sum with first k elements
    cur_sum = sum(nums[:k])
    
    # 2. init max_sum to track maximum
    max_sum = cur_sum # cur max = cur sum
    
    # 3. Iterate each element from k to end
    for i in range(k, len(nums)):
        cur_sum = cur_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, cur_sum)
    
    # 4. return avg 
    return max_sum / k
