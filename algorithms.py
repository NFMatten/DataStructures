
# Constant: O(1)
def odd_or_even(int_parameter):
    '''
    Task 1: Even or Odd 
        - Given a numeric value, determine if is is even or odd.
        - The function should take the value in as a parameter and return a boolean value (True if even, False if odd)
        - Leave a comment above the function stating the time complexity. (Big O notation) 
    '''
    if int_parameter % 2 == 0:
        return True
    else: 
        return False

print(odd_or_even(19)) # Odd; return false
print(odd_or_even(20)) # Even; return true

# Linear: O(n)
def less_than_hundred(list_parameter):
    '''
    Task 2: Less than 100
        - Given a list of numbers, determine if each item in the list is lower than 100
        - The function should take in the list as a parameter and return a boolean value (False if there are any numbers greater than 100, True if all numbers are less than 100)
        - Leave a comment above the function stating the time complexity. (Big O notation)
    '''
    for number in list_parameter:
        if number > 100:
            return False
    return True

list_with_above_100 = [3, 18, 27, 36, 45, 54, 63, 27, 81, 90, 99, 108]
list_with_below_100 = [3, 18, 27, 36, 45, 54, 63, 27, 81, 90, 99]

print(less_than_hundred(list_with_above_100)) # one element above 100; return false
print(less_than_hundred(list_with_below_100)) # all elements beloew 100; return true



# Quadratic: O(n^2)
def repeated_names(list_of_names):
    """
    Task 3: Repeated Names
        - Given a list of names, determine if any names are contained in the list more than once.
        - The function should take in the list as a paramenter and return a boolean value (True if there are any repeated names, False if no repeats)
        - Leave a comment above the function stating the time complexity (Big O notation)
    """
    
    for i in range(len(list_of_names)):
        for j in range(len(list_of_names)):
            if i == j:
                continue
            if list_of_names[i] == list_of_names[j]:
                return True
    return False

list_of_names_repeated = ["John", "Nik", "Aaron", "Nik"]
list_of_names_without = ["Nik", "John", "Adam", "Aaron"]

print(repeated_names(list_of_names_repeated)) # at least one element repeated; returns True
print(repeated_names(list_of_names_without)) # no elements repeated; returns False





# Quadratic: O(n^2)
def sort_list(num_list):
    """
    Task 4: Sort List
        - Given a list of numbers, manually sort the list into ascending order (may not use built in .sort() method)
        - Suggested strategy:
            - Starting with the first two numbers, compare them to see which is larger.
            - Place the lower number to the left and the higher number to the right.
            - Iterate through the list, checking each pair of numbers one at a time.
            - Repeat from the start until the entire list is sorted.
        - Leave a comment above the function stating the time complexity (Big O notation)
    """
    print(f"Unsorted list: {num_list}")
    iteration = 0
    swap = True
    while swap == True:
        swap = False
        for i in range(len(num_list) - 1):
            for j in range(len(num_list) - 1):
                if num_list[j] > num_list[j + 1]:
                    swap = True
                    placeholder = num_list[j]
                    num_list[j] = num_list[j+1]
                    num_list[j+1] = placeholder
                    iteration += 1
                    print(f"Iteration: {iteration} {num_list}")
    return num_list

list_to_sort = [3,0,1,8,7,2,5,4,6,9]
#list_to_sort = [0,1,2,3,4,5,6,7,8,9] # Test for optimized code: Best case scenario, listed already sorted - no need to run entire code
print(f"Sorted List: {sort_list(list_to_sort)}")