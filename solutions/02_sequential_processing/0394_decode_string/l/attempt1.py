def decodeStr(s: str) -> str:
    stack = []
    
    cur_str = "" # handle str at 'current' level
    cur_num = 0 # handle num (multiplier) at cur level
    
    # 1. iterate each char
    for c in s:
        # 4 possibilities
        # 1.1 - char is digit
        if c.isdigit():
            cur_num = (cur_num * 10) + int(c)
        
        # 1.2 - char is alpha
        elif c.isalpha():
            cur_str += c
        
        # 1.3 - char is '[' - append state to waiting room & reset for deeper leevel
        elif c == '[':
            stack.append((cur_str, cur_num))
            cur_str = ""
            cur_num = 0
        
        # 1.4 - char is ']' - retrieve previous level state & update 
        else:
            prev_str, multiplier = stack.pop()
            
            # cur_str here is the innermost alphabets - multiply with multiplier & add prev_str to prefix
            # overwrite cur_str at every level to "update" latest
            cur_str = prev_str + (cur_str * multiplier) # update cur_str
    
    return cur_str
