def elemen_sama(list1,list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

print(elemen_sama([1,2,3], [3,4,5]))