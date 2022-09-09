"""
Task 1: Dictionary, Set, Tuple
Given the following three scenarios, choose the best data structure (between a dictionary, set, or tuple) to 
efficiently store the data. Each scenario ties directly to one data structure. Each data structure will be used only once. 
You will need to determine which data structure is best for which scenario, and then implement the data structure in Python

"""

def months_pi_day():
    """
    Store the months of the year as strings. Determine the month in the data structure in which National Pi Day exists and print that month to the console. 
        HINT: The number for Pi, when converted to an Integer, is related to the stored location of the correct month.
    """
    months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
    pi = 3.14
    print("\nTask Pi Day:")
    for index in range(len(months)):
        if (index - 1) == round(pi):
            print(f"Pi day is in the month of {months[index]}")


def fruits_and_veggies():
    """
    Store five fruits or vegetables.
        Add two of your favorite fruits and two of your favorite vegetables to the collection.
        Iterate over the collection and print each one to the console. 
    """
    print("\nTask Fruits and Veggies:")
    fru_veg_set = {"apple", "orange", "banana", "carrot", "peas"}
    fru_veg_set.update(["pineapple", "kiwi"])
    fru_veg_set.update(["broccoli", "green beans"])
    for items in fru_veg_set:
        print(items)


def user_profile():
    """
    Store information about a user profile. Use literal string interpolation to print the user’s profile information to the console. 
    The profile should consist of the following information:
        First Name
        Last Name
        Email Address
        Phone Number
    """
    print("\nTask User Profile:")
    profile = {
        'first_name': 'Nik',
        'last_name' : 'Matten',
        'email_address' : 'nik@matten.com',
        'phone_number' : 1234567890
    }
    print(f"First Name: {profile['first_name']}")
    print(f"Last Name: {profile['last_name']}")
    print(f"Email Address: {profile['email_address']}")
    print(f"Phone number: {profile['phone_number']}")

"""
Task 2: List of Dictionaries
Use a list to store the dictionary of your immediate family members, with each index 
of the list storing its own dictionary. Dictionary should contain the following keys:
    First name
    Last name
    Relation to you
"""

def list_of_dictionaries():
    family_list = [
        {
            "first_name" : "first name",
            "last_name" : "last name",
            "relation" : "Sister"
        },
        {
            "first_name" : "first name",
            "last_name" : "last name",
            "relation" : "Sister"
        },
        {
            "first_name" : "first name",
            "last_name" : "last name",
            "relation" : "Wife"
        }
    ]
    return family_list

def print_family():
    """
    Once you have stored the List of Dictionary items, write a function/method that will iterate 
    over the List and print off the First Name and Relation of each person in the List.
    """
    print("\nTask Family Members:")
    family_list = list_of_dictionaries()
    for index in family_list:
        first_name = index['first_name']
        relation = index['relation']
        print(f'{first_name} {relation}')
    print("")