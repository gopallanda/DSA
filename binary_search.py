def binarySearch(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    n = int(input("enter size of array:"))
    arr = list(map(int, input("enter element:").split()))
    target = int(input("enter target:"))
    res = binarySearch(arr, target)
    print("element is found at index at:", res)
