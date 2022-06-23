def basic_op(operator, value1, value2):
    
    if operator == "+":
        return value1 + value2
    
    elif operator == "-":
        return value1 - value2
    
    elif operator == "*":
        return value1 * value2
    
    elif operator == "/":
        return value1 / value2


print(basic_op('+', 2, 2))
# 4
print(basic_op('-', 2, 2))
# 0
print(basic_op('*', 2, 2))
# 4
print(basic_op('/', 2, 2))
# 1.0