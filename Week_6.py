import time

class Belanja:
    def __init__(self):
        self.keranjang = []  # List untuk menyimpan barang (nama & harga)

    def tambah_barang(self, nama, harga):
        self.keranjang.append((nama, harga))
        print(f"{nama} (Rp{harga:,.2f}) berhasil ditambahkan ke keranjang!")

    def hapus_barang(self, nama):
        for item in self.keranjang:
            if item[0] == nama:
                self.keranjang.remove(item)
                print(f"🗑 {nama} berhasil dihapus dari keranjang!")
                return
        print("Barang tidak ditemukan di keranjang!")

    def tampilkan_keranjang(self):
        if not self.keranjang:
            print("🛒 Keranjang belanja Anda kosong.")
            return
        print("\n🛍 Keranjang Belanja Anda:")
        for i, (nama, harga) in enumerate(self.keranjang, start=1):
            print(f"{i}. {nama} - Rp{harga:,.2f}")
        print(f"Total sementara: Rp{self.hitung_total():,.2f}\n")

    def hitung_total(self):
        return sum(harga for _, harga in self.keranjang)

    def checkout(self):
        if not self.keranjang:
            print("⚠ Keranjang belanja kosong! Tambahkan barang sebelum checkout.")
            return
        print("\n Checkout Berhasil!")
        print(f" Total Belanja Anda: Rp{self.hitung_total():,.2f}")
        print("✅ Terima kasih telah berbelanja!")
        self.keranjang.clear()  # Kosongkan keranjang setelah checkout


belanja = Belanja()

while True:
    print("\n=== MENU ===")
    print("1. Tambah Barang ke Keranjang")
    print("2. Hapus Barang dari Keranjang")
    print("3. Lihat Keranjang")
    print("4. Checkout")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        nama = input("Masukkan nama barang: ")
        while True:  # Loop untuk memastikan harga yang dimasukkan valid
            try:
                harga = float(input("Masukkan harga barang: "))
                belanja.tambah_barang(nama, harga)
                break  # Keluar dari loop jika harga valid
            except ValueError:
                print("Harga harus berupa angka! Coba lagi.")
        
    elif pilihan == "2":
        nama = input("Masukkan nama barang yang ingin dihapus: ")
        belanja.hapus_barang(nama)

    elif pilihan == "3":
        belanja.tampilkan_keranjang()

    elif pilihan == "4":
        start_time = time.time()  # Mulai hitung waktu
        belanja.checkout()
        end_time = time.time()  # Akhir hitung waktu
        print(f"Waktu eksekusi: {end_time - start_time:.6f} detik")

    elif pilihan == "5":
        print("Terima kasih !")
        break

    else:
        print("Pilihan tidak valid! Silakan coba lagi.")
