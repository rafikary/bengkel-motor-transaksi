import tkinter as tk
from tkinter import ttk
import csv
import pandas as pd

class BengkelMotor:
    def __init__(self, root):
        self.root = root
        self.root.title("Bengkel")

        self.bengkel = []

        # untuk tempat menginputkan data 
        barang_label = tk.Label(root, text="Nama Barang:")
        barang_label.pack()
        self.barang_entry = tk.Entry(root)
        self.barang_entry.pack()

        harga_label = tk.Label(root, text="Harga Barang:")
        harga_label.pack()
        self.harga_entry = tk.Entry(root)
        self.harga_entry.pack()

        stok_label = tk.Label(root, text="Stok")
        stok_label.pack()
        self.stok_entry = tk.Entry(root)
        self.stok_entry.pack()

        # Button untuk menambah seluruh data yang telah diinputkan
        add_button = tk.Button(root, text="Submit", command=self.add_bengkel)
        add_button.pack(pady=10)

        save_button = tk.Button(root, text="Simpan ke CSV", command=self.save_to_csv)
        save_button.pack(pady=10)

         # Fungsi dibawah ini untuk membuat tabel untuk menampilkan barang yang ada dibengkel
        columns = ("Nama_Barang","Harga_Barang","Stok")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
        self.tree.pack(padx=10, pady=10)

        # Load data dari CSV
        self.load_bengkel()

    def load_bengkel(self):
        try:
            with open("data_bengkel.csv", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.tree.insert("", "end", values=(row["Nama_Barang"], row["Harga_Barang"], row["Stok"]))
                    self.bengkel.append(row)
        except FileNotFoundError:
            # untuk mengantisipasi jika file tidak ditemukan
            pass
   

    def add_bengkel(self):
        # untuk Mendapatkan nilai dari data yang sudah diinputkan
        barang = self.barang_entry.get()
        harga = self.harga_entry.get()
        stok = self.stok_entry.get()
        
        # untuk menyimpan data diCSV
        self.bengkel.append({"Nama_Barang": barang, "Harga_Barang": harga, "Stok": stok })

        # Menambahkan data pengeluaran ke Treeview
        self.tree.insert("", "end", values=(barang, harga, stok))

        # untuk mengosongkan input data setelah ditambahkan
        self.barang_entry.delete(0, tk.END)
        self.harga_entry.delete(0, tk.END)
        self.stok_entry.delete(0, tk.END)
    
    def save_to_csv(self):
    # Membuat DataFrame dari data produksi
        df = pd.DataFrame(self.bengkel)

    # Menyimpan DataFrame ke dalam file CSV tanpa menyertakan indeks
        df.to_csv("data_bengkel.csv", index=False)
        print("Data berhasil disimpan ke data_bengkel.csv")

if __name__ == "__main__":
    root = tk.Tk()
    app = BengkelMotor(root)
    root.mainloop()

