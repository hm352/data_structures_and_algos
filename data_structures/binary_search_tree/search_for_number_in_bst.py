from data_structures.dfs.utils import Node

# class Node():
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def search_for_number_in_bst(root, n):
    if root is None:
        return
    if root.val == n:
        return True
    if root.left and root.left.val > n:
        search_for_number_in_bst(root.right, n)
    if root.right and root.right.val < n:
        search_for_number_in_bst(root.left, n)

if __name__ == "__main__":
    root = Node(6)
    root.left = Node(2)
    root.right = Node(8)
    root.right.left = Node(7)
    root.right.right = Node(9)

    print(search_for_number_in_bst(root, 8))