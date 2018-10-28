def parentheses_match(x):
    stack = []
    for item in x:
        if item in '([{':
            stack.append(item)
            continue
        if item.isnumeric():
            continue
        if item in '+-*/':
            continue
        if item in ')}]':
            if len(stack) == 0:
                return False
            else:
                p = stack.pop()
                if (p is '(' and item  is ')') or (p is '{' and item is '}') or (p is '[' and item is ']'):
                    continue
                else:
                    return False
    if len(stack) == 0:
        return True
    else:
        return False

