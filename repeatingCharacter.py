#returns the first non-repeating character in a string

s1="so this is a string"

def firstNonRepeatChar():
    myList = []
    
    for i in s1:
        if i not in myList:
            myList.append(i)
        
        else:
            myList.remove(i)
            break
        
    return myList[0]

print(firstNonRepeatChar())
    
    