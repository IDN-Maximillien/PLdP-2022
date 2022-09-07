# Memasukkan Library ke dalam Kode
import random

# Fungsi List Angka Acak
def randomList(liste):
    panjang = int(input('Tentukan Panjang List : '))
    while True:
        liste.append(random.randint(10, 90))
        if len(liste) >= panjang:
            break

def partition(l, r, nums):
    # Elemen terakhir akan menjadi pivot dan elemen terakhir akan menjadi pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Menukar nilai yang lebih kecil dari pivot ke depan
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Menukar elemen terakhir dengan nilai yang ditunjuk pointer
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr
 
def quicksort(l, r, nums):
    if len(nums) == 1:  # Menentukan kondisi untuk mencegah pengulangan tak henti
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Mengurutkan nilai sebelah kiri
        quicksort(pi+1, r, nums)  # Mengurutkan nilai sebelah kanan
    return nums

 
# List angka pertama
data = [67,13,71,39,45]
print(f'Sebelum Sorting : {data}')
print(quicksort(0, len(data)-1, data))
print(f'Sesudah Sorting : {data}')

# List angka ke dua
daftar = []
randomList(daftar)
print(f'Sebelum Sorting : {daftar}')
print(quicksort(0, len(daftar)-1, daftar))
print(f'Sesudah Sorting : {daftar}')
