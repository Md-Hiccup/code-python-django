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

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()
        elements.append(self.data)
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    # 1. Finds minimum elements in entire binary tree
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    # 2. Finds maximum elements in entire binary tree
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # 3. Calculate sum of all elements
    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    # 4. Perform post order traversal of a binary tree
    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()
        elements.append(self.data)
        return elements

    # 5. Perform pre order traversal of a binary tree
    def pre_order_traversal(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements


def build_tree(elements):
    print("Building binary search tree")
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
    inOrderTraverse = numbers_tree.in_order_traversal()
    print("In-Order Traversal: ", inOrderTraverse)

    # 1. finding min
    findMin = numbers_tree.find_min()
    print("Minimum element: ", findMin)

    # 2. finding max
    findMax = numbers_tree.find_max()
    print("Maximum element: ", findMax)

    # 3. calculate sum of all elements
    calculateSum = numbers_tree.calculate_sum()
    print("Total sum of elements: ", calculateSum)

    # 4. Post-order traversal
    postOrderTraverse = numbers_tree.post_order_traversal()
    print("Post-Order Traversal: ", postOrderTraverse)

    # 5. Pre-order traversal
    preOrderTraverse = numbers_tree.pre_order_traversal()
    print("Pre-Order Traversal: ", preOrderTraverse)

