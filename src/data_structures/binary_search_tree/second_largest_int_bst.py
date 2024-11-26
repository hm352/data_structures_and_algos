# Given a Binary Search Tree, the task is to find the second largest element in the given BST.

from ..dfs.utils import Node

# class Node():
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def reverse_in_order_traversal(root, n, result):
    # We have instatiated a counter variable and a 
    # result variable that we alter when we have traversed
    # all the right most nodes
    if not root or n[0] >= 2:
        return
    
    reverse_in_order_traversal(root.right, n, result)
    print('----------------')
    print(n)
    print(root.val)
    print('----------------')
    n[0] += 1
    
    if n[0] == 2:
        result[0] = root.val
        return result
    
    reverse_in_order_traversal(root.left, n, result)

def second_largest_integer(root):
    # This requires the use of a memory type List to work apparently
    # For some reason when passing through with integers doesn't work in the same way
    # although understand the general pricinples of what this algorithm is doing

    # REVERSE IN ORDER TRAVERSAL
    
    result = [-1]
    n = [0]
    print(reverse_in_order_traversal(root, n, result))


if __name__ == "__main__":
    # Representation of the input BST:
    #              7
    #             / \
    #            4   8
    #           / \   
    #          3   5 

    root = Node(7)
    root.left = Node(4)
    root.right = Node(8)
    root.left.left = Node(3)
    root.left.right = Node(5)
    second_largest_integer(root)