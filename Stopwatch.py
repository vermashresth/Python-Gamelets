# template for "Stopwatch: The Game"
import simplegui
import random
# define global variables
t,minutes,bc,tries,milli,minutes,seconds,successcount = 0,0,0,0,0,0,0,0
run = False
watchtext = ""
X = 200 
Y = 250
# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
def format(t):
    global X,Y,milli,watchtext,minutes,seconds
    bc = int(t / 10)
    if run:
        global seconds
        if bc < 60:
            minutes = 0
            seconds = add0sec(bc)
        else :
            minutes = int(bc / 60)
            seconds = add0sec(bc % 60) 
        milli = t % 10
    watchtext = str(minutes)+":"+str(add0sec(seconds))+"."+str(milli)
    return watchtext
    

def add0sec(k): 
    if k < 10:
        sec = "0"+str(k)
    else:
        sec = str(k)
    return sec
 
scorelab = "Points"+"/"+"Tries "

# define event handlers for buttons; "Start", "Stop", "Reset"
def stop_handler():
    global milli,tries,successcount,run,t
    timer1.stop()
    if run:
        if t % 10 == 0:
            successcount += 1
            tries +=1
        else :
            tries += 1
    run = False 

def draw_handler(canvas):
    canvas.draw_text(format(t), (X, Y), 45,"orange")
    canvas.draw_text(score(successcount,tries), (10, 100), 35,"orange")
    canvas.draw_text(scorelab, (10, 50), 25,"orange")       

def score(successcount,tries):
    k = str(successcount)+"/"+str(tries)
    return k

def start_handler():
    global run
    timer1.start()
    run = True

def reset_handler():
    global t,tries,successcount
    t = 0
    tries = 0
    successcount = 0

# define event handler for timer with 0.1 sec interval
def watchhandler():
    global t
    t = t + 1
    format(t)
  
# create frame
frame = simplegui.create_frame("stopwatch", 500, 500)

# register event handlers
timer1 = simplegui.create_timer(100, watchhandler)
frame.set_draw_handler(draw_handler)
start = frame.add_button("Start", start_handler,100)
stop= frame.add_button("Stop", stop_handler,100)
reset= frame.add_button("Reset", reset_handler,100)
label8 = frame.add_label("Click reset to restart the game")

# start timer and frame
frame.start()
timer1.start()