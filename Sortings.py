# Bubble sort
# class Base:
#     def BubbleSort(self,arr):
#         n=len(arr)
#         for i in range(n):
#             for j in range(n-i-1):

#                 if arr[j]>arr[j+1]:
#                     arr[j],arr[j+1]=arr[j+1],arr[j]
#         return arr
# obj=Base()
# arr=[9,4,7,1,5,7,4]
# print(obj.BubbleSort(arr))

# Selection sort

# class Base:
#     def selectionSort(self,arr):
#         n=len(arr)
#         for i in range(n):
#             min_idx=i
#             for j in range(i+1,n):
#                 if arr[j]<arr[min_idx]:
#                     min_idx=j
#                     arr[i],arr[min_idx]=arr[min_idx],arr[i]
#         return arr

# arr=[7,1,5,9,3,8]
# obj=Base()
# print(obj.selectionSort(arr))

# Quick sort

# class QuickSort:
#     def partition(self, arr, low, high):
#         pivot = arr[high]
#         i = low - 1
#         for j in range(low, high):
#             if arr[j] < pivot:
#                 i += 1
#                 self.swap(arr, i, j)
#         self.swap(arr, i + 1, high)
#         return i + 1

#     def swap(self, arr, i, j):
#         arr[i], arr[j] = arr[j], arr[i]

#     def quickSort(self, arr, low, high):
#         if low < high:
#             pi = self.partition(arr, low, high)
#             self.quickSort(arr, low, pi - 1)
#             self.quickSort(arr, pi + 1, high)


# obj = QuickSort()
# arr=[10,80,30,90,40,50,70]
# obj.quickSort(arr,0,len(arr)-1)
# print(arr)

# merge sort
# class Base:
#     def mergeSort(self,arr):
#         if len(arr)>1:
#             mid=len(arr)//2
#             left_half=arr[:mid]
#             right_half=arr[mid:]
#             self.mergeSort(left_half)
#             self.mergeSort(right_half)
#             self.merge(arr,left_half,right_half)
#     def merge(self,arr,left_half,right_half):
#         i=j=k=0
#         while i<len(left_half) and j<len(right_half):
#             if left_half[i]<right_half[j]:
#                 arr[k]=left_half[i]
#                 i+=1
#             else:
#                 arr[k]=right_half[j]
#                 j+=1
#             k+=1
#         while i <len(left_half):
#             arr[k]=left_half[i]
#             i+=1
#             k+=1
#         while j<len(right_half):
#             arr[k]=right_half[j]
#             j+=1
#             k+=1
# obj=Base()
# arr=[4,2,7,2,5,8,9,5,1]
# print("array before sorting:",arr)
# obj.mergeSort(arr)
# print("array after sorting:",arr)

# recursive bubble sort
# def bubbleSort(self,arr,n=None):
#         # code here
#         if n==None:
#             n=len(arr)
#         if n==1:
#             return
#         for i in range(n-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#         self.bubbleSort(arr,n-1)
#         return arr

# insertion sort
# def insertion_sort(arr):
#     # Traverse through 1 to len(arr)
#     for i in range(1, len(arr)):
#         key = arr[i]  # Current element to be placed correctly
#         j = i - 1

#         # Move elements of arr[0..i-1] that are greater than `key`
#         # to one position ahead of their current position
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1

#         arr[j + 1] = key  # Place `key` at its correct position

# # Example usage
# arr = [12, 11, 13, 5, 6]
# insertion_sort(arr)
# print("Sorted array:", arr)  # Output: [5, 6, 11, 12, 13]


# recursive insertion sort
# def recursive_insertion_sort(arr, n=None):
#     if n is None:
#         n = len(arr)  # Initialize `n` if not provided

#     # Base case: If array has only one element, it's already sorted
#     if n <= 1:
#         return

#     # Recursively sort the first `n-1` elements
#     recursive_insertion_sort(arr, n - 1)

#     # Insert the nth element into the sorted sequence
#     key = arr[n - 1]  # Last element
#     j = n - 2

#     # Shift elements of arr[0..n-2] that are greater than `key`
#     while j >= 0 and arr[j] > key:
#         arr[j + 1] = arr[j]  # Move element one position ahead
#         j -= 1

#     arr[j + 1] = key  # Place key at its correct position


# # Example usage
# arr = [12, 11, 13, 5, 6]
# recursive_insertion_sort(arr)
# print("Sorted array:", arr)  # Output: [5, 6, 11, 12, 13]


def mergeSort(arr):
    n = len(arr)
    if n > 1:
        mid = n // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


if __name__ == "__main__":
    size = int(input())
    user_input = input()  # 1
    print(user_input, type(user_input))
    split_user = user_input.split()  # 2
    print(split_user, type(split_user))
    arr = list(map(int, split_user))  # 3 map(function, iterable)
    # arr = list(map(int, input().split()))  1,2,3 IN ONE LINE
    mergeSort(arr)
    print(arr)  # space after comma [1, 3, 5, 6, 7, 8, 8] (default list)
    string_map = map(str, arr)  # 4
    joins = ",".join(string_map)  # 5
    res = "[" + joins + "]"  # 6
    print(res)  # without space after comma [1,3,5,6,7,8,8]
    # print("[" + ",".join(map(str, arr)) + "]") # 4,5,6 in one line
