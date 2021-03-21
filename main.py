import treeAlgorithms as treeAlg

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = treeAlg.createBinarySearchTree([2, 3, 5, 1, 4, 6, 8, 7])
    print('Asc:')
    treeAlg.printBSTAsc(x)
    print('\nDesc:')
    treeAlg.printBSTDesc(x)
    print('\nPreOrder:')
    treeAlg.printBSTPreorder(x)
    print('\nPostOrder:')
    treeAlg.printBSTPostorder(x)
