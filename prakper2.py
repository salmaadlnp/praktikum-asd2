class Skincare:
    def __init__(self, id, nama, jenis, harga, stok):
        self.id = id
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.stok = stok
        self.next = None

class LinkedListSkincare:
    def __init__(self):
        self.head = None

    def tambah_skincare_awal(self, skincare):
        skincare.next = self.head
        self.head = skincare

    def tambah_skincare_akhir(self, skincare):
        if not self.head:
            self.head = skincare
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = skincare

    def tambah_skincare_diantara(self, skincare, id_sebelumnya):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        current = self.head
        while current:
            if current.id == id_sebelumnya:
                skincare.next = current.next
                current.next = skincare
                return
            current = current.next
        print("Skincare dengan ID {} tidak ditemukan.".format(id_sebelumnya))

    def hapus_skincare_awal(self):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        self.head = self.head.next

    def hapus_skincare_akhir(self):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        if prev:
            prev.next = None
        else:
            self.head = None

    def hapus_skincare_diantara(self, id_sebelumnya):
        if not self.head:
            print("Tidak ada skincare tersedia.")
            return
        current = self.head
        prev = None
        while current:
            if current.id == id_sebelumnya:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next
        print("Skincare dengan ID {} tidak ditemukan.".format(id_sebelumnya))

    def tampilkan_skincare(self):
        current = self.head
        if not current:
            print("Tidak ada skincare tersedia.")
        else:
            print("Daftar Skincare:")
            while current:
                print("ID:", current.id)
                print("Nama:", current.nama)
                print("Jenis:", current.jenis)
                print("Harga:", current.harga)
                print("Stok:", current.stok)
                print("-----------------------")
                current = current.next

    def update_skincare(self, id, field, value):
        current = self.head
        while current:
            if current.id == id:
                if hasattr(current, field):
                    setattr(current, field, value)
                    print("Skincare dengan ID {} berhasil diperbarui.".format(id))
                    return
                else:
                    print("Field tidak valid.")
                    return
            current = current.next
        print("Skincare dengan ID {} tidak ditemukan.".format(id))


if __name__ == "__main__":
    toko = LinkedListSkincare()

    while True:
        print("\nMenu:")
        print("1. Tambah barang di awal")
        print("2. Tambah barang di akhir")
        print("3. Tambah barang di antara node")
        print("4. Hapus barang di awal")
        print("5. Hapus barang di akhir")
        print("6. Hapus barang di antara node")
        print("7. Lihat barang")
        print("8. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan Nama: ")
            jenis = input("Masukkan Jenis: ")
            harga = int(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            skincare = Skincare(id, nama, jenis, harga, stok)
            toko.tambah_skincare_awal(skincare)
        elif pilihan == "2":
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan Nama: ")
            jenis = input("Masukkan Jenis: ")
            harga = int(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            skincare = Skincare(id, nama, jenis, harga, stok)
            toko.tambah_skincare_akhir(skincare)
        elif pilihan == "3":
            id_sebelumnya = int(input("Masukkan ID sebelumnya: "))
            id = int(input("Masukkan ID: "))
            nama = input("Masukkan Nama: ")
            jenis = input("Masukkan Jenis: ")
            harga = int(input("Masukkan Harga: "))
            stok = int(input("Masukkan Stok: "))
            skincare = Skincare(id, nama, jenis, harga, stok)
            toko.tambah_skincare_diantara(skincare, id_sebelumnya)
        elif pilihan == "4":
            toko.hapus_skincare_awal()
        elif pilihan == "5":
            toko.hapus_skincare_akhir()
        elif pilihan == "6":
            id_sebelumnya = int(input("Masukkan ID sebelumnya: "))
            toko.hapus_skincare_diantara(id_sebelumnya)
        elif pilihan == "7":
            toko.tampilkan_skincare()
        elif pilihan == "8":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
