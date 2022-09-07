def SelectionSort(liste):
    print(f'List sebelum di urutkan : {liste}')
    
    for i in range(len(liste)-1, 0, -1):
        max = 0
        for j in range(1, i+1):
            max1 = liste[max]
            if max1 < liste[j]:
                max = j
        liste[max], liste[i] = liste[i], liste[max]
    
    print(f'List sesudah di urutkan : {liste}')

daftar = [67,13,71,39,45]

SelectionSort(daftar)