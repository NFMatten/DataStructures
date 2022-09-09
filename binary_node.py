
class BinaryNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    # Insert a node into the tree
    def insert_node(self, value_to_add):
        if value_to_add < self.data:
            if self.left is None:
                self.left = BinaryNode(value_to_add)
                print(f'{value_to_add} Node updated with a left, with a right of {BinaryNode.right}')
            else:
                self.left.insert_node(value_to_add)
                print(f'{value_to_add} Node updated with a left, with a right of {BinaryNode.right}')

        elif value_to_add > self.data:
            if self.right is None:
                self.right = BinaryNode(value_to_add)
                print(f'{value_to_add} Node updated with a right, with a left of {BinaryNode.left}')
            else:
                self.left.insert_node(value_to_add)
                print(f'{value_to_add} Node updated with a right, with a left of {BinaryNode.left}')
        else:
            self.data = value_to_add

                

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

