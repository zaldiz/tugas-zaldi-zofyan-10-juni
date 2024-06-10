class Produk:
    def __init__(self, kode, nama, harga, kategori):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.kategori = kategori

def cari_produk_berdasarkan_kode(kode_produk):
    """Fungsi untuk mencari produk berdasarkan kode produk."""
     # Inisialisasi list produk
    produk_list = [
        Produk("P01", "zx25r", 100000000, "kendaraan"),
        Produk("P02", "hp", 3000000, "Elektronik"),
        Produk("P03", "baju", 200000, "Pakaian"),
    ]

    for produk in produk_list:
        if produk.kode == kode_produk:
            return produk
    return None

def main():
   
    # Contoh penggunaan
    kode_produk = input("Masukkan kode produk: ")
    produk_ditemukan = cari_produk_berdasarkan_kode(kode_produk)

    if produk_ditemukan:
        print(f"Produk dengan kode {kode_produk}:")
        print(f"Nama: {produk_ditemukan.nama}")
        print(f"Harga: {produk_ditemukan.harga}")
        print(f"Kategori: {produk_ditemukan.kategori}")
    else:
        print(f"Produk dengan kode {kode_produk} tidak ditemukan.")

if __name__ == "__main__":
    main()
