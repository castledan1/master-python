from __future__ import division
import random
from copy import deepcopy
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import time

numElements = 1000
numMin = -1000
numMax = 1000
arrElements = []
times = []

def ordenamientoPorInsercion(unaLista):
    moves = 0
    for indice in range(1,len(unaLista)): 
        valorActual = unaLista[indice]
        posicion = indice

        while posicion>0 and unaLista[posicion-1]>valorActual:
            unaLista[posicion]=unaLista[posicion-1]
            posicion = posicion-1
            moves+=1 
        unaLista[posicion]=valorActual
        moves+=1 
    # print "Insertion: "+str(unaLista)
    return moves


def shellSort(alist):
    moves = 0
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        for i in range(start_position+sublistcount,len(alist),sublistcount):

            current_value = alist[i]
            position = i

            while position>=sublistcount and alist[position-sublistcount]>current_value:
                alist[position]=alist[position-sublistcount]
                moves+=1 
                position = position-sublistcount

            alist[position]=current_value
            moves+=1 
      sublistcount = sublistcount // 2
    # print "ShellSort: "+str(alist)
    return moves

# Python program for implementation of MergeSort 
def mergeSort(arr, moves): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        moves = mergeSort(L, moves) # Sorting the first half 
        moves = mergeSort(R, moves) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                moves+=1
                i+=1
            else: 
                arr[k] = R[j] 
                moves+=1
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            moves+=1
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            moves+=1
            j+=1
            k+=1
    return moves

# Init QuickSort
movesQuick = 0
def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)
#    print("QuickSort: "+str(alist))

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   global movesQuick
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           movesQuick+=1
           alist[rightmark] = temp
           movesQuick+=1

   temp = alist[first]
   alist[first] = alist[rightmark]
   movesQuick+=1
   alist[rightmark] = temp
   movesQuick+=1


   return rightmark
# End QuickSort

# Starts HEAP SORT
movesHeap = 0
def heapify(arr, n, i): 
    global movesHeap
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        movesHeap+=2
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    global movesHeap
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        movesHeap+=2
        heapify(arr, i, 0) 
    # print "HeapSort : "+str(arr)

# Ends HEAP SORT

# Starts bucket sort
movesBucket = 0
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    global movesBucket
    arr = [] 
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            movesBucket += 1
            k += 1
    return x 

# Ends bucket sort
for i in range(numElements):
    arrElements.append(random.randint(numMin,numMax))
# print "Arreglo original"+str(arrElements)

firstTime = int(round(time.time() * 1000))
movesIns = ordenamientoPorInsercion(arrElements[:])
lastTime = int(round(time.time() * 1000))
times.append(lastTime - firstTime)

firstTime = int(round(time.time() * 1000))
movesShell = shellSort(arrElements[:])
lastTime = int(round(time.time() * 1000))
times.append(lastTime - firstTime)

firstTime = int(round(time.time() * 1000))
movesMerge = mergeSort(deepcopy(arrElements), 0)
lastTime = int(round(time.time() * 1000))
times.append(lastTime - firstTime)

# print "MergeSort: "+str(arrayMerge)
firstTime = int(round(time.time() * 1000))
quickSort(arrElements[:])
lastTime = int(round(time.time() * 1000))
times.append(lastTime - firstTime)

firstTime = int(round(time.time() * 1000))
heapSort(arrElements[:])
lastTime = int(round(time.time() * 1000))
times.append(lastTime - firstTime)

arrBucket = []
for i in range(numElements):
    bucketValue = (random.randrange(10,100))/100
    arrBucket.append(bucketValue)

firstTime = int(round(time.time() * 1000))
bucketSort(arrBucket[:])
lastTime = int(round(time.time() * 1000))
times.append(lastTime - firstTime)

# print "Arreglo original"+str(arrElements)
# print "Moves Insertion: "+str(movesIns)
# print "Moves ShellSort: "+str(movesShell)
# print "Moves MergeSort: "+str(movesMerge)
# print "Moves QuickSort: "+str(movesQuick)
# print "Moves HeapSort : "+str(movesHeap)
# print "Moves Bucket :"+str(movesBucket)

names = ["Insertion","ShellSort","MergeSort","QuickSort","HeapSort","BucketSort"]
movesAll = [int(movesIns),int(movesShell),int(movesMerge),int(movesQuick),int(movesHeap),int(movesBucket) ]

y_pos = np.arange(len(names))
plt.figure(figsize=(20, 5))
plt.subplot(1,2,1)
plt.bar(y_pos, movesAll,align='center')
plt.xticks(y_pos, names)
plt.ylabel('Movimientos')

plt.subplot(1,2,2)
plt.bar(y_pos, times,align='center')
plt.xticks(y_pos, names)
plt.ylabel('Tiempo (milisegundos)')

plt.suptitle('Metodos de ordenamiento')

plt.show()