def complete_bracket(brackets):

    stack = []

    for bracket in brackets:
        if bracket == '[':
            stack.append(']')
        elif bracket == '{':
            stack.append('}')
        elif bracket == '(':
            stack.append(')')    
        elif not stack or stack.pop() != bracket: # not stak == empty
            return False    

    return not stack

print(complete_bracket('[{()}]'))