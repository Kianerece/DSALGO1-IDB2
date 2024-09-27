#Insertion Sort
def InsertionSort(arr1):
    arr1 = [10, 2, 3, 1, 1, 4, 89, 21]
    print("Arr1 before Insertion Sort")
    print(arr1)
    for i in range (len(arr1)):
        key = arr1[i]
        j = i - 1

        while j >= 0 and key < arr1[j]:
            arr1[j + 1] = arr1[j]
            j -= 1
        arr1[j + 1] = key
    print("Arr1 after Insertion Sort")
    print(arr1)
    InsertionSort(arr1)
#Selection Sort
def SelectionSort(arr2):
    arr2 = [10, 2, 3, 1, 1, 4, 89, 21]
    print("\nArr2 before Selection Sort")
    print(arr2)
    for i in range(len(arr2)):
        min_idx = i
        for j in range(i + 1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
                #swapping the values from our array
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
    print("Arr2 values after Selection Sort")
    print(arr2)
    SelectionSort()

#Bubble Sort
def BubbleSort(arr3):
    arr3 = [10, 2, 3, 1, 1, 4, 89, 21]
    print("\nArr3 values before Bubble Sort")
    print(arr3)
    for i in range(len(arr3)):
        for j in range(0, len(arr3) - i - 1):
            if arr3[j] > arr3[j + 1]:
                arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]
    print("Array 3 values after Bubble Sort")
    print(arr3)
    BubbleSort()