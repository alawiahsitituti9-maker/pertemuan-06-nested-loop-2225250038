# Pertemuan 06 Nested Loop Python

## Identitas

**Nama :** Siti Tuti Alawiah
**NIM  :** 2225250038
**Kelas:** 3F

---

## Tujuan

Pada Pertemuan 06, tujuan pembelajaran adalah:

1. Memahami konsep nested loop.
2. Membentuk pola menggunakan nested loop.
3. Menggunakan akumulasi untuk menghitung jumlah.
4. Menggunakan pencacahan atau counter untuk menghitung banyak kejadian.
5. Menelusuri nilai variabel `i` dan `j`.
6. Menguji program Python menggunakan VS Code.

---

## Struktur Folder

```text
pertemuan-06-nested-loop-NIM/
│
├── README.md
├── .gitignore
│
├── latihan/
│   ├── 01_pasangan_indeks.py
│   ├── 02_pola_segitiga.py
│   ├── 03_jumlah_per_baris.py
│   └── 04_hitung_pasangan.py
│
└── tugas/
    └── tabel_perkalian_dan_statistik.py
```

---

## Latihan

### 1. Pasangan Indeks

Program menampilkan seluruh pasangan `(i, j)` dengan:

* `i = 1 sampai 3`
* `j = 1 sampai 4`

Program juga menghitung banyak pasangan yang dihasilkan.

Jumlah pasangan:

```text
3 × 4 = 12
```

---

### 2. Pola Segitiga

Program menerima nilai `n`, kemudian membuat pola bintang.

Contoh untuk:

```text
n = 5
```

Hasil:

```text
*
* *
* * *
* * * *
* * * * *
```

Loop luar digunakan untuk menentukan baris, sedangkan loop dalam menentukan jumlah bintang pada setiap baris.

---

### 3. Jumlah Per Baris

Program menghitung nilai `i * j` untuk:

```text
i = 1 sampai 4
j = 1 sampai 3
```

Hasil:

```text
Jumlah baris 1 = 6
Jumlah baris 2 = 12
Jumlah baris 3 = 18
Jumlah baris 4 = 24
```

Variabel `total_baris` direset pada setiap awal iterasi loop luar.

---

### 4. Menghitung Pasangan

Program menghitung banyak pasangan `(i, j)` yang memenuhi:

```text
i + j <= n
```

Nilai `n` dimasukkan oleh pengguna.

Test case yang digunakan:

```text
n = 2
n = 3
n = 5
```

---

# Tugas 3: Tabel Perkalian dan Statistik

## Deskripsi

Program menerima bilangan bulat positif `n`.

Program kemudian:

1. Membentuk tabel perkalian dari `1` sampai `n`.
2. Menghitung jumlah setiap baris.
3. Menghitung total seluruh hasil perkalian.
4. Menghitung banyak hasil perkalian yang genap.
5. Menampilkan hasil statistik setelah tabel selesai.

---

## Algoritma Tugas 3

1. Memasukkan nilai `n`.
2. Memeriksa apakah `n` merupakan bilangan positif.
3. Jika `n <= 0`, pengguna diminta memasukkan `n` kembali.
4. Membuat `total_semua = 0`.
5. Membuat `count_genap = 0`.
6. Menjalankan loop luar dari `1` sampai `n`.
7. Pada setiap baris, membuat `total_baris = 0`.
8. Menjalankan loop dalam dari `1` sampai `n`.
9. Menghitung `hasil = i * j`.
10. Menambahkan `hasil` ke `total_baris`.
11. Menambahkan `hasil` ke `total_semua`.
12. Jika `hasil` genap, `count_genap` ditambah `1`.
13. Setelah loop dalam selesai, menampilkan jumlah baris.
14. Setelah semua loop selesai, menampilkan total keseluruhan dan banyak hasil genap.

---

## Peran Variabel

| Variabel      | Fungsi                                       |
| ------------- | -------------------------------------------- |
| `n`           | Menentukan ukuran tabel                      |
| `i`           | Mengatur baris pada loop luar                |
| `j`           | Mengatur kolom pada loop dalam               |
| `hasil`       | Menyimpan hasil `i * j`                      |
| `total_baris` | Menghitung jumlah hasil pada setiap baris    |
| `total_semua` | Menghitung jumlah seluruh hasil perkalian    |
| `count_genap` | Menghitung banyak hasil perkalian yang genap |

---

## Cara Menjalankan

Jalankan program Tugas 3 melalui terminal VS Code:

```bash
python tugas/tabel_perkalian_dan_statistik.py
```

Jika menggunakan `python3`:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

---

## Hasil Pengujian

### Test Case 1

Input:

```text
n = 1
```

Hasil yang diharapkan:

```text
Jumlah pasangan = 1
Total semua = 1
Banyak hasil genap = 0
```

### Test Case 2

Input:

```text
n = 2
```

Hasil yang diharapkan:

```text
Total semua = 9
Banyak hasil genap = 3
```

### Test Case 3

Input:

```text
n = 3
```

Hasil yang diharapkan:

```text
Total semua = 36
Banyak hasil genap = 5
```

---

## Analisis Efisiensi

Jika nilai `n` digunakan untuk membuat tabel `n × n`, maka loop dalam dijalankan sebanyak:

```text
n × n = n²
```

kali.

Contoh:

```text
n = 3
3 × 3 = 9 iterasi
```

```text
n = 5
5 × 5 = 25 iterasi
```

Semakin besar nilai `n`, semakin banyak proses yang dilakukan oleh nested loop.

---

## Kesimpulan

Nested loop digunakan untuk memproses data dalam bentuk baris dan kolom. Loop luar mengatur baris, sedangkan loop dalam mengatur kolom.

Akumulator `total_baris` digunakan untuk menghitung jumlah pada setiap baris, sedangkan `total_semua` digunakan untuk menghitung seluruh hasil perkalian.

Counter `count_genap` digunakan untuk menghitung banyak hasil perkalian yang memenuhi kondisi genap.

---

## Refleksi

Kesalahan yang perlu diperhatikan dalam nested loop adalah posisi indentasi dan lokasi inisialisasi variabel.

`total_baris` harus direset pada setiap baris karena digunakan untuk menghitung jumlah masing-masing baris. Sementara itu, `total_semua` tidak boleh direset pada setiap baris karena digunakan untuk menghitung jumlah keseluruhan.

Dengan menggunakan tracing terhadap `i` dan `j`, alur nested loop dapat lebih mudah dipahami dan kesalahan logika dapat ditemukan.

---

## GitHub

Perintah Git yang digunakan:

```bash
git init
git add .
git commit -m "feat: menambahkan latihan nested loop pertemuan 06"
git branch -M main
git remote add origin https://github.com/USERNAME/pertemuan-06-nested-loop-NIM.git
git push -u origin main
```

Commit berikutnya:

```bash
git add latihan
git commit -m "feat: menyelesaikan latihan pola dan nested loop"

git add tugas/tabel_perkalian_dan_statistik.py
git commit -m "feat: menyelesaikan tugas 3 akumulasi dan pencacahan"

git add README.md
git commit -m "docs: menambahkan hasil uji analisis dan refleksi"

git push
```

---

## Status

* [x] Latihan nested loop
* [x] Pola segitiga
* [x] Akumulasi per baris
* [x] Pencacahan pasangan
* [x] Tugas 3
* [x] README.md
* [ ] Push ke GitHub
