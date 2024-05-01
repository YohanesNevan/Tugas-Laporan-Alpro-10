
buka = open("berita.txt", "r", encoding="utf-8")

bacabaris = buka.read()

pisah = bacabaris.split(".")

kataunik = []

for i in pisah:
    kata = i.strip().split()
    for j in kata:
        j = j.strip(".,?!\"';:-").lower()
        if j not in kataunik:
            kataunik.append(j)
        
print("======Isi Berita======")
print(bacabaris)

print("=======Kata Unik Pada Berita========")
print(kataunik)