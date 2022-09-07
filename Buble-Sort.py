daftar = [67, 13, 71, 39, 45, 89]

def tukar(liste, une, deux):
    liste[une], liste[deux] = liste[deux], liste[une]

def bubleSort_for(liste):
    status = True
    longueur = len(liste)
    k = 1
    while longueur > 1 and status:
        status = False
        j = 1
        
        for m in range(longueur-1):
            # print('line - a')
            if liste[j] < liste[j-1]:
                # print('line - b')
                status = True
                tukar(liste, j, j-1)
                print(f'=== Proses ke-{j} : {liste} ===')
            else:
                # print('line - c')
                print(f'=== Proses ke-{j} : {liste} ===')
            j += 1
        

def bubleSort_while(liste):
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
                print(f'=== Proses ke-{j} : {liste} ===')
                # atau bisa juga : print('Proses ke', j)
            else:
                # print('line - c')
                print(f'=== Proses ke-{j} : {liste} ===')
                # print()
            j += 1
            
        print(f'iterasi ke-{k} : {liste}')
        k += 1
        if not status:
            print(f'Hasil akhir : {liste}')

print('Sebelum Bubble Sort :', daftar)
bubleSort_while(daftar)
print('Sesudah Bubble Sort :', daftar)
