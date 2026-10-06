def faktoriala(n) :
    if n == 0 :
        return 1 
    else :  
        return n * faktoriala(n-1)
print(faktoriala(6)) 