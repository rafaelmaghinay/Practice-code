#reverses a string

sentence="Hello, World!"

def stringRev():
    newString = ""
    j = len(sentence) - 1
    
    #concatenates the last index of sentence to newString
    for i in sentence:
        newString = newString + sentence[j]
        j-=1
        
    return newString

print(stringRev())