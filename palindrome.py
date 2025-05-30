#checks if a sentence is a palindrome

s1="A man, a plan, a canal, Panama"


def palCheck():
    sentence = s1.lower().replace(" ", "").replace(",","")  #removes all unnecessary spaces and special letters
    j = len(sentence) - 1 
    
    
    for i in sentence:
        if i is not sentence[j]:
            return False
        j-=1
        
    return True

if palCheck():
    print("the sentence is a palindrome")
else:
    print("the sentence is not a palindrome")