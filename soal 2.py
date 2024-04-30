def terbesar_kedua(listnya):
    if len(listnya) < 2:
        return
    
    if len(listnya) == 2 and listnya[0] == listnya[1]:
        return
    
    listnya = list(set(listnya))
    listnya.sort()
    
    print(listnya)
    
    list2 = []
    for i in listnya:
        if i not in list2:
            list2.append(i)
    
    return list2[-2]

print(terbesar_kedua([1,5,3,2,6,9,8,9]))
print(terbesar_kedua([1,2]))
