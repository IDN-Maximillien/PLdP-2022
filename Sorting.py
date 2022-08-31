data = [67,13,71,39,45]

def insert_sort(L):
    for i in range(1, len(L)):
        kanan = int(L[i])
        kiri = i-1
        while kiri >= 0 and L[kiri] > kanan:
            L[kiri + 1] = L[kiri]
            kiri -= 1
    print('Hello', L)

insert_sort(data)