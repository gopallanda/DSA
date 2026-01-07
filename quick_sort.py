def quickSort_naive(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quickSort_naive(left) + [pivot] + quickSort_naive(right)


def quickSort_lomuto(arr, low, high):
    if low < high:
        pivot_index = lomuto_partition(arr, low, high)
        quickSort_lomuto(arr, low, pivot_index - 1)
        quickSort_lomuto(arr, pivot_index + 1, high)


def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort_hoare(arr, low, high):
    if low < high:
        pivot_index = hoare_partition(arr, low, high)
        quickSort_hoare(arr, low, pivot_index)
        quickSort_hoare(arr, pivot_index + 1, high)


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == "__main__":
    n = int(input("enter the size of thr array:"))
    arr = list(map(int, input("enter the elements :").split()))
    sorted_arr = quickSort_naive(arr)
    print("sorted array_naive:", sorted_arr)
    quickSort_hoare(arr, 0, len(arr) - 1)
    print("sorted array_hoare:", arr)
    quickSort_lomuto(arr, 0, len(arr) - 1)
    print("sorted array_lomuto:", arr)
