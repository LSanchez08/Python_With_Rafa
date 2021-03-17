
print('*********************************************************')
if 4 < 5:
    print(True)
else:
    print(False)

if (4 > 5):
    print(True)
else:
    print(False)

a = 10
b = 5

if a + b == 3:
    print(1)
elif (a + b == 15):
    print(0)
else:
    print(-1)

print('*********************************************************')

cont = 0
while cont < 10:
    cont += 1

    print(cont)

cont = 0
while cont < 10:
    cont += 1
    if cont == 5:
        continue

    print(cont)

cont = 0
while cont < 10:
    cont += 1
    if cont == 5:
        break
    
    print(cont)

print('*********************************************************')

for i in range(10):
    print(i)

print("----------------------------")

for i in range(5, 10):
    print(i)

print("----------------------------")

for i in range(0, 10, 2):
    print(i)

print("----------------------------")

for i in range(10, 0, -1):
    print(i)

print('*********************************************************')

List = [1,2,3,4,5]

for x in List:
    print(x)
    # print(List.index(x))


print('*********************************************************')
a = 100

b = 0

try:
    print(a * b)
except:
    print('error')


try:
    print(a/b)
except:
    print('error')
