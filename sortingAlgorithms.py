
# Complexity
# Worst Case O(n^2)
# Best Case O(n)
# Avg Case O(n*log(n))
#approach: Divide and Conquer
def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[end]
    leftIndex = start
    rightIndex = end - 1
    while True:
        while leftIndex <= rightIndex and arr[leftIndex] <= pivot:
            leftIndex += 1
        while leftIndex <= rightIndex and arr[rightIndex] >= pivot:
            rightIndex -= 1
        if leftIndex < rightIndex:
            arr[leftIndex], arr[rightIndex] = arr[rightIndex], arr[leftIndex]
        else:
            break
    arr[end], arr[leftIndex] = arr[leftIndex], arr[end]
    quick_sort(arr, leftIndex+1, end)
    quick_sort(arr, start, leftIndex-1)
    return


# Complexity
# Worst Case O(n^2)
# Best Case O(n)
# Avg Case O(n*log(n))
def bubble_sort(unsorted_list):
    print(f'{unsorted_list}')


# Complexity
# Worst Case O(n^2)
# Best Case O(n)
# Avg Case O(n*log(n))
def merge_sort(unsorted_list):
    print(f'{unsorted_list}')


# Complexity
# Worst Case O(n^2)
# Best Case O(n)
# Avg Case O(n*log(n))
def radix_sort(unsorted_list):
    print(f'{unsorted_list}')
