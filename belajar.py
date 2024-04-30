nilai_ujian = [80,75,70,90,81,84,92,71,65,80,70]
nama_pahlawan = ['Soekarno', 'Diponegoro', 'Jend. Sudirman', 'Cut Nya Dhien']
nilai_campuran = ['Javascript', 20,34.4, True]
list_dalam_list = [23,[22,20], 45]
print(nilai_ujian)
print(nama_pahlawan)
print(nilai_campuran)
print(list_dalam_list)

data = [10,20,30,40]
data[0]= 50
print(data)

nama = 'Yohanes Nevan'
nama[0] = 'A'
print(nama)

bil1 = [1,2,3,4]
bil2 = [5,6,7]
bil_total = bil1 + bil2
print(bil_total)

bil1 = [1,2,3,4]
bil_total = [1,2,3,4] * 2
print(bil_total)

nama = ["Naruto","Luffy","Ichigo","Goku"]
print(nama)
print(nama[0])
print(nama[3])
#indeks akses dihitung dari belakang
print(nama[-2])
print(nama[-1])

nama = ['yan', 'roy', 'fang', 'rizz']
nama.append(['ram', 'lak'])
print(nama)

nama = ['yan', 'roy', 'fang', 'rizz','mar']
nama.extend(["klok","tji"])
print(nama)

nama = ['yan', 'roy', 'fang', 'rizz','mar']
nama.sort()
print(nama)


list_nilai = ["Asep", 100, True]
print(f"Nama: {list_nilai[0]}, nilai: {list_nilai[1]}")
#ganti nilai
list_nilai[0] = "Dimas"
list_nilai[1]
print(f"Nama: {list_nilai[0]}, nilai: {list_nilai[1]}")

penambahan isi list
lista = [1,2,3,4]
listb = [4,5,6]
hasil = lista + listb
print(hasil)

lst = []
lst.append(1)
lst.append("satu")
lst.append("true")
print(lst)

lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = [7,8,9]

lst1.extend(lst2)
lst1.extend(lst3)
print(lst1)
print(lst1+lst2+lst3)

def extendcoba(lst1,lst2):
    lst1 = lst1+lst2
    return lst1
print(extendcoba(lst1,lst2))

lst1 = [1,2,3,23,56,6923,6,436,3,34]
lst1.sort()
lst2 = lst1[::-1]
print(lst2)

lst1 = [0,1,2,3,4,5]
lst1.pop(3)
print(lst1)

lst2 = lst1.copy()
del lst2[3]
print(lst2)

lst1 = [0,1,2,3,4,5]
terpop = lst1.pop(3)
print(lst1)
print(terpop)

lst2 = [0,1,2,3,4,5]
del lst2[3]
print(lst2)

lst1 = [1,2,3,4,5,3,7,5,3]
for i in range(lst1.count(3)):
    lst1.remove(3)
    
print(lst1)

lst1 = [1,2,3,4]
lst2 = lst1

print(lst1)
print(lst2)
print()

lst2[0] = 0
print(lst1)
print(lst2)

lst1 = []
for i in range(4):
    lst1.insert(0,1)
print(lst1)

lst1 = [1,2,3]
lst2 = lst1[::-1]
print(lst1)
print(lst2)

a ="ini ada14h string"
b = ["ini", "ada", 1,4, "string"]
print(id(a))

a = "tes"
print(id(a))

a ="ini ada14h string"
b = [1,2,3]
print(id(b))
b[0] = 100
print(id(b))

def nama_fungsi(paramenter):
    argument = ''''''
    
def hapus_index_pertama(list):
    return list[1:]

list1 = [1,2,3,4]
print(hapus_index_pertama(list1))

pass