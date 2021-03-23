
def SubArray(data, value):
    final = 0
    for x in range(len(data) - value + 1):
        current = 0
        for y in range(value):
            current += data[x + y]
        if current > final:
            final = current
    if final == 0:
        return None
    return final

print(SubArray([1, 2, 5, 2, 8, 1, 5], 2))
print(SubArray([1, 2, 5, 2, 8, 1, 5], 4))
print(SubArray([4, 2, 1, 6], 1))
print(SubArray([4, 2, 1, 6, 1], 4))
print(SubArray([0], 4))