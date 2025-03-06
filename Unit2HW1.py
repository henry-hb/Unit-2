"""
Name: Henry Hall-Brown
Date: 3/6/2025
Description: Unit 2 HW 1
"""

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_type: str):
        """
        creates new restaurant object

        Args:
            restaurant_name (str): name of restaurant
            cuisine_type (str): type of food served at restaurant
        """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """
        prints description of restaurant including its name and what kind of food it serves
        """
        print(f"{self.restaurant_name} is a restaurant that serves {self.cuisine_type}.")

    def open_restaurant(self):
        """
        prints the name of the restaurant and that it is open
        """
        print(f"{self.restaurant_name} is open!")
    
class User:
    def __init__(self, first_name: str, last_name: str, height: int, mood: str):
        """
        creates new user object

        Args:
            first_name (str): first name of user
            last_name (str): last name of user
            height (int): height of user (in inches)
            mood (str): current mood of user
        """
        self.first_name = first_name
        self.last_name = last_name
        self.height = height
        self.mood = mood
    
    def describe_user(self):
        """
        prints description of user including first and last name, height (in inches) and their current mood
        """
        print(f"{self.first_name} {self.last_name} is {self.height} inches and is currently {(self.mood).lower()}.")

    def greet_user(self):
        """
        prints a greeting to the user with their first and last name
        """
        print(f"Hello {self.first_name} {self.last_name}!")

def main():
    restaurant_one = Restaurant("Wendy's", "Fast Food")
    restaurant_two = Restaurant("Tony's", "Pizza")
    restaurant_three = Restaurant("Buster's", "BBQ")
    restaurant_one.describe_restaurant()
    restaurant_one.open_restaurant()
    restaurant_two.describe_restaurant()
    restaurant_two.open_restaurant()
    restaurant_three.describe_restaurant()
    restaurant_three.open_restaurant()
    print("")
    user_one = User("Henry", "Hall-Brown", "72", "Hungry")
    user_two = User("Brandon", "Smith", "66", "Happy")
    user_three = User("JT", "Nugent", "78", "Sleepy")
    user_one.describe_user()
    user_one.greet_user()
    user_two.describe_user()
    user_two.greet_user()
    user_three.describe_user()
    user_three.greet_user()

if __name__ == "__main__":
    main()
