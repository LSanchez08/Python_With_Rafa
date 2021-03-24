import os

emptyTic = [['', '', ''],['', '', ''],['', '', '']]
player = 1

def SelectPosition(place):
    data = -1
    while data < 1 or data > 3:
        data = int(input(f'Select the {place}: '))
        if data < 1 or data > 3:
            print('Not an accepted value')
    
    return data - 1

def VerifyPosition(row, column, value):
    if emptyTic[row][column] == '':
        emptyTic[row][column] = value
        return True
    else:
        print('Position already filled')
        return False
    
def PrintTic():
    for row in emptyTic:
        print(f'{row[0]} | {row[1]} | {row[2]}')
        print('-------')

def Verify(player):

    for e in emptyTic:
        if (e[0] == e[1] and e[1] == e[2]) and e[0] != '':
            if player == 1:
                return 'Player 1 wins!'
            else:
                return 'Player 2 wins!'
        
    for i in range(0, len(emptyTic)):
        if (emptyTic[0][i] == emptyTic[1][i] and emptyTic[1][i] == emptyTic[2][i]) and emptyTic[0][i] != '':
            if player == 1:
                return 'Player 1 wins!'
            else:
                return 'Player 2 wins!'

    if emptyTic[0][0] == emptyTic[1][1] and emptyTic[1][1] == emptyTic[2][2] and emptyTic[0][0] != '':
        if player == 1:
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'

    if emptyTic[0][2] == emptyTic[1][1] and emptyTic[1][1] == emptyTic[2][0] and emptyTic[0][2] != '':
        if player == 1:
            return 'Player 1 wins!'
        else:
            return 'Player 2 wins!'

    cont = 0

    for i in range(0, len(emptyTic)):
        for e in range(len(emptyTic[i])):
            if emptyTic[i][e] == '':
                cont += 1
    
    if cont == 0:
        return 'Draw!'

    
    return False
    

while True:
    bowl = False
    if player == 1:
        symbol = 'X'
    else:
        symbol = 'O'
    print(f'Current symbol: {symbol}')

    PrintTic()

    while not bowl:
        x = SelectPosition('row')
        y = SelectPosition("column")

        bowl = VerifyPosition(x, y, symbol)

    finish = Verify(player)

    if not finish:
        player *= -1
        os.system('cls')
        continue
    else:
        os.system('cls')
        print(finish)
        PrintTic()
        break
