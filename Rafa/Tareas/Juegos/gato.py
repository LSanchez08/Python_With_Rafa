
#tablero de gato, numeros representan vacio, X representa jugador 1 y O representa jugador 2
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#Ciclo para registrar los movimientos de ambos jugadores
#movimientof representa la cantidad de movimientos
movimientof = 0
#ganador es una variable para determinar si hubo un empate o no
ganador = 0
while movimientof < 9:

    #Ciclo para guardar un movimiento valido del jugador 1
    movimiento1 = 0
    while movimiento1 == 0:

        #el jugador 1 ingresa donde sera su movimiento
        #impresión del tablero
        print (lista1[0:3])
        print (lista1[3:6])
        print (lista1[6:])
        casilla = int(input('¡Jugador 1! (X) ingresa la casilla en la que deseas posicionarte'))
        #se corrobora que el numero de casilla este dentro del parametro
        if casilla <= 0 or casilla > 9:
            print('El numero de la casilla es incorrecto, por favor ingrese un valor dentro del parametro en el tablero')
        else:
            #se guarda el movimiento del jugador 1
            if type(lista1[casilla -1]) == int:
                if casilla >= 1 and casilla <= 3:
                    lista1[casilla - 1] = 'X'
                    movimiento1 = 1
                    movimientof +=1
                else:
                    if casilla >= 4 and casilla <= 6:
                        lista1[casilla - 1] = 'X'
                        movimiento1 = 1
                        movimientof +=1
                    else:
                        if casilla >= 7 and casilla <= 9:
                            lista1[casilla - 1] = 'X'
                            movimiento1 = 1
                            movimientof +=1
                        else:
                            print ('la casilla ya esta ocupada intenta de nuevo')

            #corroboración del ganador
            #       123                                             456                                              789                                                147                                             258                                                 369                                             159                                                 357
            if (lista1[0] and lista1[1] and lista1[2]) == 'X' or (lista1[3] and lista1[4] and lista1[5]) == 'X' or (lista1[6] and lista1[7] and lista1[8]) == 'X' or (lista1[0] and lista1[3] and lista1[6]) == 'X' or (lista1[1] and lista1[4] and lista1[7]) == 'X' or (lista1[2] and lista1[5] and lista1[8]) == 'X' or (lista1[0] and lista1[4] and lista1[8]) == 'X' or (lista1[2] and lista1[4] and lista1[6]) == 'X':
                #impresión del tablero
                if (lista1[0] and lista1[4] and lista1[8]) == 'X':
                    print('blblblb1')
                
                if (lista1[6] and lista1[7] and lista1[8]) == 'X':
                    print('blblbl2')
                
                if (lista1[2] and lista1[5] and lista1[8]) == 'X':
                    print('bblblblb3')

                print (lista1[0:3])
                print (lista1[3:6])
                print (lista1[6:])
                print ('El jugador 1 ha ganado')
                movimientof = 9
                ganador = 1

    if ganador == 1:
        break

    #Ciclo para guardar un movimiento valido del jugador 2
    movimiento2 = 0
    while movimiento2 == 0:

        #el jugador 2 ingresa donde sera su movimiento
        #impresión del tablero
        print (lista1[0:3])
        print (lista1[3:6])
        print (lista1[6:])
        casilla = int(input('¡Jugador 2! (O) ingresa la casilla en la que deseas posicionarte'))
        #se corrobora que el numero de casilla este dentro del parametro
        if casilla <= 0 or casilla > 9:
            print('El numero de la casilla es incorrecto, por favor ingrese un valor dentro del parametro en el tablero')
        else:
            #se guarda el movimiento del jugador 2
            if type(lista1[casilla - 1]) == int:
                if casilla >= 1 and casilla <= 3:
                    lista1[casilla - 1] = 'O'
                    movimiento2 = 1
                    movimientof +=1
            else:
                print ('la casilla ya esta ocupada intenta de nuevo')

            if type(lista1[casilla - 1]) == int:
                if casilla >= 4 and casilla <= 6:
                    lista1[casilla - 1] = 'O'
                    movimiento2 = 1
                    movimientof +=1
            else:
                print ('la casilla ya esta ocupada intenta de nuevo')

            if type(lista1[casilla - 1]) == int:
                if casilla >= 7 and casilla <= 9:
                    lista1[casilla - 1] = 'O'
                    movimiento2 = 1
                    movimientof +=1
            else:
                print ('la casilla ya esta ocupada intenta de nuevo')

            #corroboración del ganador
            #       123                                             456                                              789                                                147                                             258                                                 369                                             159                                                 357
            if (lista1[0] and lista1[1] and lista1[2]) == 'O' or (lista1[3] and lista1[4] and lista1[5]) == 'O' or (lista1[6] and lista1[7] and lista1[8]) == 'O' or (lista1[0] and lista1[3] and lista1[6]) == 'O' or (lista1[1] and lista1[4] and lista1[7]) == 'O' or (lista1[2] and lista1[5] and lista1[8]) == 'O' or (lista1[0] and lista1[4] and lista1[8]) == 'O' or (lista1[2] and lista1[4] and lista1[6]) == 'O':
                #impresión del tablero
                print (lista1[0:3])
                print (lista1[3:6])
                print (lista1[6:])
                print ('El jugador 2 ha ganado')
                movimientof = 9
                ganador = 1
    if ganador == 1:
        break

