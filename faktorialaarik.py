def potentzia(a ,b ) :
    if b == 0 :
        return 1 
    else :  
        return a * potentzia(a, b-1)
print(potentzia(6, 2)) 

