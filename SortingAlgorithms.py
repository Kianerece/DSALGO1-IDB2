#Insertion Sort
arr1 = [10, 2, 3 , 1 , 1, 4, 89, 21]
#printing the values arr1

print(aar1)
for i in range(1, len(arr1)):#
    key = arr1[i]
    j = i - 1
    # move elements of arr1[0..i-1]
    #that are greater than the key
    #to  one position ahead of
    #their current position

    while j >= 0 and key < arr1[j]:#
        arr1[j + 1] = aar1[j]
        j-=1
    arr1[j+1]= key

        print("arr1 after insertion")
        print(arr1)
        arr2 = [10, 2,3, 1,1 ,4, 89, 21]

        print("arr2 before Selection Sort: ")
        print(arr2)
    for i in range(len(arr2)):
        min_idx = 1
        for j in range(i +1, len(arr2)):
            if arr2[min_idx] > arr2[j]:
                min_idx = j
                #swapping values from our array
                arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i]
print(arr2)