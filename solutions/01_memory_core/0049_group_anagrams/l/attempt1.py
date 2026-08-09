from collections import defaultdict

def groupAnagram(strs: list[str]) -> list[list[str]]:
    results = defaultdict(list)
    
    for word in strs:
        key = "".join(sorted(word))
        results[key].append(word)
    
    return list(results.values())