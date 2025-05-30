""""
Python code to check if two strings are anagrams of eachother
using a dictionary
"""

def areAnagrams(s1,s2):
    
    #create a hashmap to store character frequencies
    charCount = {}
    
    #Count frequency of each character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
        
    #Count frequency of each character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
        
    #check if all frequencies are 0
    for value in charCount.values():
        if value != 0:
            return False
        
    #if all conditions are satisfied, they are anagrams
    return True


if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")
    
    