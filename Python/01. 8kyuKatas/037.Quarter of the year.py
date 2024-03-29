# DESCRIPTION:
# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: 
# Month 2 (February), is part of the first quarter; 
# Month 6 (June), is part of the second quarter;
# Month 11 (November), is part of the fourth quarter.

# ============
# Solution:
# ============

def quarter_of(month):

    if month in [1,2,3]:

        return 1

    elif month in [4,5,6]:

        return 2

    elif month in [7,8,9]:

        return 3

    elif month in [10,11,12]:

        return 4


print(quarter_of(5))
# 2

print(quarter_of(10))
# 4
