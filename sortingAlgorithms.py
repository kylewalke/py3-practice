# Complexity
# Worst Case O(n^2)
# Best Case O(n*log(n))
# Avg Case O(n*log(n))
# approach: Divide and Conquer
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
    quick_sort(arr, leftIndex + 1, end)
    quick_sort(arr, start, leftIndex - 1)
    return


# Complexity
# Worst Case O(n^2)
# Best Case O(n)
# Avg Case O(n^2)
# pretty bad tbh
def bubble_sort(unsorted_list):
    for x in range(len(unsorted_list)):
        swap_flag = False
        for y in range(len(unsorted_list) - 1):
            if (unsorted_list[y] > unsorted_list[y + 1]):
                swap_flag = True
                unsorted_list[y], unsorted_list[y + 1] = unsorted_list[y + 1], unsorted_list[y]
        if not swap_flag:
            break
    return


# Complexity
# Worst Case O(n*log(n))
# Best Case O(n*log(n))
# Avg Case O(n*log(n))
# also div and conquer
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    leftHalf = unsorted_list[:len(unsorted_list) // 2]
    rightHalf = unsorted_list[len(unsorted_list) // 2:]
    leftHalf = merge_sort(leftHalf)
    rightHalf = merge_sort(rightHalf)

    sortedList = []
    while len(leftHalf) >= 1 and len(rightHalf) >= 1:
        if leftHalf[0] > rightHalf[0]:
            sortedList.append(rightHalf[0])
            rightHalf.remove(rightHalf[0])
        else:
            sortedList.append(leftHalf[0])
            leftHalf.remove(leftHalf[0])
    while len(leftHalf) > 0:
        sortedList.append(leftHalf[0])
        leftHalf.remove(leftHalf[0])
    while len(rightHalf) > 0:
        sortedList.append(rightHalf[0])
        rightHalf.remove(rightHalf[0])
    return sortedList


# Complexity
# Worst Case O(nk)
# Best Case O(nk)
# Avg Case O(nk)
# k max val in array
def radix_sort(unsorted_list):
    print(f'{unsorted_list}')
