zenbakia = int(input("zenbaki bat eman "))

bikoitza = zenbakia * 2

aurkitua = False
iteratzailea = zenbakia + 1

while (not aurkitua ) and (iteratzailea < bikoitza ) :
    if iteratzailea % 10 == 0 :
        aurkitua = True

    iteratzailea += 1 

if aurkitua :
    print("Aurkitu dut")
else :
    print("Ez dut aurkitu")
