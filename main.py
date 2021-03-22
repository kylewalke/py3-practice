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

    sortAlg.bubble_sort([2, 3, 5, 1, 4, 6, 8, 7])
    print('Bubble Sort: ')

    sortAlg.merge_sort([2, 3, 5, 1, 4, 6, 8, 7])
    print('Merge Sort: ')

    sortAlg.radix_sort([2, 3, 5, 1, 4, 6, 8, 7])
    print('Radix Sort: ')

