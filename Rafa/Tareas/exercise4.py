
def procesar(lista):
    
    listap = []
    for x in range (len(lista)):
        cont = 0
        for p in range (1, lista[x] + 1):
            if lista[x]%p == 0:
                cont += 1
        if cont == 2:
            listap.append(lista[x])
    
    lpo = []
    lne = []
    cer = 0
    for x in range (len(lista)):
        if lista[x] > 0:
            lpo.append(lista[x])
        if lista[x] == 0:
            cer += 1
        if lista[x] < 0:
            lne.append(lista[x])
    
    promp = 0
    for x in range (len(lpo)):
        promp += lpo[x]
    promp = promp/len(lpo)

    promn = 0
    for x in range (len(lne)):
        promn += lne[x]
    promn = promn/len(lne)

    listaf = [promp, promn, cer, listap]
    print (listaf)

procesar ([-5, 3, 0, 7, 14, -6, 3, 0, -2, 3, 8])
procesar ([2, 0, 0, 1, -4, -3, 0, 5, 11, -7, 9])
