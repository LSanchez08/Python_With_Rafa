moveplayer = 0
movimientof = 0
jugador1 = 'X'
jugador2 = 'O'

def estado_actual (data):
    global moveplayer
    global movimientof
    global jugador1
    global jugador2

    if ((tablero[0] == tablero[1] and tablero[1] == tablero[2] and tablero[0] == jugador1) or (tablero[3] == tablero[4] and tablero[4] == tablero[5] and tablero[3] == jugador1) or (tablero[6] == tablero[7] and tablero[7] == tablero[8] and tablero[6] == jugador1)) or ((tablero[0] == tablero[1] and tablero[1] == tablero[2] and tablero[0] == jugador2) or (tablero[3] == tablero[4] and tablero[4] == tablero[5] and tablero[3] == jugador2) or (tablero[6] == tablero[7] and tablero[7] == tablero[8] and tablero[6] == jugador2)):
        print(f'El jugador {moveplayer} ¡Gano!')
        movimientof = 9
        print('primera')
        print (tablero[0:3])
        print (tablero[3:6])
        print (tablero[6:])
        return

    elif ((tablero[0] == tablero[3] and tablero[3] == tablero[6] and tablero[0] == jugador1) or (tablero[1] == tablero[4] and tablero[4] == tablero[7] and tablero[1] == jugador1) or (tablero[2] == tablero[5] and tablero[5] == tablero[8] and tablero[2] == jugador1)) or ((tablero[0] == tablero[3] and tablero[3] == tablero[6] and tablero[0] == jugador2) or (tablero[1] == tablero[4] and tablero[4] == tablero[7] and tablero[1] == jugador2) or (tablero[2] == tablero[5] and tablero[5] == tablero[8] and tablero[2] == jugador2)):
        print (f'El jugador {moveplayer} ¡Gano!')
        movimientof = 9
        print('segunda')
        print (tablero[0:3])
        print (tablero[3:6])
        print (tablero[6:])
        return

    elif ((tablero[0] == tablero[4] and tablero[4] == tablero[8] and tablero[0] == jugador1) or (tablero[2] == tablero[4] and tablero[4] == tablero[6] and tablero[2] == jugador1)) or ((tablero[0] == tablero[4] and tablero[4] == tablero[8] and tablero[0] == jugador2) or (tablero[2] == tablero[4] and tablero[4] == tablero[6] and tablero[2] == jugador2)):
        print (f'El jugador {moveplayer}¡Gano!')
        movimientof = 9
        print('tercera')
        print (tablero[0:3])
        print (tablero[3:6])
        print (tablero[6:])
        return
    elif movimientof == 9:
        print('Empate')
        print (tablero[0:3])
        print (tablero[3:6])
        print (tablero[6:])
        return
    else:
        print(f'Siguiente, Jugador!')
        movimientof += 1
        if moveplayer == 2:
            moveplayer = 0
            return

tablero = [1, 2, 3, 4, 5, 6, 7, 8, 9]

while movimientof < 9:

    while moveplayer == 0:
        if movimientof == 9:
            break

        print (tablero[0:3])
        print (tablero[3:6])
        print (tablero[6:])
        casilla = int(input('¡Jugador 1! (X) ingresa la casilla en la que deseas posicionarte '))

        if casilla <= 0 or casilla > 9:
            print('El numero de la casilla es incorrecto, por favor ingrese un valor dentro del parametro en el tablero')
        else:

            if type(tablero[casilla -1]) == int:
                if casilla >= 1 and casilla <= 3:
                    tablero[casilla - 1] = 'X'
                    moveplayer = 1
                else:
                    if casilla >= 4 and casilla <= 6:
                        tablero[casilla - 1] = 'X'
                        moveplayer = 1
                    else:
                        if casilla >= 7 and casilla <= 9:
                            tablero[casilla - 1] = 'X'
                            moveplayer = 1
                estado_actual(tablero)
                print(moveplayer)
                
            else:
                print ('la casilla ya esta ocupada intenta de nuevo')

    while moveplayer == 1:
        if movimientof == 9:
            break

        print (tablero[0:3])
        print (tablero[3:6])
        print (tablero[6:])
        casilla = int(input('¡Jugador 2! (X) ingresa la casilla en la que deseas posicionarte '))

        if casilla <= 0 or casilla > 9:
            print('El numero de la casilla es incorrecto, por favor ingrese un valor dentro del parametro en el tablero')
        else:

            if type(tablero[casilla -1]) == int:
                if casilla >= 1 and casilla <= 3:
                    tablero[casilla - 1] = 'O'
                    moveplayer = 2
                else:
                    if casilla >= 4 and casilla <= 6:
                        tablero[casilla - 1] = 'O'
                        moveplayer = 2
                    else:
                        if casilla >= 7 and casilla <= 9:
                            tablero[casilla - 1] = 'O'
                            moveplayer = 2
                estado_actual(tablero)
                print(moveplayer)
                
            else:
                print ('la casilla ya esta ocupada intenta de nuevo')