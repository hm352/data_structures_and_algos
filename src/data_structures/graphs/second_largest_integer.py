from data_structures.utils.graph_node import GraphNode

# class GrahpNode:
#     def __init__(self, val):
#         self.val = val
#         self.children = []

def in_order_search(root, largest, second_largest):
    if not root:
        return
    
    if root.val > largest[0]:
        second_largest[0] = largest[0]
        largest[0] = root.val
    
    elif root.val > second_largest[0] and root.val < largest[0]:
        second_largest[0] = root.val
    
    [
        in_order_search(child, largest, second_largest) 
        for child in root.children
    ]

def find_second_largest_node(root):
    largest = [-1]
    second_largest = [-1]
    in_order_search(root, largest, second_largest)
    return second_largest

if __name__ == "__main__":

  # Representation of given N-ary tree
  #         11
  #       /  |  \
  #     21   29  90
  #    /    /  \   \
  #   18   10  12  77
  
  root = GrahpNode(11)
  root.children.append(GrahpNode(21))
  root.children.append(GrahpNode(29))
  root.children.append(GrahpNode(90))
  root.children[0].children.append(GrahpNode(18))
  root.children[1].children.append(GrahpNode(10))
  root.children[1].children.append(GrahpNode(12))
  root.children[2].children.append(GrahpNode(77))

  print(find_second_largest_node(root))