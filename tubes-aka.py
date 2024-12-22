import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import time
import matplotlib.pyplot as plt
import sys
import random

# Tingkatkan batas kedalaman rekursi
sys.setrecursionlimit(20000)


def buat_kamar():
    kamar = []
    for i in range(1, 101):
        status = "Kosong" if random.choice([True, False]) else "Terisi"
        kamar.append({
            "nomor_kamar": i,
            "tipe_kamar": random.choice(["Single", "Double", "Suite"]),
            "harga_kamar": random.randint(50000, 200000),
            "status": status
        })
    return kamar


def buat_penghuni():
    return []

# Algoritma iteratif untuk mencari kamar kosong


def cari_kamar_kosong_iteratif(kamar):
    return [k for k in kamar if k['status'] == "Kosong"]

# Algoritma rekursif untuk mencari kamar kosong


def cari_kamar_kosong_rekursif(kamar, index=0, hasil=None):
    if hasil is None:
        hasil = []
    if index >= len(kamar):
        return hasil
    if kamar[index]['status'] == "Kosong":
        hasil.append(kamar[index])
    return cari_kamar_kosong_rekursif(kamar, index + 1, hasil)

# Fungsi untuk mencari kamar kosong rekursif


def cari_kamar_rekursif():
    kamar_kosong = cari_kamar_kosong_rekursif(kamar)
    if kamar_kosong:
        tampilkan_tabel_kamar(kamar_kosong, "Kamar Kosong (Rekursif)")
    else:
        messagebox.showinfo(
            "Kamar Kosong", "Tidak ada kamar kosong yang tersedia.")

# Fungsi untuk mencari kamar kosong iteratif


def cari_kamar_iteratif():
    kamar_kosong = cari_kamar_kosong_iteratif(kamar)
    if kamar_kosong:
        tampilkan_tabel_kamar(kamar_kosong, "Kamar Kosong (Iteratif)")
    else:
        messagebox.showinfo(
            "Kamar Kosong", "Tidak ada kamar kosong yang tersedia.")

# Fungsi untuk analisis efisiensi algoritma


def analisis_efisiensi():
    ukuran_data = [10, 50, 100, 500, 1000, 5000, 10000]
    waktu_iteratif = []
    waktu_rekursif = []

    for ukuran in ukuran_data:
        data_dummy = [{"status": "Kosong" if i %
                       2 == 0 else "Terisi"} for i in range(ukuran)]

        # Analisis waktu iteratif
        mulai = time.time()
        cari_kamar_kosong_iteratif(data_dummy)
        waktu_iteratif.append(time.time() - mulai)

        # Analisis waktu rekursif
        mulai = time.time()
        cari_kamar_kosong_rekursif(data_dummy)
        waktu_rekursif.append(time.time() - mulai)

    # Plot hasil
    plt.figure(figsize=(10, 6))
    plt.plot(ukuran_data, waktu_iteratif, label="Iteratif", marker="o")
    plt.plot(ukuran_data, waktu_rekursif, label="Rekursif", marker="o")
    plt.title("Analisis Efisiensi Algoritma")
    plt.xlabel("Jumlah Data")
    plt.ylabel("Waktu (detik)")
    plt.legend()
    plt.grid()
    plt.show()

# Fungsi untuk menampilkan tabel kamar kosong


def tampilkan_tabel_kamar(kamar_list, judul):
    tabel_kamar_window = tk.Toplevel(root)
    tabel_kamar_window.title(judul)

    tree = ttk.Treeview(tabel_kamar_window, columns=(
        "Nomor", "Tipe", "Harga", "Status"), show="headings")
    tree.heading("Nomor", text="Nomor Kamar")
    tree.heading("Tipe", text="Tipe Kamar")
    tree.heading("Harga", text="Harga Kamar")
    tree.heading("Status", text="Status")

    for k in kamar_list:
        tree.insert("", "end", values=(
            k['nomor_kamar'], k['tipe_kamar'], k['harga_kamar'], k['status']))

    tree.pack(padx=10, pady=10)

# Fungsi untuk tambah kamar


def tambah_kamar():
    def simpan_kamar():
        try:
            nomor_kamar = int(entry_nomor_kamar.get())
            tipe_kamar = entry_tipe_kamar.get()
            harga_kamar = float(entry_harga_kamar.get())

            kamar.append({"nomor_kamar": nomor_kamar, "tipe_kamar": tipe_kamar,
                         "harga_kamar": harga_kamar, "status": "Kosong"})
            messagebox.showinfo("Sukses", "Kamar berhasil ditambahkan!")
            tambah_kamar_window.destroy()
        except Exception as e:
            messagebox.showerror("Kesalahan", f"Input tidak valid: {e}")

    tambah_kamar_window = tk.Toplevel(root)
    tambah_kamar_window.title("Tambah Kamar")

    tk.Label(tambah_kamar_window, text="Nomor Kamar:").grid(
        row=0, column=0, padx=10, pady=5)
    entry_nomor_kamar = tk.Entry(tambah_kamar_window)
    entry_nomor_kamar.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(tambah_kamar_window, text="Tipe Kamar:").grid(
        row=1, column=0, padx=10, pady=5)
    entry_tipe_kamar = tk.Entry(tambah_kamar_window)
    entry_tipe_kamar.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(tambah_kamar_window, text="Harga Kamar:").grid(
        row=2, column=0, padx=10, pady=5)
    entry_harga_kamar = tk.Entry(tambah_kamar_window)
    entry_harga_kamar.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(tambah_kamar_window, text="Simpan", command=simpan_kamar).grid(
        row=3, column=0, columnspan=2, pady=10)

# Fungsi untuk pesan kamar


