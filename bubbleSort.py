# sorts a list from least to greatest using a bubble sort

myList = [4,3,1,2,6,5]

def bubbleSort():
    
    #sorts starting from the first index
    for n in myList:
        swapped=False
        
        for i in range(n + 1):
            if myList[i] > myList[i+1]:
                
                #swap
                myList[i], myList[i+1] = myList[i+1], myList[i]
                swapped = True
                
        if not swapped:
            break
        
    return myList
    
print(myList)
print(f"sorted list = {bubbleSort()}")