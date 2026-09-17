zenbakia = int(input("Eman zenbaki bat "))
def karratua(zenbakia) :
    zenbakia  = zenbakia ** 2 
    return zenbakia 


def da_bikoitia(zenbaki) : 
   
    if zenbaki % 2 == 0 :
        return   True
    else :
        return False
print(karratua(zenbakia))
print(da_bikoitia(zenbakia))

