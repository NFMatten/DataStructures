import implementation
from linked_list import LinkedList
from binary_node import BinaryNode

# ## Task: Dictionary, set, tuples ##
# def main():
#     implementation.months_pi_day()
#     implementation.fruits_and_veggies()
#     implementation.user_profile()
#     implementation.print_family()




# ## Linked List ## 

# def create_linked_list():
#     linked_list = LinkedList()
#     linked_list.append_node(55)
#     linked_list.append_node(48)
#     linked_list.append_node(405)
#     linked_list.append_node(32)
#     linked_list.append_node(45)
#     return linked_list

# def find_node_in_linked_list():
#     linked_list = create_linked_list()
#     print(linked_list.find_node(55)) # Find first node
#     print(linked_list.find_node(405)) # Find middle node
#     print(linked_list.find_node(45)) # Find last node
#     print(linked_list.find_node(100000)) # Find nonexistant node

# def main():
#     find_node_in_linked_list()
#     linked_list = create_linked_list()
#     print(linked_list.find_node_recursively(linked_list.head, 45)    


## Binary Search Tree ##

def create_and_print_bst():
    print("\n\n===== Binary TreeL Insertion Activity =====")
    root = BinaryNode(27)
    print(root.insert_node(14))
    print(root.insert_node(35))
    print(root.insert_node(10))
    print(root.insert_node(19))
    print(root.insert_node(31))
    print(root.insert_node(42))

def main():
    """
    Add 5 nodes to the tree (make sure to go in both directions for testing).
    Search for a node in the tree
    Make sure to consistently drop a breakpoint and step through both methods to ensure it is working properly.
    """
    create_and_print_bst()




if __name__ == "__main__":
    main()