
cont = 0

# def fibonacciNormal(data):
#     cont = 0
#     List = []
#     for i in range(data + 1):
#         cont += 1
#         if i == 0 or i == 1:
#             List.append(1)
#         elif i >= 2:
#             List.append(List[i-2] + List[i - 1])
#     print(cont)
#     return List

# print(fibonacciNormal(15))

def fibonacciRecursive(data):
    global cont
    cont += 1
    if data == 0 or data == 1:
        return 1
    
    return fibonacciRecursive(data -2) + fibonacciRecursive(data - 1)

print(fibonacciRecursive(15))
print(cont)

List = [1, 1]
cont = 0

def fibonacciDynamic(data):
    global List
    global cont
    cont += 1

    if len(List) == data:
        List.append(List[-1] + List[-2])

    if data == 0 or data == 1:
        return 1

    if len(List) > data:
        return List[data - 2] + List[data - 1]

    return fibonacciDynamic(data - 2) + fibonacciDynamic(data - 1)


def fibonacciD(data):
    return fibonacciDynamic(data)


print(fibonacciD(15))
print(cont)