def pesan_kamar():
    def simpan_pesanan():
        try:
            nama_pemesan = entry_nama_pemesan.get()
            durasi = int(entry_durasi.get())
            nomor_kamar = int(entry_nomor_kamar_pesanan.get())

            for k in kamar:
                if k['nomor_kamar'] == nomor_kamar and k['status'] == "Kosong":
                    penghuni.append(
                        {"nama": nama_pemesan, "nomor_kamar": nomor_kamar, "durasi": durasi, "status": "Menginap"})
                    k['status'] = "Terisi"
                    messagebox.showinfo("Sukses", "Pesanan berhasil disimpan!")
                    pesan_kamar_window.destroy()
                    return

            messagebox.showerror("Kesalahan", "Kamar tidak tersedia.")
        except Exception as e:
            messagebox.showerror("Kesalahan", f"Input tidak valid: {e}")

    pesan_kamar_window = tk.Toplevel(root)
    pesan_kamar_window.title("Pesan Kamar")

    tk.Label(pesan_kamar_window, text="Nama Pemesan:").grid(
        row=0, column=0, padx=10, pady=5)
    entry_nama_pemesan = tk.Entry(pesan_kamar_window)
    entry_nama_pemesan.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(pesan_kamar_window, text="Durasi Menginap (hari):").grid(
        row=1, column=0, padx=10, pady=5)
    entry_durasi = tk.Entry(pesan_kamar_window)
    entry_durasi.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(pesan_kamar_window, text="Nomor Kamar:").grid(
        row=2, column=0, padx=10, pady=5)
    entry_nomor_kamar_pesanan = tk.Entry(pesan_kamar_window)
    entry_nomor_kamar_pesanan.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(pesan_kamar_window, text="Simpan", command=simpan_pesanan).grid(
        row=3, column=0, columnspan=2, pady=10)

# Fungsi untuk menampilkan data kamar


def tampilkan_data_kamar():
    def hapus_kamar():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Kesalahan", "Pilih kamar untuk dihapus.")
            return
        nomor_kamar = tree.item(selected_item)['values'][0]
        for k in kamar:
            if k['nomor_kamar'] == nomor_kamar:
                kamar.remove(k)
                tree.delete(selected_item)
                messagebox.showinfo("Sukses", "Kamar berhasil dihapus.")
                return

    data_kamar_window = tk.Toplevel(root)
    data_kamar_window.title("Data Kamar")

    tree = ttk.Treeview(data_kamar_window, columns=(
        "Nomor", "Tipe", "Harga", "Status"), show="headings")
    tree.heading("Nomor", text="Nomor Kamar")
    tree.heading("Tipe", text="Tipe Kamar")
    tree.heading("Harga", text="Harga Kamar")
    tree.heading("Status", text="Status")

    for k in kamar:
        tree.insert("", "end", values=(
            k['nomor_kamar'], k['tipe_kamar'], k['harga_kamar'], k['status']))

    tree.pack(padx=10, pady=10)

    tk.Button(data_kamar_window, text="Hapus Kamar",
              command=hapus_kamar).pack(pady=10)

# Fungsi untuk menampilkan data penghuni kamar


def tampilkan_data_penghuni():
    def checkout_penghuni():
        selected_item = tree.focus()
        if not selected_item:
            messagebox.showerror("Kesalahan", "Pilih penghuni untuk checkout.")
            return
        nomor_kamar = tree.item(selected_item)['values'][1]
        for p in penghuni:
            if p['nomor_kamar'] == nomor_kamar and p['status'] == "Menginap":
                p['status'] = "Checkout"
                for k in kamar:
                    if k['nomor_kamar'] == nomor_kamar:
                        k['status'] = "Kosong"
                tree.item(selected_item, values=(
                    p['nama'], nomor_kamar, p['durasi'], p['status']))
                messagebox.showinfo("Sukses", "Penghuni berhasil checkout.")
                return

    data_penghuni_window = tk.Toplevel(root)
    data_penghuni_window.title("Data Penghuni Kamar")

    tree = ttk.Treeview(data_penghuni_window, columns=(
        "Nama", "Nomor Kamar", "Durasi", "Status"), show="headings")
    tree.heading("Nama", text="Nama Penghuni")
    tree.heading("Nomor Kamar", text="Nomor Kamar")
    tree.heading("Durasi", text="Durasi")
    tree.heading("Status", text="Status")

    for p in penghuni:
        tree.insert("", "end", values=(
            p['nama'], p['nomor_kamar'], p['durasi'], p['status']))

    tree.pack(padx=10, pady=10)

    tk.Button(data_penghuni_window, text="Checkout",
              command=checkout_penghuni).pack(pady=10)


# Inisialisasi data
kamar = buat_kamar()
penghuni = buat_penghuni()

root = tk.Tk()
root.title("Sistem Reservasi Hotel")

menu_frame = tk.Frame(root)
menu_frame.pack(pady=20)

tk.Button(menu_frame, text="Tambah Kamar", command=tambah_kamar,
          width=20).grid(row=0, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Pesan Kamar", command=pesan_kamar,
          width=20).grid(row=0, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Tampilkan Data Kamar", command=tampilkan_data_kamar,
          width=20).grid(row=1, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Tampilkan Data Penghuni",
          command=tampilkan_data_penghuni, width=20).grid(row=1, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Cari Kamar Kosong (Rekursif)",
          command=cari_kamar_rekursif, width=30).grid(row=2, column=0, padx=10, pady=5)
tk.Button(menu_frame, text="Cari Kamar Kosong (Iteratif)",
          command=cari_kamar_iteratif, width=30).grid(row=2, column=1, padx=10, pady=5)
tk.Button(menu_frame, text="Analisis Efisiensi", command=analisis_efisiensi,
          width=30).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
