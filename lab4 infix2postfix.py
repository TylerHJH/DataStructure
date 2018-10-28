def infix2postfix(expression):
    result = []     # 结果列表
    stack = []      # 栈
    for item in expression:      # 遍历表达式
        if item.isnumeric():    # 如果当前字符为数字，则直接放入结果列表
            result.append(item)
        elif len(stack) == 0:   # 如果栈为空，直接入栈
            stack.append(item)
        elif item in '*/(':     # 如果为*/(，入栈e
            stack.append(item)
        elif item in ')':       # 如果为(，弹出至)为止
            t = stack.pop()
            while t != '(':
                result.append(t)
                t = stack.pop()
        elif item in '+-' and stack[len(stack) - 1] in '*/':    # 如果当前字符为+-，且栈顶为*/
            if stack.count('(') == 0:                           # 无(则全弹出，当前字符入栈
                while stack:
                    result.append(stack.pop())
            else:
                t = stack.pop()
                while t != '(': # 有(则弹出至(，当前字符入栈
                    result.append(t)
                    t = stack.pop()
                stack.append('(')
            stack.append(item)
        else:
            stack.append(item)  # 其他情况直接入栈
    while stack:    # 遍历结束后，弹出栈中剩余项
        result.append(stack.pop())
    return ''.join(result)  # 以字符串返回


a = '1+5*4+(6+5*1)'
print(infix2postfix(a))
