
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

    def find_node_recursively(self, current_node, value):
        '''
        Take in the root node as a parameter, and the value we're trying to find
        Check if the current node has any value assigned to it (if it's the tail.next node, it will be None and end the function)
        Check if the current node contains the value we're trying to find -> return True is so.
        Otherwise, move to the next node (recursively)
        If at the end of the function we don't find what we're looking for, return False.
        '''

        if current_node: 
            if current_node.value == value:
                return True
            else:
                return self.find_node_recursively(current_node.next, value)
        return False