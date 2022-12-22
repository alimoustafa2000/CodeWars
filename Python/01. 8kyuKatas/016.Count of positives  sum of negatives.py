# DESCRIPTION:
# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array.

# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# ============
# Solution:
# ============

def count_positives_sum_negatives(arr):
    
    positive = []
    negative = []
    result = []               
    
    for num in arr:
        if num > 0:
            positive.append(num)
            
        elif num < 0:
            negative.append(num)
            
    if arr == []:
        return []
            
    a_p = len(positive)
    result.append(a_p)
    
    a_n = sum(negative)
    result.append(a_n)
            
    return result

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
# [10, -65]

print(count_positives_sum_negatives([]))
# []