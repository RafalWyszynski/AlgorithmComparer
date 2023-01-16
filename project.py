import random

def quickSort(arr, left, right):
    if(left >= right):
        return
    pivot = arr[(left + right) // 2]  
    i = left - 1
    j = right + 1
    while(1):
        while(1):             
            i += 1
            if(arr[i] >= pivot):
                break
        while(1):           
            j -= 1
            if(arr[j] <= pivot):
                break
        if(i >= j):
            break
        arr[i],arr[j] = arr[j],arr[i]
    quickSort(arr, left, j)
    quickSort(arr, j+1, right)


array = []
print("Ile danych chcesz wprowadzić?")
x = int(input())
print("Wprowadź " +str(x) +" wartości. Każdą potwierdź spacją:")
for i in range (0,x):
    c = int(input())
    array.append(c)    
print(array)
quickSort(array, 0, len(array)-1)
print(array)