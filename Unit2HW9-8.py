class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        print("Available privileges include ",end="")
        for i in range (len(self.privileges) - 1):
            print (self.privileges[i].lower(), end = ", ")
        print("and " + self.privileges[len(self.privileges) - 1].lower())