arr = [41, 39, 34, 1, 2, 4, 2, 6, 39 ]

largest = -1
second_largest = -1

for i in range(len(arr)):
    if arr[i] > largest:
        second_largest = largest
        largest = arr[i]
    elif arr[i] > second_largest and arr[i] < largest:
        second_largest = arr[i]

print(second_largest)
