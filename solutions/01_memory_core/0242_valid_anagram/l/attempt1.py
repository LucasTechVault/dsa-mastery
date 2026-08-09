from collections import defaultdict

def validAnagram(s: str, t: str) -> bool:
    # 1. Optimization check
    if len(s) != len(t):
        return False

    counter = defaultdict(int)
    
    # 2. build counter
    for c in s:
        counter[c] += 1
    
    # 3. validate
    for c in t:
        if counter[c] == 0:
            return False
    
        counter[c] -= 1
    
    return True