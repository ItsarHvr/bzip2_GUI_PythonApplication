import bz2
import os
import tkinter as tk
from tkinter import filedialog, messagebox


def compress_file():
    input_file = filedialog.askopenfilename(title="Pilih file untuk dikompresi")
    if not input_file:
        return
   
    output_file = input_file + ".bz2"
   
    if not os.path.isfile(input_file):
        messagebox.showerror("Error", f"File '{input_file}' tidak ditemukan.")
        return
    # Membaca file asli
    with open(input_file, 'rb') as file:
        data = file.read()
   
    # Mengompresi data menggunakan Bzip2
    compressed_data = bz2.compress(data)
    # Menyimpan data yang telah dikompresi
    with open(output_file, 'wb') as file:
        file.write(compressed_data)
    # Menghitung ukuran file sebelum dan sesudah kompresi
    original_size = os.path.getsize(input_file)
    compressed_size = os.path.getsize(output_file)
   
    messagebox.showinfo("Sukses",
        f"File berhasil dikompresi:\n"
        f"Dari {original_size} bytes menjadi {compressed_size} bytes\n"
        f"Efisiensi: {100 - (compressed_size / original_size * 100):.2f}% lebih kecil"
    )


def decompress_file():
    input_file = filedialog.askopenfilename(title="Pilih file .bz2 untuk didekompresi", filetypes=[("Bzip2 Files", "*.bz2")])
    if not input_file:
        return


    # Mendapatkan nama file asli tanpa .bz2
    if input_file.endswith(".bz2"):
        original_name = input_file[:-4]  # Menghapus ".bz2"
        default_extension = os.path.splitext(original_name)[1]  # Ambil ekstensi asli
    else:
        original_name = input_file
        default_extension = ""


    # Menentukan nama file default untuk penyimpanan
    output_file = filedialog.asksaveasfilename(
        title="Simpan sebagai",
        initialfile=os.path.basename(original_name),  # Gunakan nama asli sebagai default
        defaultextension=default_extension,  # Pakai ekstensi asli
        filetypes=[("All Files", "*.*")]
    )
   
    if not output_file:
        return


    try:
        with bz2.open(input_file, 'rb') as file_in, open(output_file, 'wb') as file_out:
            file_out.write(file_in.read())


        messagebox.showinfo("Sukses", f"File berhasil didekompresi sebagai '{output_file}'")
    except Exception as e:
        messagebox.showerror("Error", f"Terjadi kesalahan saat dekompresi: {e}")


# Membuat GUI dengan Tkinter
root = tk.Tk()
root.title("Kompresi & Dekompresi Bzip2")
root.geometry("400x200")
# Tombol untuk kompresi
compress_button = tk.Button(root, text="Kompresi File", command=compress_file, width=30)
compress_button.pack(pady=10)
# Tombol untuk dekompresi
decompress_button = tk.Button(root, text="Dekompresi File", command=decompress_file, width=30)
decompress_button.pack(pady=10)
# Tombol keluar
exit_button = tk.Button(root, text="Keluar", command=root.quit, width=30)
exit_button.pack(pady=10)
# Menjalankan event loop Tkinter
root.mainloop()