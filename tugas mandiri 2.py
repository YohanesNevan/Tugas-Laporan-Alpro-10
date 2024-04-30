# Inisialisasi list untuk menyimpan masukan dari pengguna angka = [] # Meminta masukan dari pengguna while True: masukan = input("Masukkan angka (ketik 'done' untuk selesai): ") # Jika pengguna memasukkan 'done', keluar dari loop if masukan.lower() == 'done': break # Coba ubah masukan pengguna menjadi angka dan tambahkan ke dalam list 'angka' try: angka.append(float(masukan)) except ValueError: print("Masukan tidak valid. Harap masukkan angka atau 'done' untuk selesai.") # Jika tidak ada angka yang dimasukkan, tampilkan pesan if len(angka) == 0: print("Tidak ada angka yang dimasukkan.") else: # Menampilkan nilai maksimum dan minimum dari deretan angka yang dimasukkan pengguna nilai_max = max(angka) nilai_min = min(angka) print("Nilai maksimum:", nilai_max) print("Nilai minimum:", nilai_min)# Inisialisasi list untuk menyimpan masukan dari pengguna
angka = []

# Meminta masukan dari pengguna
while True:
    masukan = input("Masukkan angka (ketik 'done' untuk selesai): ")
    
    # Jika pengguna memasukkan 'done', keluar dari loop
    if masukan.lower() == 'done':
        break
    
    # Coba ubah masukan pengguna menjadi angka dan tambahkan ke dalam list 'angka'
    try:
        angka.append(float(masukan))
    except ValueError:
        print("Masukan tidak valid. Harap masukkan angka atau 'done' untuk selesai.")

# Jika tidak ada angka yang dimasukkan, tampilkan pesan
if len(angka) == 0:
    print("Tidak ada angka yang dimasukkan.")
else:
    # Menampilkan nilai maksimum dan minimum dari deretan angka yang dimasukkan pengguna
    nilai_max = max(angka)
    nilai_min = min(angka)
    print("Nilai maksimum:", nilai_max)
    print("Nilai minimum:", nilai_min)
