class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_second_largest_int(root, largest, second_largest):
    if not root:
        return
    if root.val > largest:
        second_largest = largest
        largest = root.val
    find_second_largest_int(root.right, largest, second_largest)
    find_second_largest_int(root.left, largest, second_largest)
    return second_largest

def start_search(root):
    largest= 0
    second_largest = -1
    find_second_largest_int(root, largest, second_largest)
    

 

root = Node(7)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(3)
root.left.right = Node(5)

print(start_search(root))

