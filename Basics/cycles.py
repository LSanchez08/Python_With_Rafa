
print('*********************************************************')
if (4 < 5):
    print(True)
else:
    print(False)

if (4 > 5):
    print(True)
else:
    print(False)

a = 10
b = 5

if (a + b == 3):
    print(1)
elif (a + b == 15):
    print(0)
else:
    print(-1)

print('*********************************************************')

cont = 0
while (cont < 10):
    cont += 1

    print(cont)

cont = 0
while (cont < 10):
    cont += 1
    if (cont == 5):
        continue

    print(cont)

cont = 0
while cont < 10:
    cont += 1
    if (cont == 5):
        break
    
    print(cont)

print('*********************************************************')

for i in range(10):
    print(i)

