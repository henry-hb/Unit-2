"""
Name: Henry Hall-Brown
Date: 3/6/2025
Description: Unit 2 HW 2
"""

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """
        creates new restaurant object

        Args:
            restaurant_name (str): name of restaurant
            cuisine_type (str): type of food served at restaurant
            number_served (int): how many customers have been served
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """
        prints description of restaurant including its name and what kind of food it serves
        """
        print(f"Restaurant name: {self.restaurant_name}\nRestaurant cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """
        prints the name of the restaurant and that it is open
        """
        print(f"{self.restaurant_name} is open")
    
    def set_number_served(self, new_value):
        """
        updates number_served to whatever the new value is
        """
        if(new_value > self.number_served):
            self.number_served = new_value
        else:
            print("You cannot reduce the amount of people you've served!")
    
    def increment_number_served(self, increment):
        """
        adds increment to whatever the current value of number_served is
        """
        self.number_served += increment
    
class User:
    def __init__(self, first_name: str, last_name: str):
        """
        creates new user object

        Args:
            first_name (str): first name of user
            last_name (str): last name of user
            login_attempts (int): how many times the user has logged in
        """
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        """
        prints description of user including first and last name, height (in inches) and their current mood
        """
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}")

    def greet_user(self):
        """
        prints a greeting to the user with their first and last name
        """
        print(f"Welcome {self.first_name}!")

    def increment_login_attempts(self):
        """
        increments login_attempts by 1
        """
        self.login_attempts += 1

    def reset_login_attempts(self):
        """
        sets login_attempts to 0
        """
        self.login_attempts = 0

def main():
    restaurant_one = Restaurant("Wendy's", "Fast Food")
    restaurant_one.describe_restaurant()
    print(restaurant_one.number_served)
    restaurant_one.number_served = 10
    print(restaurant_one.number_served)
    restaurant_one.set_number_served(30)
    print(restaurant_one.number_served)
    restaurant_one.increment_number_served(300)
    print(restaurant_one.number_served)
    print("")

    user_one = User("Henry","Hall-Brown")
    user_one.describe_user()
    print(user_one.login_attempts)
    for i in range(12):
        user_one.increment_login_attempts()
    print(user_one.login_attempts)
    user_one.reset_login_attempts()
    print(user_one.login_attempts)


if __name__ == "__main__":
    main()
