def descending_order(num):
    
    a = str(num)

    x = list (a)

    x.sort(reverse=True)

    y = "".join(x)

    final_result = int(y)

    return final_result


print(descending_order(123456789))
# 987654321