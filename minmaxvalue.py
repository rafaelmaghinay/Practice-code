#finds minimum and maximum value in a list

myList = [4, 5, -3, 6 ,1, 10, -15, 25, 15, 3 ]

def maximum():
    max = float('-inf')
    min = float('inf')
    
    for i in myList:
        if max < i:
            max = i
            
    return max

def minimum():
    min = float('inf')
    
    for i in myList:
        if min > i:
            min = i
            
    return min
    

print(f"max is {maximum()}")
print(f"min is {minimum()}")