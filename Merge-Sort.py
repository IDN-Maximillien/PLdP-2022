# Code is currently being worked
def mergeSort(arr):
    if len(arr) > 1:
  
        # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        print(f'(A) L= {L}, R = {R}')

        # Sorting the first half
        print('\n[Masuk] MergeSort 1')
        mergeSort(L)
        print('[Keluar] MergeSort 1\n')
  
        # Sorting the second half
        print('[Masuk] MergeSort 2')
        mergeSort(R)
        print('[Keluar] MergeSort 2\n')
  
        print(f'(A) L= {L}, R = {R}')
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        print('\n[Masuk] Loop While')
        while i < len(L) and j < len(R):
            print(f'(B) L = {L}, R = {R}')
            print(f'   (1) L[i] = {L[i]}, R[j] = {R[j]}')
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                # print(f'   (2) L[i] = {L[i]}, R[j] = {R[j]}')
                arr[k] = R[j]
                j += 1
            k += 1
        print('[Keluar] Loop While\n')
  
        print(f'(C) L = {L}, R = {R}')
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    print(35*'=')
  
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

data = [67,13,71,39,45]
print(data)
mergeSort(data)
print(data)
