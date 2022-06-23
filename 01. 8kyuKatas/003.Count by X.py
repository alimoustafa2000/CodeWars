def count_by(x, n):
    
    a = []
    
    for num in range(1, n+1, 1):
        
        result = x * num
        
        a.append(result)
        
    return a
        
        
print(count_by(2, 5))
# [2, 4, 6, 8, 10]