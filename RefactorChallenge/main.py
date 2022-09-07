from months import Months
from fruits_and_veggies import FruitsAndVeggies

def pi_day():
    check_pi_day = Months(3.14)
    print(check_pi_day.compare_num_to_month())

def fruits_and_veggies():
    # Creates new object
    new_obj = FruitsAndVeggies()
    # Prints set after adding new item
    print(new_obj.add_to_set("Apple"))
    print(new_obj.add_to_set("Orange"))
    # Discards item from set
    print(new_obj.discard_from_food_set("Apple"))
    # Prints set after set has been cleared
    print(new_obj.clear_food_set())
    # Add multiple items individually to set
    food_list = ["Peas", "Carrots"]
    print(new_obj.add_from_list(food_list))




def main():
    pi_day()
    fruits_and_veggies()    


main()


