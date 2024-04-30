def ambil_tiga_terbesar(nilai):
    # Menggunakan fungsi sorted() untuk mengurutkan nilai dari terbesar ke terkecil
    urutan = sorted(nilai, reverse=True)
    # Mengambil tiga nilai terbesar dari daftar yang telah diurutkan
    tiga_nilai = urutan[:3]
    return tiga_nilai

# Contoh penggunaan fungsi dengan list nilai yang diberikan
nilai = [1, 5, 2, 3, 4, 21, 9, 8, 7]
tiga_nilai_terbesar = ambil_tiga_terbesar(nilai)
# Mencetak tiga nilai terbesar
print("Tiga nilai terbesar:", tiga_nilai_terbesar)