
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append_node(self, value_to_add):
        new_node = Node(value_to_add)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
            return
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_node(self, node_to_find):
        current_node = self.head
        print("Searching Linked List for Node:", node_to_find)
        while current_node != None:
            if current_node.value == node_to_find:
                return True
            else:
                current_node = current_node.next
        return False