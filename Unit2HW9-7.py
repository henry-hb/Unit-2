"""
Name: Henry Hall-Brown

9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator's set of
privileges. Create an instance of Admin, and call your method.
"""
from Unit2HW9-8 import privileges
class User:
    def __init__(self, first_name: str, last_name: str):
        """
        creates new user object

        Args:
            first_name (str): first name of user
            last_name (str): last name of user
        """
        self.first_name = first_name
        self.last_name = last_name
    
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
    
class Admin(User):
    def __init__(self, first_name: str, last_name: str, privileges):
        super().__init__(first_name, last_name)
        self.privileges = privileges
    
    def show_privileges(self):
        print("Available privileges include ",end="")
        for i in range (len(self.privileges) - 1):
            print (self.privileges[i].lower(), end = ", ")
        print("and " + self.privileges[len(self.privileges) - 1].lower())

def main():
    admin = Admin("Henry", "Hall-Brown", ["Can hack everything", "Free stuff at vending machines", "Can make dinosaur game work on school computers"])
    admin.show_privileges()

if __name__ == "__main__":
    main()