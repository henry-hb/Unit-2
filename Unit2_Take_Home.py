#add documentation
'''
Name: Henry Hall-Brown
Date: 4/20/25
File: Unit2_Take_Home.py
Description: A program that creates a garden with a few available plant types.
'''

class Plant:
    garden_size = 0
    def __init__(self, name, scientific_name, age = 0):
        self.name = name
        self.scientific_name = scientific_name
        self.__age = age
        Plant.garden_size += 1
    
    def __str__(self):
        return f"Name: {self.name} ({self.scientific_name}) Age: {self.get_age()} years old."
    
    def __eq__(self, other):
        if (self.name == other.name and self.scientific_name == other.scientific_name and self.get_age() == other.get_age()):
            return True
        return False
    
    def water(self):
        print(f"Your {self.name} is feeling well watered.")
        
    def get_age(self):
        return self.__age
    
    def increment_age(self):
        self.__age += 1

    def prune_plant(self, age):
        #age must be lower than current age
        #a bit of a stretch to say that pruning is making a plant younger whoops
        if age < self.get_age():
            self.__age = age
        else:
            print("Cannot make the plant older!")

class Spider_Plant(Plant):
    def __init__(self, name, scientific_name, age, num_plants):
        #num_plants is how many times the spider plant has reproduced another spider plant from one of its ends
        super().__init__(name, scientific_name, age)
        self.num_plants = num_plants
    
    def __str__(self):
        return f"Name: {self.name} ({self.scientific_name}) Age: {self.get_age()} years old. {self.num_plants - 1} offshoots."

    def __eq__(self, other):
        if (self.name == other.name and self.scientific_name == other.scientific_name and self.get_age() == other.get_age() and self.num_plants == other.num_plants):
            return True
        return False
    
    def __add__(self,other):
        #spider plants add on to each other's ends
        return self.num_plants + other.num_plants - 2
    
class Succulent(Plant):
    def __init__(self, name, scientific_name, age, bears_fruit: bool):
        super().__init__(name, scientific_name, age)
        self.bears_fruit = bears_fruit
    
    def __str__(self):
        if(self.bears_fruit):
            return f"Name: {self.name} ({self.scientific_name}) Age: {self.get_age()} years old. Bears fruit."
        else:
            return f"Name: {self.name} ({self.scientific_name}) Age: {self.get_age()} years old. Does not bear fruit."

    def __eq__(self, other):
        if (self.name == other.name and self.scientific_name == other.scientific_name and self.get_age() == other.get_age() and self.bears_fruit == other.bears_fruit):
            return True
        return False
    
    def water(self):
        print(f"Make sure not to water your {self.name} too much!")

    def pick_fruit(self):
        if(self.bears_fruit):
            print(f"You picked a fruit off your {self.name}!")
        else:
            print(f"{self.name} doesn't have any fruit on it!")

def main():
    plant1 = Plant("tree", "genus species", 12)
    plant1.increment_age()
    print(plant1)
    plant1.water()

    plant2 = Plant("tree", "genus species", 12)
    plant2.increment_age()
    print(plant2)
    print(plant1 == plant2)

    spider1 = Spider_Plant("Young Spider Plant","Chlorophytum comosum", 1, 1)
    spider1.increment_age()
    print(spider1)
    spider1.water()

    spider2 = Spider_Plant("Old Spider Plant", "Chlorophytum comosum", 30, 12)
    spider2.increment_age()
    print(spider2)
    print(spider1 + spider2)

    succ1 = Succulent("Aloe Vera", "Aloe barbadensis Miller", 100, False)
    succ1.increment_age()
    print(succ1)
    succ1.water()
    succ1.pick_fruit()

    succ2 = Succulent("Prickly Pear Cactus", "Mill", 20, True)
    succ2.increment_age()
    print(succ2)
    succ2.water()
    succ2.pick_fruit()

    print(Plant.garden_size)
    plant1.prune_plant(5)
    print(plant1)

if __name__ == "__main__":
    main()