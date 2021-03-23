import treeAlgorithms as treeAlg
import sortingAlgorithms as sortAlg

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unsortedArray = [2, 3, 5, 1, 4, 6, 8, 7]

    #Tree Algs
    x = treeAlg.createBinarySearchTree(unsortedArray)
    print('Asc:')
    treeAlg.printBSTAsc(x)
    print('\nDesc:')
    treeAlg.printBSTDesc(x)
    print('\nPreOrder:')
    treeAlg.printBSTPreorder(x)
    print('\nPostOrder:')
    treeAlg.printBSTPostorder(x)

    #Sorting Algs
    b = [2, 3, 5, 1, 4, 6, 8, 7]
    sortAlg.quick_sort(b, 0, len(b)-1)
    print(f'\nQuick Sort: {b}')

    b = [2, 3, 5, 1, 4, 6, 8, 7]
    sortAlg.bubble_sort(b)
    print(f'Bubble Sort: {b}')

    b = [2, 3, 5, 1, 4, 6, 8, 7]
    b = sortAlg.merge_sort(b)
    print(f'Merge Sort: {b}')

    b = [2, 3, 5, 1, 4, 6, 8, 7]
    sortAlg.radix_sort(b)
    print(f'Radix Sort: {b}')

