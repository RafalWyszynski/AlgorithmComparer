import random

def QuickSort(arr, left, right):
    if left < right:
        x = random.randint(left,right)
        print(x)
        i = left
        j = right
        while 1>0:
            while arr[i] < arr[x] and i<len(arr):
                i = i+1
            while arr[j] >= arr[x] and j>=0:
                j = j-1
            if i <= j:
                arr[i],arr[j] = arr[j],arr[i]
            else:
                break
        print(arr)              
        if i < right:
            QuickSort(arr, i, right)
        if j > left:
            QuickSort(arr, left, j)


    


    
array = []
print("Ile danych chcesz wprowadzić?")
x = int(input())
print("Wprowadź " +str(x) +" wartości. Każdą potwierdź spacją:")
for i in range (0,x):
    c = int(input())
    array.append(c)    
print(array)
print(QuickSort(array, 0, len(array)-1))
