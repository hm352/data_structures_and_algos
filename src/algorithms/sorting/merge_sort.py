def merge_sort(array, l, r):
    if l < r:
        mid = (l + r) // 2
        merge_sort(array, l, mid)
        merge_sort(array, mid + 1, r)
        merge(array, l, mid, r)

def merge(array, l, mid, r):
    temp = []
    i = l
    j = mid + 1
    while i <= mid and j <= r:
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= mid:
        temp.append(array[i])
        i += 1
    while j <= r:
        temp.append(array[j])
        j += 1
    for i in range(l, r + 1):
        array[i] = temp[i - l]
    print(array)
    return array
    

if __name__ == "__main__":
    unsorted = [5, 4, 3, 2, 1, 7,10, 25, 24]
    print(unsorted)
    s = merge_sort(unsorted, 0, len(unsorted) - 1)
    print(unsorted)