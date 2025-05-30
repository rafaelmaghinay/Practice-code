#checks if a number is a prime number

def isPrime(num):
    flag = False
    
    #number is 0 or 1
    if num == 0 or num == 1:
        flag = True
        
    elif num > 1:
        
        #finds a factor
        for i in range(2, num):
            if num % 2 == 0:
                flag = True
                break
    return flag        


num = 10
notPrime = isPrime(num)
if notPrime == True:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
        
                