#create unique methods for each class
#add documentation
"""
Henry Hall-Brown
Period 5
Unit 2 Take Home Test Portion
"""
class Plant:
    garden_size = 0
    def __init__(self, name, scientific_name, age = 0):
        self.name = name
        self.scientific_name = scientific_name
        self.__age = age
        Plant.garden_size += 1
    
    def __repr__(self):
        return f"Name: {self.name} ({self.scientific_name}) Age: {self.__age} years old."
    
    def __eq__(self, other):
        if (self.name == other.name and self.scientific_name == other.scientific_name and self.__age == other.__age):
            return True
        return False
    
    def water(self):
        print(f"Your {self.name} is feeling well watered.")
        
    def get_age(self):
        return self.__age

class Spider_Plant(Plant):
    def __init__(self, name, scientific_name, age, num_plants):
        #num_plants is how many times the spider plant has reproduced another spider plant from one of its ends
        super().__init__(name, scientific_name, age)
        self.num_plants = num_plants
    
    def __repr__(self):
        return f"Name: {self.name} ({self.scientific_name}) Age: {self.__age} years old. {self.num_plants - 1} offshoots."

    def __eq__(self, other):
        if (self.name == other.name and self.scientific_name == other.scientific_name and self.__age == other.__age and self.num_plants == other.num_plants):
            return True
        return False
    
    def __add__(self,other):
        return self.num_plants + other.num_plants
    
class Succulent(Plant):
    def __init__(self, name, scientific_name, age, bears_fruit: bool):
        super().__init__(name, scientific_name, age)
        self.bears_fruit = bears_fruit
    
    def __repr__(self):
        if(self.bears_fruit):
            return f"Name: {self.name} ({self.scientific_name}) Age: {self.__age} years old. Bears fruit."
        else:
            return f"Name: {self.name} ({self.scientific_name}) Age: {self.__age} years old. Does not bear fruit."

    def __eq__(self, other):
        if (self.name == other.name and self.scientific_name == other.scientific_name and self.__age == other.__age and self.bears_fruit == other.bears_fruit):
            return True
        return False
    
    def water(self):
        print(f"Make sure not to water your {self.name} too much!")

def main():
    plant1 = Plant("tree", "genus species", 12)
    print(plant1)
    plant1.water()
    plant2 = Plant("tree", "genus species", 12)
    print(plant2)
    print(plant1 == plant2)
    spider1 = Spider_Plant("Young Spider Plant","Chlorophytum comosum", 1, 1)
    print(spider1)
    spider1.water()
    spider2 = Spider_Plant("Old Spider Plant", "Chlorophytum comosum", 30, 12)
    print(spider2)
    print(spider1 + spider2)
    succ1 = Succulent("Aloe Vera", "Aloe barbadensis Miller", 100, False)
    print(succ1)
    succ1.water()
    print(Plant.garden_size)

if __name__ == "__main__":
    main()