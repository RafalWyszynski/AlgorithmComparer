import random
import time


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

def randomQuickSort(arr, left, right):
    if(left >= right):
        return
    pivot = arr[random.randint(left,right)]  
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

def MergeSort(arr, iL, iR):
    if iL < iR:
        mid = (iL + iR)//2
        MergeSort(arr, iL, mid)
        MergeSort(arr, mid + 1, iR)
        Merge(arr, iL, mid, iR)
    return


def Merge(arr, iL, iM, iR):

    arr1 = arr[iL:iM+1].copy()
    arr2 = arr[iM+1:iR+1].copy()

    lenArr1 = len(arr1)
    lenArr2 = len(arr2)

    i = 0
    j = 0
    while 1>0:
        if i > lenArr1 - 1:
            for indexElement in range(j, lenArr2):
                arr[iL] = arr2[indexElement]
                iL += 1
            return

        if j > lenArr2 - 1:
            for indexElement in range(i, lenArr1):
                arr[iL] = arr1[indexElement]
                iL += 1
            return

        if arr1[i] <= arr2[j]:
            arr[iL] = arr1[i]
            i += 1
            iL += 1
        else:
            arr[iL] = arr2[j]
            j += 1
            iL += 1

def Start():
    warunek = 0
    option3 = 0
    print("\nWitaj w programie porównującym 3 algorytmy sortowania.")
    option1 = input('[1] Wczytaj dane z klawiatury. \n[2] Wczytaj dane z pliku.\n')

    while option1 != "1" and option1 != "2":
        print("[BŁĄD] Wprowadź prawidłową wartość!\n")
        option1 = input('[1] Wczytaj dane z klawiatury. \n[2] Wczytaj dane z pliku.\n')  

    date = []
    if option1 == "1": 
        print("Ile danych chcesz wprowadzić?")
        while True:
            try:
                dateCount = int(input())
                if dateCount <= 0:
                    somethink = int("Hey")
                break
            except:
                print("\n[BŁĄD] Wprowadzono złą wartość. Spróbuj ponownie:")    #Klawiatura
        print("Wprowadź " + str(dateCount) +" wartości. Każdą potwierdź enterem:")
        i = 0
        while i < int(dateCount):
            try:                
                i+=1
                date.append(int(input()))
            except:
                i= i-1
                print("[BŁĄD] Wprowadź cyfrę!")
    elif option1 == "2":    #Plik 
        print("\nCzy chcesz edytować plik czy stworzyć nowy?")
        option3 = input('[1] Stwórz plik. \n[2] Wczytaj istniejący plik.\n')

        while option3 != "1" and option3 != "2":
            print("[BŁĄD] Wprowadź prawidłową wartość!\n")
            option3 = input('[1] Stwórz plik. \n[2] Wczytaj istniejący plik.\n') 

        if option3=="2":
            print("Podaj nazwę pliku (plik musi znajdować się w folderze) w formacie nazwa.txt: ")
            while True:
                try:
                    path = str(input())            
                    file = open(path)
                    break
                except:
                    print("\n[BŁĄD] Plik musi znajdować się w tym samym folderze! Wprowadź nazwę ponownie:")
            try:
                content = file.read()
                file.close()
                dateContent = content.split()          
                for elements in dateContent:
                    date.append(int(elements))
            except:
                print("[BŁĄD] Plik zawiera źle sformatowane dane!")
                warunek = 1
        elif option3 == "1":
            print("\nPodaj nazwę pliku:")
            while True:
                try:
                    path = str(input())            
                    file = open(path,'w')
                    break
                except:
                    print("[BŁĄD] Nieprawidłowo wpisano nazwę pliku!")

            print("\nIle danych chcesz wprowadzić?")
            while True:
                try:
                    dateCount = int(input())
                    break
                except:
                    print("[BŁĄD] Ile danych chcesz wprowadzić?")    #Klawiatura
            print("Wprowadź " + str(dateCount) +" wartości. Każdą potwierdź enterem:")
            i = 0
            while i < int(dateCount):
                try:                
                    i+=1
                    temp = int(input())
                    file.write(str(temp))
                    file.write(' ')
                except:
                    i= i-1
                    print("[BŁĄD] Wprowadź cyfrę!")               
            file.close()
            file = open(path)
            content = file.read() 
            dateContent = content.split()          
            for elements in dateContent:
                date.append(int(elements))
        

    if warunek == 0:
        dateMS = date.copy()
        dateQSR = date.copy()
        dateQSM = date.copy()

        print(f"\nPrzed posortowaniem: {date}")
        print("\n/////////////////Quick Sort z pivotem jako mediana////////////////")
        tic = time.perf_counter()
        quickSort(dateQSM, 0, len(dateQSM)-1)
        toc = time.perf_counter()
        print(f"Po posortowaniu: {dateQSM}")
        t1 = toc -  tic
        print(f"Czas trwania: {t1:0.10f} sekundy")

        print("\n///////////////////Quick Sort z losowym pivotem///////////////////")
        tic2 = time.perf_counter()
        randomQuickSort(dateQSR, 0, len(dateQSR)-1)
        print(f"Po posortowaniu: {dateQSR}")
        toc2 = time.perf_counter()
        t2 = toc2 - tic2
        print(f"Czas trwania: {t2:0.10f} sekundy")

        print("\n////////////////////////////Merge Sort////////////////////////////")
        tic3 = time.perf_counter()
        MergeSort(dateMS, 0, len(dateMS)-1)
        print(f"Po posortowaniu: {dateMS}")
        toc3 = time.perf_counter()
        t3 = toc3 - tic3
        print(f"Czas trwania: {t3:0.10f} sekundy")

        if(t3>t2>t1):
            print("\n****KOLEJNOŚĆ OD NAJSZYBSZEGO****:\n1.Quick Sort z pivotem jako mediana.\n2.Quick Sort z losowym pivotem.\n3.Merge Sort.")
        if(t2>t3>t1):
            print("\n****KOLEJNOŚĆ OD NAJSZYBSZEGO****:\n1.Quick Sort z pivotem jako mediana.\n2.Merge Sort.\n3.Quick Sort z losowym pivotem.")
        if(t3>t1>t2):
            print("\n****KOLEJNOŚĆ OD NAJSZYBSZEGO****:\n1.Quick Sort z losowym pivotem.\n2.Quick Sort z pivotem jako mediana.\n3.Merge Sort.")
        if(t1>t3>t2):
            print("\n****KOLEJNOŚĆ OD NAJSZYBSZEGO****:\n1.Quick Sort z losowym pivotem.\n2.Merge Sort.\n3.Quick Sort z pivotem jako mediana.")
        if(t2>t1>t3):
            print("\n****KOLEJNOŚĆ OD NAJSZYBSZEGO****:\n1.Merge Sort.\n2.Quick Sort z pivotem jako mediana.\n3.Quick Sort z losowym pivotem.")
        if(t1>t2>t3):
            print("\n****KOLEJNOŚĆ OD NAJSZYBSZEGO****:\n1.Merge Sort.\n2.Quick Sort z losowym pivotem.\n3.Quick Sort z pivotem jako mediana.")

    return

Start()