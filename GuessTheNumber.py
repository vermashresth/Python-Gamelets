
import simplegui
import random
guess100 = random.randint(1,100)
guess1000 = random.randint(1,1000)
x = 7
def counter():
    global x
    x = x - 1

frame = simplegui.create_frame("Testing", 300, 300)

def inphandler(pl_guess):
    global k
    global x
    counter()
    print "Your guess was", pl_guess
    if x > 0:
        if k > int(pl_guess) :
            print "Higher!"
            print "Number of guess remaining are",x
        elif k < int(pl_guess) :
            print "Lower!"
            print "Number of guess remaining are",x
        elif k == int(pl_guess) :
            print "Correct!"
            print "Click on any button to start new game"
        else :
            print "Game over"
            print "The number was",k
            print "Better luck next time"
    print
        
a = frame.add_input("Label", inphandler, 100)
def buttonhandler1():
    print "New game. Guess a number from 1 - 100"
    global guess100
    global k
    global x
    x = 7
    print "Number of guess remaining are",x
    print
    k = guess100
def buttonhandler2():
    print "New game. Guesss a number from 1 - 1000"
    global guess1000
    global k
    global x
    x = 10
    print "Number of guess remaining are",x
    print
    k = guess1000
    
button1 = frame.add_button("range 1 - 100", buttonhandler1,200)
button2 = frame.add_button("range 1- 1000", buttonhandler2,200)
frame.start()