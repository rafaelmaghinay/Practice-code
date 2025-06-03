#finds missing ingredients between 1 and n, given a list

def isMissing(N, M, ingredients):
    missingIng  = []
    if N > 1000 and N < 1:
        return False
    
    y = N - M
    
    
    for i in range(1, N):
        if i not in ingredients:
            missingIng.append(i)
            
    return missingIng


N = 20
ingredients = [1,2,4,7,8,10,11,15,16,18]
print(isMissing(N, len(ingredients), ingredients))
