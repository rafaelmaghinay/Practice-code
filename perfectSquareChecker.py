#checks if a number is a perfect square

import math

def squareChecker(num):
    squareRoot = math.sqrt(num)   
    return squareRoot.is_integer()

num = 26    
if squareChecker(num) is True:
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")