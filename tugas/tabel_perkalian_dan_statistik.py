# Tugas 3: Tabel Perkalian dan Statistik

print("Tabel Perkalian dan Statistik")

# Input n
n = int(input("n: "))

# Validasi agar n harus positif
while n <= 0:
    print("n harus positif.")
    n = int(input("n: "))

# Akumulator total keseluruhan
total_semua = 0

# Counter untuk menghitung hasil genap
count_genap = 0

# Nested loop
for i in range(1, n + 1):

    # Jumlah untuk setiap baris
    total_baris = 0

    for j in range(1, n + 1):

        # Menghitung hasil perkalian
        hasil = i * j

        # Menampilkan tabel
        print(f"{hasil:4}", end="")

        # Akumulasi jumlah per baris
        total_baris += hasil

        # Akumulasi jumlah keseluruhan
        total_semua += hasil

        # Menghitung banyak hasil genap
        if hasil % 2 == 0:
            count_genap += 1

    # Menampilkan jumlah setiap baris
    print(f"   | jumlah baris = {total_baris}")

# Menampilkan hasil akhir
print(f"Total seluruh hasil = {total_semua}")
print(f"Banyak hasil genap = {count_genap}")