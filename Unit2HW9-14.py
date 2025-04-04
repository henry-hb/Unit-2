"""
Name: Henry Hall-Brown
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""
from random import randint
class Lottery:
    def __init__(self, lottery):
        self.lottery = lottery
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for i in range (4):
            if (randint (1,2) == 1):
                self.lottery.append(randint(0,9))
            else:
                self.lottery.append(letters[randint(0,25)])

def main():
    winner = Lottery([])
    print (winner.lottery)

if __name__ == "__main__":
    main()