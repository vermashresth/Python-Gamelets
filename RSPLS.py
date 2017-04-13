import random
a = 1 or 2 or 3 or 4 or 5 
b = "rock" or "scissor" or "lizard" or "paper" or "spock"

def name2number(name):
    global a
    if name == "rock":
        a = 1
    elif name == "paper":
        a = 5
    elif name == "scissor":
        a = 4
    elif name == "lizard":
        a = 2
    elif name == "spock":
        a = 3
    return int(a)
def number2name(number):
    global b
    if number == 1:
        b = "rock"
    elif number == 5:
        b = "paper"
    elif number == 4:
        b = "scissor"
    elif number == 2:
        b = "lizard"
    elif number == 3:
        b = "spock"
    return b
def rpsls(c):
    computer_guess = random.randint(1,5)
    player_guess = c
    print "Player chooses " , player_guess 
    print "Computer chooses ", number2name(computer_guess)
    if number2name(computer_guess) == c:
        print "Player and computer tie!"
    elif computer_guess == (name2number(c) + 1)%5 or computer_guess-5 == (name2number(c) + 1)%5 or  computer_guess == (name2number(c) +3)%5 or computer_guess-5 == (name2number(c) +3)%5 :
        print "Player wins!"
    else :
        print "Computer wins!"
    print
    print

rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissor")








    




