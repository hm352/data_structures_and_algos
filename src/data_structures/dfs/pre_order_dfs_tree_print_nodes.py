# Visit the root
# Traverse the left subtree, i.e., call Preorder(left-subtree)
# Traverse the right subtree, i.e., call Preorder(right-subtree)

from utils import Node

def print_preorder(root):
    if root:
        print(root.val)
        print_preorder(root.left)
        print_preorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print_preorder(root)