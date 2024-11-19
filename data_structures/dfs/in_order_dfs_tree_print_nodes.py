from utils import Node

def printInOrder(root):
    if root is None:
        return
    printInOrder(root.left)
    print(root.val)
    printInOrder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print(printInOrder(root))