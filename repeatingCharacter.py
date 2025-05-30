#returns the first non-repeating character in a string

s1="So this is a string"

def firstNonRepeatChar():
    myList = []
    
    for i in s1.lower():
        if i not in myList:
            myList.append(i)
        
        else:
            myList.remove(i)
            break
        
    if len(myList) != 0:
        return myList[0]
    else:
        return 0


if firstNonRepeatChar() != 0:
    print(firstNonRepeatChar())
else:
    print("Didn't find any non-repeating characters")
    
    