LEFT = ['{', '(', '[']
RIGHT = ['}', ')', ']']


def match(exprs):
    stack = []
    for expr in exprs:
        if expr in LEFT:
            stack.append(expr)
        elif expr in RIGHT:
            if not stack or not 1 <= ord(expr) - ord(stack[-1]) <= 2:
                return False
            stack.pop()
    return not stack

print(match("[}"))
print(match("[]"))
