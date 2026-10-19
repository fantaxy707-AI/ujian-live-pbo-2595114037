class TransaksiKasir:
    def __init__(self, nama, barang, jumlah, harga):
        self.nama=nama
        self.barang=barang
        self.harga=self._validasi_nilai(harga, "Harga Barang ")
        self.jumlah=int(self._validasi_nilai(jumlah, "Jumlah Barang"))

    def _validasi_nilai(selfself, nilai, keterangan):
        if nilai <= 0:
            raise ValueError(f"{keterangan} harus pakai nilai yang positif (lebih dari nol (0))")
        return nilai

    def _format_rupiah(self, nominal):
        return f"RP{int(nominal):,.0f}".replace(",",".")

    def hitung_subtotal(self):
        return self.harga *self.jumlah

    def hitung_diskon(self):
        subtotal = self.hitung_subtotal()
        if subtotal >= 500000:
            persen = 15
        elif subtotal >= 250000:
            persen = 10
        elif subtotal >= 100000:
            persen = 5
        else:
            persen = 0

        potongan = int(subtotal*(persen/100))
        return persen, potongan

    def total_bayar(self):
        subtotal=self.hitung_subtotal()
        _, potongan=self.hitung_diskon()
        return subtotal-potongan

    def cetak(self):
        subtotal = self.hitung_subtotal()
        persen, potongan=self.hitung_diskon()
        total=self.total_bayar()

        print("=====================")
        print(f"pembeli : {self.nama}")
        print(f"barang : {self.barang}")
        print(f"subtotal : {self._format_rupiah(subtotal)}")
        print(f"diskon : {persen}%")
        print(f"potongan : {self._format_rupiah(potongan)}")
        print(f"total bayar : {self._format_rupiah(total)}")
if __name__ == "__main__":
    try:
        print("=====================")
        nama=input("nama pembeli: ")
        barang=input("nama barang: ")
        harga=float(input("harga barang:"))
        jumlah=float(input("jumlah barang: "))
        print("=====================")
        transaksi=TransaksiKasir(nama, barang, jumlah, harga)
        transaksi.cetak()

    except ValueError as e:
        print(f"inputan nya salah bro/sis")