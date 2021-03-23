
def max_subarray_sum (lista, sum):

    contm = 0
    numm = 0
    while contm < len(lista):

        cont = contm 
        num = lista[contm]
        
        while cont < (contm + sum -1):

            if contm + sum > len(lista) - 1:
                
                break

            num += lista[cont + 1]
            cont += 1
 

        if numm < num:
            numm = num
        
        contm += 1

    print (numm)

max_subarray_sum ([1, 2, 5, 2, 8, 1, 5], 2)
max_subarray_sum ([1, 2, 5, 2, 8, 1, 5], 4)
max_subarray_sum ([4, 2, 1, 6], 1)
max_subarray_sum ([4, 2, 1, 6, 2], 4)
max_subarray_sum ([], 4)
