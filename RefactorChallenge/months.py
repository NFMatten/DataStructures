from math import pi

class Months:
    def __init__(self, number):
        self.months = self.months_list()
        self.num_to_compare = number

    def months_list(self):
        months_tuple = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        return months_tuple

    def number_rounded(self):
        return round(self.num_to_compare)

    def compare_num_to_month(self):
        num_rounded = self.number_rounded()
        for index in range(len(self.months)):
            if (index - 1) == num_rounded:
                return f"{self.num_to_compare} day is in {self.months[index]}"