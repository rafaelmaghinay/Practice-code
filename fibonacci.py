#finds fibonacci of the nth number

def fibonacci(n):
    if n <= 1:
        return n
    
    return fibonacci(n-1) + fibonacci(n-2)

num = input("enter a number and we'll solve for the fibonacci: ")
num = int(num)
print(f"fibonacci of {num} is {fibonacci(num)}")