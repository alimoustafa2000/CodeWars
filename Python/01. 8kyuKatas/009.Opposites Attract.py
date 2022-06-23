def love_fun( flower1, flower2 ):
    if flower1 % 2 == 0 and flower2 % 2 != 0:
        return True
    
    elif flower2 % 2 == 0 and flower1 % 2 != 0:
        return True
    
    else:
        return False


print(love_fun(2,5))
# True

print(love_fun(2,4))
# False
