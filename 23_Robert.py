import tkinter as tk
from tkinter import ttk

data_siswa = []

def ke_Layar(frame):
    if frame == halaman2:
        tampilkan_data()
    frame.tkraise()

def simpan_data():
    nama = entry_nama.get()
    kelas = entry_kelas.get()
    alamat = entry_alamat.get()

    if nama and kelas and alamat:
        data_siswa.append({"nama": nama, "kelas": kelas, "alamat": alamat})
        entry_nama.delete(0, tk.END)
        entry_kelas.delete(0, tk.END)
        entry_alamat.delete(0, tk.END)
        label_status.config(text="Data berhasil disimpan!", foreground="#2e8b57")
    else:
        label_status.config(text="Semua kolom harus diisi!", foreground="red")

def tampilkan_data():
    for i in tree.get_children():
        tree.delete(i)
    if data_siswa:
        for i in range(len(data_siswa)):
            s = data_siswa[i]
            tree.insert("", tk.END, values=(str(i+1), s["nama"], s["kelas"], s["alamat"]))
    else:
        tree.insert("", tk.END, values=("-", "Belum ada data", "-", "-"))

def cari_data():
    keyword = entry_cari.get().lower()
    for i in tree_cari.get_children():
        tree_cari.delete(i)
    hasil = [s for s in data_siswa if keyword in s["nama"].lower()]
    if hasil:
        for s in hasil:
            tree_cari.insert("", tk.END, values=(s["nama"], s["kelas"], s["alamat"]))
    else:
        tree_cari.insert("", tk.END, values=("Data tidak ditemukan", "-", "-"))

window = tk.Tk()
window.title("Aplikasi Data Peserta Didik A1")
window.geometry("850x400")
window.configure(bg="#fced90")

style = ttk.Style()
style.theme_use("clam")
style.configure("TFrame", background="#fced90")
style.configure("TLabel", background="#fced90", font=("Segoe UI", 10))
style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=5)
style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background="#4682b4", foreground="white")
style.configure("Treeview", background="#fafafa", fieldbackground="#fafafa", foreground="black")

halaman1 = ttk.Frame(window)
halaman2 = ttk.Frame(window)
halaman3 = ttk.Frame(window)

for frame in (halaman1, halaman2, halaman3):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# === Halaman 1: Tambah Data ===
judul1 = ttk.Label(halaman1, text="Form Tambah Data Peserta Didik A1", font=("Segoe UI", 14, "bold"), anchor="center")
judul1.pack(pady=10)

ttk.Label(halaman1, text="Nama:", font=("Courier New", 14)).pack(pady=3)
entry_nama = ttk.Entry(halaman1, width=35)
entry_nama.pack()

ttk.Label(halaman1, text="Kelas:", font=("Courier New", 14)).pack(pady=3)
entry_kelas = ttk.Entry(halaman1, width=35)
entry_kelas.pack()

ttk.Label(halaman1, text="Alamat:", font=("Courier New", 14)).pack(pady=3)
entry_alamat = ttk.Entry(halaman1, width=35)
entry_alamat.pack()

ttk.Button(halaman1, text="Simpan Data", command=simpan_data).pack(pady=20)
label_status = ttk.Label(halaman1, text="", font=("Segoe UI", 9))
label_status.pack()

frame_tombol = ttk.Frame(halaman1)
frame_tombol.pack()
ttk.Button(frame_tombol, text="Lihat Data", command=lambda:ke_Layar(halaman2)).grid(row=0, column=0, padx=5)
ttk.Button(frame_tombol, text="Cari Data", command=lambda:ke_Layar(halaman3)).grid(row=0, column=1, padx=5)

# === Halaman 2: Lihat Data ===
judul2 = ttk.Label(halaman2, text="Daftar Data Peserta Didik A1", font=("Segoe UI", 14, "bold"))
judul2.pack(pady=10)

kolom = ("No", "Nama", "Kelas", "Alamat")
tree = ttk.Treeview(halaman2, columns=kolom, show="headings", height=10)
for kol in kolom:
    tree.heading(kol, text=kol)

tree.column("No", width=50, anchor="center")
tree.column("Nama", width=200, anchor="w")
tree.column("Kelas", width=100, anchor="center")
tree.column("Alamat", width=300, anchor="w")
tree.pack(pady=5)

ttk.Button(halaman2, text="Kembali", command=lambda:ke_Layar(halaman1)).pack(pady=10)

# === Halaman 3: Cari Data ===
judul3 = ttk.Label(halaman3, text="Cari Data Siswa", font=("Segoe UI", 14, "bold"))
judul3.pack(pady=10)

ttk.Label(halaman3, text="Masukkan Nama:").pack(pady=3)
entry_cari = ttk.Entry(halaman3, width=35)
entry_cari.pack(pady=5)
ttk.Button(halaman3, text="Cari", command=cari_data).pack(pady=5)

kolom_cari = ("Nama", "Kelas", "Alamat")
tree_cari = ttk.Treeview(halaman3, columns=kolom_cari, show="headings", height=8)
for kolom in kolom_cari:
    tree_cari.heading(kolom, text=kolom)
tree_cari.pack(pady=5)

ttk.Button(halaman3, text="Kembali", command=lambda:ke_Layar(halaman1)).pack(pady=10)

halaman1.tkraise()
window.mainloop()