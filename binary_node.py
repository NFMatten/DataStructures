
class BinaryNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    # Insert a node into the tree
    def insert_node(self, root, value_to_add):
        if root is None:
            return BinaryNode(value_to_add)
        else:
            if root.data <= value_to_add:
                print(f"{value_to_add} inserted as child of {root.data} to the right")
                root.right = self.insert_node(root.right, value_to_add)
            else:
                print(f"{value_to_add} inserted as child of {root.data} to the left")
                root.left = self.insert_node(root.left, value_to_add)
            return root

                

    # Search for a specific node in the tree. Value to be searched by should be passed into the method.
    def search_for_node(self, value_to_search):
        current_node = self.data

        while current_node != None:
            if value_to_search < current_node:
                current_node = self.left
            elif value_to_search > current_node:
                current_node = self.right
            else:
                return True
        return False

