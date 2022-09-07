# WIP

class UserProfile:

    def __init__(self):
        self.first_name = self.input_first_name()
        self.last_name = self.input_last_name()
        self.email_address = self.input_email()
        self.phone_number = self.input_phone()
        
    def build_dictionary(self):
        profile = {
            "first_name" : self.first_name,
            "last_name" : self.last_name,
            "email_address" : self.email_address,
            "phone_number" : self.phone_number
        }
        return profile
    
    def input_first_name(self):
        first_name = input("Please enter your first name: ")
        return first_name

    def input_last_name(self):
        last_name = input("Please enter your last name: ")
        return last_name

    def input_email(self):
        email_address = str(input("Please enter your email address: "))
        return email_address

    def input_phone(self):
        phone_number = int(input("Please enter your phone number: "))
        return phone_number