class PenilaianMahasiswa:
    def __init__(self, nama, nim, tugas, uts, uas):
        self.nama = nama
        self.nim = nim
        self.tugas = self._cek_nilai(tugas)
        self.uts = self._cek_nilai(uts)
        self.uas = self._cek_nilai(uas)
    def _cek_nilai(self, nilai):
        if not (0 <= nilai <= 100):
            raise ValueError ("nilai harus antara 0 sampek 100")
        return nilai
    def hitung_final(self):
        return(self.tugas*0.3)+(self.uts*0.3)+(self.uas*0.4)
    def cek_grade(self):
        final = self.hitung_final()
        if final >= 85:
            grade = "A"
        elif final >= 75:
            grade = "B"
        elif final >= 65:
            grade = "C"
        elif final >= 50:
            grade = "D"
        else:
            grade = "E"
        status="lulus"if final>=65 else "gagal"
        return grade, status
    def cetak(self):
        final = self.hitung_final()
        grade, status=self.cek_grade()

        print("=======================")
        print(f"nama: {self.nama}")
        print(f"nim: {self.nim}")
        print(f"nilai akhir: {final:.2f}")
        print(f"kelas: {grade}")
        print(f"status: {status}")
        print("=======================")

if __name__ == "__main__":

    try:
        nama = input("nama: ")
        nim = input("nim: ")
        tugas = float(input("nilai akhir tugas: "))
        uts = float(input("nilai akhir uts: "))
        uas = float(input("nilai akhir uas: "))
        mhs = PenilaianMahasiswa(nama, nim, tugas, uts, uas)
        print("=====================")


        mhs.cetak()
    except ValueError as e:
        print(f"inputanmu salah brosis")