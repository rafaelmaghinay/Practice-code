#counts vowels in a string

s1="This is a strIng, I dont wanna miss a thing"
vowels= ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def vowelCount():
    counter = 0
    
    for i in s1:
        if i in vowels:
            counter+=1
    
    return counter

print(f"your string has {vowelCount()} vowels")
    
    