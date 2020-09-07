class TreeNode:
    def __init__(self, name, desg):
        self.name = name
        self.desg = desg
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, typ):
        if typ == "name":
            value = self.name
        elif typ == "both":
            value = self.name + " (" + self.desg + ")"
        else:
            value = self.desg

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__"  if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(typ)


def build_management_tree():
    root = TreeNode("Nilpul", "CEO")
    cto = TreeNode("Chinmay", "CTO")
    infra = TreeNode("Vishwa", "Infrastructure Head")
    infra.add_child(TreeNode("Dhaval", "Cloud Manager"))
    infra.add_child(TreeNode("Abhijit", "App Manager"))
    cto.add_child(infra)

    hr = TreeNode("Gels", "HR Head")
    hr.add_child(TreeNode("Peter", "Recruitment Manager"))
    hr.add_child(TreeNode("Waqas", "Policy Manager"))

    root.add_child(cto)
    root.add_child(hr)

    return root


if __name__ == "__main__":
    root_node = build_management_tree()

    print("Hierarchy - Name")
    root_node.print_tree("name")    # prints only name hierarchy

    print("\nHierarchy - Designation")
    root_node.print_tree("designation") # prints only designation hierarchy

    print("\nHierarchy - Both (Name and Designation)")
    root_node.print_tree("both")    # prints both (name and designation) hierarchy
