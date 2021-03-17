
def Anagram(data, data2):
    List = list(data)
    List2 = list(data2)

    List.sort()
    List2.sort()

    if List == List2:
        return True
    else:
        return False


print(Anagram('', ''))
print(Anagram('aaz', 'zza'))
print(Anagram('anagram', 'nagaram'))
print(Anagram('rat', 'car'))
print(Anagram('awesome', 'awesom'))
print(Anagram('qwerty', 'qeywrt'))
print(Anagram('texttwisttime', 'timetwisttext'))
