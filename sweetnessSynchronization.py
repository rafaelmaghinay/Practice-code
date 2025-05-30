#find highest sweetness level and match everything
#n =  number of advanced candy-making machines

def findHighest(settings):
    #initialized as the least current number to find the next highest number
    current = 0
    for i in settings:
        if i > current:
            current = i

    return current

def match(n, highest):
    newSettings = []
    
    for i in range(n):
        newSettings.append(highest)
        
    return newSettings

settings= [4,6,3,7,2]
print(settings)
print(match(len(settings), findHighest(settings)))