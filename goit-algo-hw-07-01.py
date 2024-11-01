class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root: Node, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def min_value_node(node: Node):
    current = node
    while current.left:
        current = current.left
    return current

def max_value_node(node: Node):
    current = node
    while current.right:
        current = current.right
    return current

def total_tree_value(node: Node):
    if node is None:
        return 0
    else:
        return (total_tree_value(node.left)) + node.val + (total_tree_value(node.right))

root = Node(4)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 5)
root = insert(root, 2)

print(root)
print(f"Max value = {max_value_node(root).val}")
print(f"Min value = {min_value_node(root).val}")
print(f"Total tree value = {total_tree_value(root)}")

