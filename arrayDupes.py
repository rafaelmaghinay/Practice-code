#removing duplicates in an array/list

my_list = [1, 2, 2, 3, 4, 4, 4]

def dupeRemove():
    #creating a new list so that I wouldn't be able to use nested loops
    newList = []
    
    for i in my_list:
        if i not in newList:
            newList.append(i)
                
    return newList

print(dupeRemove())