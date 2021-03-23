
def Procesar(data):
    valuePos = []
    valueNeg = []
    zeroCount = 0
    primeList = []
    for e in data:
        cont = 0
        if e > 0:
            valuePos.append(e)
        if e < 0:
            valueNeg.append(e)
        if e == 0:
            zeroCount += 1
        for i in range(1, e + 1):
            if e % i == 0:
                cont += 1
        if cont == 2:
            primeList.append(e)

    return [sum(valuePos)/len(valuePos), sum(valueNeg)/len(valueNeg), zeroCount, primeList]



print(Procesar([-5, 3, 0, 7, 14, -6, 3, 0, -2, 3, 8]))
print(Procesar([2, 0, 0, 1, -4, -3, 0, 5, 11, -7, 9]))