if ganador == 0:
    print('El juego resulto en un empate')





#el jugador 1 ingresa donde sera su movimiento
        #impresión del tablero
        print (lista1[0:3])
        print (lista1[3:6])
        print (lista1[6:])
        casilla = int(input('¡Jugador 1! (X) ingresa la casilla en la que deseas posicionarte'))
        #se corrobora que el numero de casilla este dentro del parametro
        if casilla <= 0 or casilla > 9:
            print('El numero de la casilla es incorrecto, por favor ingrese un valor dentro del parametro en el tablero')
        else:
            #se guarda el movimiento del jugador 1
            if type(lista1[casilla -1]) == int:
                if casilla >= 1 and casilla <= 3:
                    lista1[casilla - 1] = 'X'
                    movimiento1 = 1
                    movimientof +=1
                else:
                    if casilla >= 4 and casilla <= 6:
                        lista1[casilla - 1] = 'X'
                        movimiento1 = 1
                        movimientof +=1
                    else:
                        if casilla >= 7 and casilla <= 9:
                            lista1[casilla - 1] = 'X'
                            movimiento1 = 1
                            movimientof +=1
                        else:
                            print ('la casilla ya esta ocupada intenta de nuevo')
            
            #corroboración del ganador
            #       123                                             456                                              789                                                147                                             258                                                 369                                             159                                                 357
            if (lista1[0] and lista1[1] and lista1[2]) == 'X' or (lista1[3] and lista1[4] and lista1[5]) == 'X' or (lista1[6] and lista1[7] and lista1[8]) == 'X' or (lista1[0] and lista1[3] and lista1[6]) == 'X' or (lista1[1] and lista1[4] and lista1[7]) == 'X' or (lista1[2] and lista1[5] and lista1[8]) == 'X' or (lista1[0] and lista1[4] and lista1[8]) == 'X' or (lista1[2] and lista1[4] and lista1[6]) == 'X':
                #impresión del tablero
                if (lista1[0] and lista1[4] and lista1[8]) == 'X':
                    print('blblblb1')
                
                if (lista1[6] and lista1[7] and lista1[8]) == 'X':
                    print('blblbl2')
                
                if (lista1[2] and lista1[5] and lista1[8]) == 'X':
                    print('bblblblb3')

                print (lista1[0:3])
                print (lista1[3:6])
                print (lista1[6:])
                print ('El jugador 1 ha ganado')
                movimientof = 9
                ganador = 1

    if ganador == 1:
        break