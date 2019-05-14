import random

class Dice:
    
    def roll(self):
        return random.randint(1,6)
    
die1 = Dice()
die2 = Dice()
while(True):
    value1 = die1.roll()
    value2 = die2.roll()
    print("半か長か入力してください(半：１、長：０)")
    evenodd = int(input())
    if (evenodd == 1  or evenodd == 0):
        if((value1 + value2)%2 == evenodd):
            print(value1,"と",value2,"でした")
            print("You Win!!")
            break
        else:
            print(value1,"と",value2,"でした")
            print("You Lose!! なんで負けたか明日までに考えてきてください")
    else:
        print("invalid number!!")
