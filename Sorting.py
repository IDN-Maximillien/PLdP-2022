# data = [67,13,71,39,45]

def insert_sort(L):
    print("Sebelum sort : ",L)

    # for j in range(1, len(L) + 1):
    for i in range(1, len(L)):
        kanan = L[i]
        kiri = i-1
        while kiri >= 0 and L[kiri] > kanan:
            L[kiri + 1] = L[kiri]
            kiri -= 1
        L[kiri + 1] = kanan
    
        
    print("Sesudah sort : ",L)
    # print('Hello', L)

data = []

panjang = int(input('Panjang List : '))
for j in range(1, panjang+1):
    angka = int(input(f'Angka {j} : '))
    data.append(angka)

insert_sort(data)
