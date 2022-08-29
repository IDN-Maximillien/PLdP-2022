
def binSearch(angka, daftar):
    daftar.sort()
    langkah = 0
    ketemu = False
    awal = 0
    akhir = len(daftar)-1

    while awal <= akhir and not ketemu:
        tengah = (awal+akhir)//2
        print(f'Awal = {awal}, Tengah = {tengah}, Akhir = {akhir}')
        if daftar[tengah] == angka:
            ketemu = True
            break
        elif angka > daftar[tengah]:
            awal = tengah + 1
        else:
            akhir = tengah - 1
        langkah += 1
        
    if ketemu == True:
        print(f'Angka {angka} ditemukan pada posisi ke {awal +1}!')
    else:
        print(f'Angka {angka} tidak ditemukan! Pencarian dilakukan sebanyak {langkah} langkah.')

def searchAlt(angka, listAngka):
    stat = False
    for i in range(len(listAngka)):
        if listAngka[i] == angka:
            stat = True
            break
        else:
            continue
    if stat == True:
        print(f'{angka} ditemukan pada indeks ke {i+1}')
    else: 
        print(f'{angka} tidak ditemukan!')
listAngka = [67,13,71,39,45]
cariangka = int(input('Angka : '))    

binSearch(cariangka, listAngka)
searchAlt(cariangka, listAngka)
