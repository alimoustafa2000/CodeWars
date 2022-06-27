def square_sum(numbers):
    
    a = []
    
    for number in numbers:
        
        x = number ** 2
        
        a.append(x)
        
    return sum(a)


print(square_sum([0, 3, 4, 5]))
# 50