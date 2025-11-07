# latihan_upload_project_dan_repository
Latihan project UI TKinter dan repository GitHub

Aplikasi Data Peserta Didik A1 adalah program berbasis **Python (Tkinter GUI)** yang digunakan untuk mengelola data siswa secara sederhana.
Aplikasi ini memiliki tiga halaman utama untuk menambah, menampilkan, dan mencari data siswa dengan antarmuka yang ramah pengguna.

# Fitur Utama

## Tambah Data Siswa
  Memasukkan nama, kelas, dan alamat siswa, kemudian menyimpannya ke dalam daftar data.

## Lihat Data Siswa
  Menampilkan seluruh data yang telah disimpan dalam bentuk tabel interaktif (Treeview).

## Cari Data Siswa
  Mencari data berdasarkan *nama siswa* dan menampilkan hasil pencarian dengan cepat.

## Navigasi Multi-Halaman
  Menggunakan sistem frame Tkinter untuk berpindah antar halaman tanpa menutup aplikasi.


# Tampilan Antarmuka

Aplikasi ini memiliki tampilan dengan warna latar lembut (`#fced90`) dan elemen modern menggunakan tema **"clam"** dari `ttk.Style`.


# 📦 Cara Menjalankan

1. Pastikan Python 3 sudah terinstal di perangkat Anda.

2. Simpan kode ini dalam file, misalnya `app_data_siswa.py`.

3. Jalankan aplikasi melalui terminal atau command prompt:

   ```bash
   python app_data_siswa.py
   ```

4. Aplikasi GUI akan muncul dan siap digunakan!

---

# 🗂️ Struktur Program

* **`halaman1`** — Form untuk menambah data siswa
* **`halaman2`** — Tabel daftar seluruh siswa
* **`halaman3`** — Fitur pencarian data siswa

Semua data sementara disimpan dalam list Python (`data_siswa`).
