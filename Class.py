class PersegiPanjang:

    def __init__(self, inPanjang, inLebar):
        self.panjang = inPanjang
        self.lebar = inLebar
    
    def hitung_luas(self):
        return self.panjang * self.lebar
    
    def hitung_keliling(self):
        return 2*(self.panjang + self.lebar)
    
    def gambar_persegi_panjang(self):
        for i in range(self.lebar):
            for j in range(self.panjang):
                print('[]', end='')
            print()
    def gambar_persegi_panjang_tanpa_isi(self):
        for i in range(0, self.lebar):
            if i > 0 and i < self.lebar-1:
                for j in range(0, self.panjang):
                    if j > 0 and j < self.panjang-1:
                        print('  ', end="")
                    else:
                        print('[]', end="")
            else:
                for j in range(0, self.panjang):
                    print('[]', end="")
            print("")

PersegiPanjangA = PersegiPanjang(20, 10)
PersegiPanjangB = PersegiPanjang(10, 5)

print("Panjang persegi panjang A :", PersegiPanjangA.panjang)
print("Lebar persegi panjang A :", PersegiPanjangA.lebar)
print("Luas persegi panjang A : ", PersegiPanjangA.hitung_luas())
print("Keliling persegi panjang A : ", PersegiPanjangA.hitung_keliling())
print("\nMenggambar Persegi Panjang A : ")
PersegiPanjangA.gambar_persegi_panjang()
print("\nMenggambar Persegi Panjang A hanya tepinya saja : ")
PersegiPanjangA.gambar_persegi_panjang_tanpa_isi()

print("Panjang persegi panjang B :", PersegiPanjangB.panjang)
print("Lebar persegi panjang B :", PersegiPanjangB.lebar)
print("Luas persegi panjang B : ", PersegiPanjangA.hitung_luas())
print("Keliling persegi panjang B : ", PersegiPanjangB.hitung_keliling())
print("\nMenggambar Persegi Panjang B : ")
PersegiPanjangB.gambar_persegi_panjang()
print("\nMenggambar Persegi Panjang B hanya tepinya saja : ")
PersegiPanjangB.gambar_persegi_panjang_tanpa_isi()

print('*'*50)
print(PersegiPanjang.__doc__)
print(PersegiPanjang.__name__)
print(PersegiPanjang.__dict__)
print(PersegiPanjang.__module__)
print(PersegiPanjang.__bases__)
print('*'*50)
print(PersegiPanjangA.__doc__)
print(PersegiPanjangA.__dict__)
print(PersegiPanjangA.__module__)
print(PersegiPanjang.____)
