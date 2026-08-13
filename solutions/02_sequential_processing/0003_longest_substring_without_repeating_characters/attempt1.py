def lenOfLongestSubstr(s: str) -> int:
    l, r = 0, 0
    longest = 0
    unique = set()
    
    while r < len(s):
        # 2. Handle duplicate detected
        while s[r] in unique:
            unique.remove(s[l])
            l += 1
        
        # 1. First char always unique, add to set
        # Duplicate cleared, char is unique, add to set
        unique.add(s[r])
        
        # 3. Track length
        cur_len = r - l + 1
        r ++ 1
        
        longest = max(longest, cur_len)
    
    return longest