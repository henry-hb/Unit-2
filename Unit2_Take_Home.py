class Plant:
    garden_size = 0
    def __init__(self, name, scientific_name, age = 0):
        self.name = name
        self.scientific_name = scientific_name
        self.age = age
        garden_size += 1

class Spider_Plant(Plant):
    def __init__(self, name, scientific_name, age, num_plants):
        #num_plants is how many times the spider plant has reproduced another spider plant from one of its ends
        super().__init__(name, scientific_name, age)
        self.num_plants = num_plants

class Succulent(Plant):
    def __init__(self, name, scientific_name, age, bears_fruit):
        super().__init__(name, scientific_name, age)
        self.bears_fruit = bears_fruit

def main():
    pass

if __name__ == "__main__":
    main()