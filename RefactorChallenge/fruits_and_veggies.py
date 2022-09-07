

class FruitsAndVeggies:
    def __init__(self):
        self.set_of_food = set()

    def add_to_set(self, food):
        """
        Parameter: food -> string
        """
        self.set_of_food.add(food)
        return self.set_of_food

    def clear_food_set(self):
        self.set_of_food.clear()
        return self.set_of_food

    def discard_from_food_set(self, food):
        """
        Parameter: food -> string
        """
        self.set_of_food.discard(food)
        return self.set_of_food

    def add_from_list(self, food):
        """
        Parameter: food -> list
        """
        for item in food:
            self.set_of_food.add(item)
        return self.set_of_food