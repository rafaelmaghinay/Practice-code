#computes factorial of a number

def factorial(n):
    if n is 1:
        return 1
    
    return n * factorial(n-1)

num = 7
print(f"the factorial of {num} is {factorial(num)}")