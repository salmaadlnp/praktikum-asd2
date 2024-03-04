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

    # Menambahkan beberapa skincare
    skincare1 = Skincare(1, "Cleanser", "Cleanser", 50000, 10)
    skincare2 = Skincare(2, "Moisturizer", "Moisturizer", 155000, 15)
    skincare3 = Skincare(3, "Serum", "Serum", 200000, 8)
    skincare4 = Skincare(4, "Sunscreen", "Sunscreen", 100000, 20)
    skincare5 = Skincare(5, "Lip balm", "Lip balm", 20000, 5)
    skincare6 = Skincare(6, "Eye Serum", "Eye Serum", 200000, 5)

    toko.tambah_skincare_awal(skincare1)
    toko.tambah_skincare_akhir(skincare2)
    toko.tambah_skincare_akhir(skincare3)
    toko.tambah_skincare_akhir(skincare4)
    toko.tambah_skincare_diantara(skincare5, 3) # Menambahkan setelah skincare dengan ID 3
    toko.tambah_skincare_diantara(skincare6, 5) # Menambahkan setelah skincare dengan ID 5

    # Menampilkan daftar skincare
    toko.tampilkan_skincare()

    # Mengupdate harga skincare dengan ID 1
    toko.update_skincare(1, "harga", 120000)

    # Menampilkan daftar skincare setelah pembaharuan
    toko.tampilkan_skincare()

    # Menghapus skincare dengan ID 2
    toko.hapus_skincare_diantara(2)

    # Menampilkan daftar skincare setelah penghapusan
    toko.tampilkan_skincare()
