def mergeSort(arr):
    if len(arr) > 1:
  
        # Finding the mid of the array
        mid = len(arr)//2
  
        # Dividing the array elements
        L = arr[:mid]
  
        # into 2 halves
        R = arr[mid:]
  
        print(f'(A) arr = {arr}, L= {L}, R = {R}')

        # Sorting the first half
        print('\n[Masuk] MergeSort 1')
        mergeSort(L)
        print('[Keluar] MergeSort 1\n')
  
        print(f'(B) arr = {arr}, L= {L}, R = {R}')

        # Sorting the second half
        print('[Masuk] MergeSort 2')
        mergeSort(R)
        print('[Keluar] MergeSort 2\n')
  
        print(f'(C) arr = {arr}, L = {L}, R = {R}')
        i = j = k = 0
  
        # Copy data to temp arrays L[] and R[]
        print('\n[Masuk] Loop While')
        while i < len(L) and j < len(R):
            print(f'(D) arr = {arr}, L = {L}, R = {R}')
            print(f'   (1) i = {i}, L[i] = {L[i]}, j = {j} R[j] = {R[j]}')
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                # print(f'   (2) L[i] = {L[i]}, R[j] = {R[j]}')
                arr[k] = R[j]
                j += 1
            k += 1
        print('[Keluar] Loop While\n')
  
        print(f'(E) arr = {arr}, L = {L}, R = {R}')
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        print(f'(F) arr = {arr}, L = {L}, R = {R}')

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
  
        print(f'(G) arr = {arr}, L = {L}, R = {R}')
  
    print(50*'=')
  
# Code to print the list
  
  
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

data = [78,34,56,12]
print(data)
mergeSort(data)
print(data)
