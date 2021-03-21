
class BinarySearchTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def createBinarySearchTree(ordered_list) -> BinarySearchTree:
    print(f'ordered_list, {ordered_list}')
    root = BinarySearchTree(ordered_list[0])
    for item in ordered_list[1:]:
        addNode(root, BinarySearchTree(item))
    return root


def addNode(root, node):
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            addNode(root.right, node)
    else:
        if root.left is None:
            root.left = node
        else:
            addNode(root.left, node)
    return

#In order traversal and printing of values
def printBSTAsc(root):
    if root.left is not None:
        printBSTAsc(root.left)
    print(f'{root.val}', end=",")
    if root.right is not None:
        printBSTAsc(root.right)


#reverse in-order traversal and printing of values
def printBSTDesc(root):
    if root.right is not None:
        printBSTDesc(root.right)
    print(f'{root.val}', end=",")
    if root.left is not None:
        printBSTDesc(root.left)


#pre-order traversal and printing of values
def printBSTPreorder(root):
    print(f'{root.val}', end=",")
    if root.left is not None:
        printBSTDesc(root.left)
    if root.right is not None:
        printBSTDesc(root.right)


#post-order traversal and printing of values
def printBSTPostorder(root):
    if root.left is not None:
        printBSTDesc(root.left)
    if root.right is not None:
        printBSTDesc(root.right)
    print(f'{root.val}', end=",")
