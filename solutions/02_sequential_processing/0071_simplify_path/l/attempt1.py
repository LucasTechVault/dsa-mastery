def simplifyPath(path: str) -> str:
    stack = []
    
    # 1. Clean up instructions
    cleaned = path.split('/')
    
    # 2. iterate each token
    for c in cleaned:
        
        # 2.1 - '..' check - go up 1 dir
        if c == '..':
            if stack: # guard clause
                stack.pop()
        
        # 2.2 - '.' or '' check : '' results from multiple slashes
        elif c == '.' or c == '':
            continue # do nothing
    
        
        else: # else valid path, append
            stack.append(c)
    
    return '/' + '/'.join(stack)
            