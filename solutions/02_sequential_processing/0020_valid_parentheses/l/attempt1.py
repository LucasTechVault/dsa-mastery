def validParenthesis(s: str) -> bool:
    # 1. Initialize required
    stack = []
    mapping = { # closing as key to check
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # 2. iterate each char
    for c in s:
        if c not in mapping: # open brace
            stack.append(c)
        
        else: # else closing brace
            # 2.1 - empty stack check
            if not stack:
                return False

            # 2.2 - parenthesis match check
            top = stack.pop()
            if top != mapping[c]:
                return False
    
    # 3. All checks pass, check if residual in stack
    # cannot simply return True. Stack may have residual due to duplicates open braces (extra ammunition)
    return len(stack) == 0

    