# coding: utf-8
from operator import add, sub, mul, div

operator_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

operators = {  # 运算符操作表
    '+': lambda op1, op2: op1 + op2,
    '-': lambda op1, op2: op1 - op2,
    '*': lambda op1, op2: op1 * op2,
    '/': lambda op1, op2: op1 / op2,
}


def fuc(expr):
    exprs = expr.split()
    stack = []
    for expr in exprs:
        if expr in operator_dict.keys():
            y = stack.pop()
            x = stack.pop()
            stack.append(operator_dict[expr](x, y))
        elif expr.isdigit():
            stack.append(int(expr))
    return stack.pop()

33
print(fuc('2 3 4 * +'))  # 2 + 3 * 4 = 14
print(fuc('1 2 + 6 3 / * 2 +'))  # ( 1 + 2 ) * ( 6 / 3 ) + 2 = 8
print(fuc('18 3 1 2 + * /'))  # 18 / ( 3 * ( 1 + 2 ) ) = 2 
