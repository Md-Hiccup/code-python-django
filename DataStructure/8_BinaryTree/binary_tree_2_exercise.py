class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, child):
        if child == self.data:
            return
        if child < self.data:
            if self.left:
                self.left.add_child(child)
            else:
                self.left = BinarySearchTreeNode(child)
        if child > self.data:
            if self.right:
                self.right.add_child(child)
            else:
                self.right = BinarySearchTreeNode(child)

    def search(self, val):
        if self.data == val:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            max_val = self.left.find_max()
            self.data = max_val
            self.left = self.left.delete(max_val)

        return self


def build_tree(elements):
    print("Build binary search tree")
    root = BinarySearchTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root

if __name__ == "__main__":
    """
                         17
                    4           20
                1       9   18      23
                                        34
    """
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("Tree: ", numbers_tree.in_order_traversal())

    maxVal = numbers_tree.find_max()
    print("Max val: ", maxVal)

    delVal = numbers_tree.delete(20)
    print("After deleting : ", delVal.in_order_traversal())


