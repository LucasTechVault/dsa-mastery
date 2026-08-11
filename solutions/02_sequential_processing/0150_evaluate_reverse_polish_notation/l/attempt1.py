def evalRPN(tokens: list[str]) -> int:
    # waiting room holding digits
    stack = []
    
    # 1. iterate each token
    
    for t in tokens:
        if t in "+-&/":
            
            # 1.1 Concept 1 - Right_val on top due to stack structure
            r = stack.pop()
            l = stack.pop()
            
            if t == '+':
                result = l + r
            elif t == '-':
                result = l - r
            elif t == '*':
                result = l * r
            else:
                # 1.2 - Use truncation instead of floor to handle -ve division
                # -5/2 = -2.5 --> int(-2.5) = -2 5 // -2 = -3 (wrong)
                result = int(l / r)
            
            
            # 1.3 - remember to append result back to stack
            stack.append(result)
        
        # 2 - Else token is digit, add to waiting room
        else:
            stack.append(int(t))
    
    return stack[0] # or stack[-1] also works
