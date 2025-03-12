"""
Name: Henry Hall-Brown
Date: 3/12/2025 
Description: TV class project
"""


class TV:
    """Represents a TV with a brand, size, and is either a smart TV or not."""

    def __init__(self, brand: str, size: int, is_smart_TV: bool):
        """
        creates new TV.
        
        Args:
            brand (str): brand of TV 
            size (int): diagonal length of TV
            is_smart_TV (bool): true or false depending on if it's a smart TV or not
            current_channel (int): current channel that TV is set to
            current_volume (int): current volume setting of TV
        """
        self.brand = brand
        self.size = size
        self.is_smart_TV = is_smart_TV
        self.current_channel = 0
        self.current_volume = 0

    def increase_volume(self) -> None:
        """
        increases current_volume by 1
        :return: None
        """
        self.current_volume += 1

    def set_channel(self, channel: int) -> None:
        """
        sets current_channel the the inputted channel.
        :return: None
        """
        self.current_channel = channel
        print(f"Channel is now set to {self.current_channel}. ")

    def check_in(self) -> None:
        """
        Prints a message making sure someone is still watching the TV. Only exits the while loop if the user decides to stop watching TV
        :return: None
        """
        still_watching = "yes"
        while(still_watching.upper() == "YES"):
            print(f"You've been watching TV on your {self.brand} for a while. Maybe you should consider taking a break. ")
            still_watching = str(input("Are you still watching? "))
            if(still_watching.upper() == "YES"):
                print("yikes...")
                print("")
        print("Yeah that's probably for the best. ") #guilt trip method >:)
        print("")

    def print_info(self) -> None:
        """
        Prints all instance variables of the TV.
        
        :return: None
        """
        if self.is_smart_TV:
            print(f"TV Specs: - Brand: {self.brand}, Size: {self.size} inches, and it is a smart TV. The current channel is {self.current_channel} and the current volume is {self.current_volume}. ")
        else:
            print(f"TV Specs: - Brand: {self.brand}, Size: {self.size} inches, and it is not a smart TV. The current channel is {self.current_channel} and the current volume is {self.current_volume}. ")


def main() -> None:
    """
    Creates instances of the TV class and calls each of its methods.
    
    :return: None
    """
    TV1 = TV("Samsung", "72", True)
    TV2 = TV("Zenith", "24", False)
    TV1.print_info()
    TV2.print_info()

    for i in range(20): #increases volumes of both TVs by 20
        TV1.increase_volume()
        TV2.increase_volume()
    print(f"Volume is now {TV1.current_volume}. ")
    print(f"Volume is now {TV2.current_volume}. ")

    TV1.set_channel(55)
    TV2.set_channel(32)
    
    print("")
    TV1.check_in()
    TV2.check_in()

    # Print information about each pet
    TV1.print_info()
    TV2.print_info()

if __name__ == "__main__":
    main()
