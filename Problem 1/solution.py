"""
    This program calculates and displays the sum of 
    the multiples of 3 or 5 below 1000.
"""

n = 1000
sum_ = 0

for i in range(2, n):
    if i % 3 == 0 or i % 5 == 0:
        # print(i)
        sum_ += i
        
print(sum_)
