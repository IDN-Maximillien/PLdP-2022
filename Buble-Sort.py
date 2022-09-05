daftar = [67, 13, 71, 39, 45]

def tukar(liste, une, deux):
    liste[une], liste[deux] = liste[deux], liste[une]

def bubleSort(liste):
    status = True
    longueur = len(liste)
    k = 1
    while longueur > 1 and status:
        status = False
        j = 1
        while j < longueur:
            # print('line - a')
            if liste[j] < liste[j-1]:
                # print('line - b')
                status = True
                tukar(liste, j, j-1)
                print(f'=== Proses ke-{j} ===')
                # atau bisa juga : print('Proses ke', j)
            else:
                # print('line - c')
                print(f'=== Proses ke-{j} ===')
                # print()
            j += 1
        print(f'iterasi ke-{k} : {liste}')
        k += 1
        if not status:
            print(f'Hasil akhir : {liste}')

print('Sebelum Bubble Sort :', daftar)
bubleSort(daftar)
print('Sesudah Bubble Sort :', daftar)
