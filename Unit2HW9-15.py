"""
Name: Henry Hall-Brown
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. Print a message reporting 
how many times the loop had to run to give you a winning ticket.
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
    
    def __eq__(self,other):
        if self[0] == other.lottery[0] and self[1] == other.lottery[1] and self[2] == other.lottery[2] and self[3] == other.lottery[3]:
            return True
        return False

def main():
    winner = Lottery([])
    print (winner.lottery)
    my_ticket = [1,"A",2,"B"]
    attempts = 0
    new_winner = Lottery([])
    while (my_ticket != new_winner.lottery):
        attempts += 1
        new_winner = Lottery([])
        print (new_winner.lottery)
    print (f"You had to pull {attempts} lottery tickets before you got a winner")

if __name__ == "__main__":
    main()