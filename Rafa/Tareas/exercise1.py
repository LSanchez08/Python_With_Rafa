
anagrama1 = 'AWESOME'
List1 = list(anagrama1)
x = len(List1)

anagrama2 = 'AWESOM'
List2 = list(anagrama2)
y = len(List2)

List1.sort()
List2.sort()
print (List1)
print (List2)

if len(List1) == 0 and len(List2) == 0:
    print ('Es un anagrama')
else:
    if x != y:
        print ('Tu pendejada no es un anagrama')
    else:
        cont = 0

        while cont < x-1:
            
            if List1.pop() == List2.pop():
                cont += 1
            else:
                print ('Tu pendejada no es un anagrama')
                break
            if cont == x-1:
                print ('Es un anagrama')


