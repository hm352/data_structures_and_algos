# you have an unsorted list of integers, find the second highest number in that list
# without sorting the list

arr = [12, 35, 1, 10, 34, 1]

def second_largest(arr):
    first = arr[0]
    second = -1
    for i in range(1, len(arr)):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
    return second

result = second_largest(arr)
print(result)