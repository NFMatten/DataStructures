from linked_list import LinkedList



#import implementation

# # Task: Dictionary, set, tuples
# def main():
#     implementation.months_pi_day()
#     implementation.fruits_and_veggies()
#     implementation.user_profile()
#     implementation.print_family()


# main()





def create_linked_list():
    linked_list = LinkedList()
    linked_list.append_node(55)
    linked_list.append_node(48)
    linked_list.append_node(405)
    linked_list.append_node(32)
    linked_list.append_node(45)
    return linked_list

def find_node_in_linked_list():
    linked_list = create_linked_list()
    print(linked_list.find_node(55)) # Find first node
    print(linked_list.find_node(405)) # Find middle node
    print(linked_list.find_node(45)) # Find last node
    print(linked_list.find_node(100000)) # Find nonexistant node

def main():
    find_node_in_linked_list()
    


if __name__ == "__main__":
    main()