"""
Name: Henry Hall-Brown
Date: 3/10/2025 
Description: Self Serve Kiosk class assignment
"""


class Kiosk:
    def __init__(self):
        """
        creates new kiosk object

        Args:
            transaction_total (int): total cost of purchase
            total_items (int): total amount of items purchased
            item_list (dictionary): dictionary of item names and cost of each item
        """
        self.transaction_total = 0
        self.total_items = 0 
        self.item_list = {"Item": "Price"}
        print("Hi welcome to the self-serve kiosk!")

    def get_total(self) -> int:
        """
        returns total price of order
        :return: transaction_total (int)
        """
        return self.transaction_total
    
    def add_item(self) -> none:
        """
        adds new item to item_list and increments total_items by 1 and adds item price to transaction_total
        :return: None
        """
        adding_items = (input("Would you like to add an item? "))
        while(adding_items.upper() == "YES"):
            name = input("What is the name of your item? ")
            price = int(input("What is the price of your " + name + "? "))
            self.transaction_total += price
            self.total_items += 1
            self.item_list[name] = price
            adding_items = input("Would you like to add another item? ")

    def take_payment(self) -> none:
        """
        asks if user is using cash and calls give_change() if they use extra money than needed
        :return: None
        """
        cash = int(input("How much money are you using today? "))
        if (cash > self.transaction_total):
            self.give_change(cash)
        elif (cash == self.transaction_total):
            print("Thank you! Have a nice day!")
        else:
            print("That is not enough money! Try again with more money ")
            self.finalize_purchase()

    def give_change(self, money_provided):
        """
        gives back change relating to how much extra cash they gave compared to the final price
        :return: None
        """
        change = money_provided - self.transaction_total
        print(f"Your change is {change} dollars. Have a nice day!")

    def finalize_purchase(self):
        """
        prints total cost and total items and calls take_payment() to coordinate the payment
        :return: None
        """
        print(f"Your total amount is {self.total_items} items and {self.transaction_total} dollars.")
        self.take_payment()

    def print_receipt(self):
        """
        prints item_list to print all item names and item prices in the dictionary
        :return: None
        """
        for i in self.item_list:
            print(i.title(),end="")
            for j in range(30):
                if j > len(i):
                    print(" ",end="")
            print(self.item_list[i],end="")
            print(" dollars")

def main():
    """
    makes instance of kiosk class and tests all instance methods in the kiosk class
    :return: None
    """
    kiosk_one = Kiosk()
    kiosk_one.add_item()
    ready = input("Are you ready to check out? ")
    while(ready.upper() != "YES"):
        kiosk_one.add_item()
        ready = input("Are you ready to check out? ")
    kiosk_one.finalize_purchase()
    kiosk_one.print_receipt()

if __name__ == "__main__":
    main()
