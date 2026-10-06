def sekuentzia(a) : 
    if a == 1 :
        return 1
    elif a == 2 :
        return 2 
    else : 
        return sekuentzia(a-1) + sekuentzia(a-2)
print(sekuentzia(50)) 

