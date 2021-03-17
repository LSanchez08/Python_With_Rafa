
def CountUnique(data):
    return len(set(data))

print(CountUnique([1, 1, 1, 1, 1, 2]))
print(CountUnique([1, 2, 3, 4, 4, 4, 7, 7, 12, 12, 13]))
print(CountUnique([]))
print(CountUnique([-2, -1, -1, 0, 1]))
