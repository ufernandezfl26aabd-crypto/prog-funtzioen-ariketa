
n = int(input("Eman zenbaki bat "))
def lehena_da (zenbakia) :
    if zenbakia %  2: 
        return False

    for zenbakia in (n,n *2 ):
        if lehena_da(zenbakia) :
            return False



        lehena = False


    if  lehena :
        print("lehena da ") 
    else :
        print("Ez da lehena ") 

