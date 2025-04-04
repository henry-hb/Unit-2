"""
Name: Henry Hall-Brown

9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method.
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
        print(f"Restaurant name: {self.restaurant_name}\nRestaurant cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """
        prints the name of the restaurant and that it is open
        """
        print(f"{self.restaurant_name} is open")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = flavors

    def print_flavors(self):
        print("The available flavors are ",end="")
        for i in range (len(self.flavors) - 1):
            print (self.flavors[i], end = ", ")
        print("and " + self.flavors[len(self.flavors) - 1])

def main():
    handels = IceCreamStand("Handels", "Ice Cream", ["Vanilla", "Chocolate", "Cookies and Cream", "Strawberry"])
    print(handels.flavors)
    handels.print_flavors()

if __name__ == "__main__":
    main()