#Ping game by SV
import simplegui
import random
ballpos = [500/2,500/2]
gutter_wid = 10
width = 500
height = 500
strk_h = 50
ballpos = [width/2,height/2]
strk1t = [gutter_wid/2,((height-strk_h)/2)]
strk1b = [gutter_wid/2,(height-strk_h)/2+strk_h]
strk2t = [width-gutter_wid/2,(height-strk_h)/2]
strk2b = [width-gutter_wid/2,(height-strk_h)/2+strk_h]
frame = simplegui.create_frame("game_board",width,height)
vel1 = 0
vel2 = 0
x = random.randint(-4,4)
y = random.randint(-4,4)
p1 = ""
p2 = ""
def input_handler1(text_input):
    global p1
    p1 = text_input
def input_handler2(text_input):
    global p2
    p2 = text_input
def timer_handler():
    
    velball[0] = velball[0]*1.5
    velball[1] = velball[1]*1.5
timer = simplegui.create_timer(5000, timer_handler)
def ball_init():
    global ballpos, x, y, velball
    ballpos = [width/2,height/2]
    x = random.randint(-4,4)
    y = random.randint(-4,4)
    velball = [x,y] 
    timer.stop()
    timer.start()
velball = [0,0]  

score1 = 0
score2 = 0

def counter1():
    global score1
    score1 += 1
def counter2():
    global score2
    score2 +=1

def draw_handler(canvas):
    global gutter_wid, height, vel, strk1t, strk1b, strk2t, strk2b, velball, a , b , c
    canvas.draw_polygon([(0,0), (0,height), (gutter_wid,height),(gutter_wid,0)],1, "Green","Green")
    canvas.draw_polygon([(width,0), (width-gutter_wid,0), (width-gutter_wid,height),(width,height)],1, "red","red")
    canvas.draw_line(strk1t,strk1b,gutter_wid/2+3.5,"white")
    canvas.draw_line(strk2t,strk2b,gutter_wid/2+3.5, "white")
    canvas.draw_line((width/2, 0), (width/2,height ), 6, "grey")
    strk1t[1] += vel1
    strk1b[1] += vel1
    strk2t[1] += vel2
    strk2b[1] += vel2
    ballpos[0] += velball[0]
    ballpos[1] += velball[1]
    if ballpos[0] + 10 < width - gutter_wid:
        velball[0] =velball[0]
    else:
        if ballpos[1]<strk2t[1]:
            velball = velball
            counter1()
            ball_init()
        elif ballpos[1]>strk2b[1]:
            velball = velball
            counter1()
            ball_init()
        else:
            velball[0] =-velball[0] 
    if ballpos[0] - 10 > gutter_wid:
        velball[0] =velball[0]
    else:
        if ballpos[1]<strk1t[1]:
            velball = velball
            counter2()
            ball_init()
        elif ballpos[1]>strk1b[1]:
            velball = velball
            counter2()
            ball_init()
        else:
            velball[0] =-velball[0] 
    if ballpos[1]-10 <0:
        velball[1] = -velball[1]
    else:
        if ballpos[1]+10>height:
            velball[1] = -velball[1]
        else :
            velball[1]=velball[1]
                      
            
    
    canvas.draw_circle(ballpos, 10, 1, "yellow", "yellow")
    canvas.draw_text(str(score1), (200, 80), 40, "green")
    canvas.draw_text(str(score2), (300, 80), 40, "Red")
    canvas.draw_text(p1, (150, 40), 30, "green")
    canvas.draw_text(p2, (300, 40), 30, "Red")
    
def key_handler1(key):
    ac = 5
    global vel1, vel2 
    if key == simplegui.KEY_MAP["up"]:
        vel1 -= ac
    elif key == simplegui.KEY_MAP["down"]:
        vel1 += ac
    elif key == simplegui.KEY_MAP["w"]:
        vel2 -= ac
    elif key == simplegui.KEY_MAP["s"]:
        vel2 += ac
    
def key_handler2(key):
    global vel1, vel2
    if key==simplegui.KEY_MAP["W"]:
        vel2=0
    if key==simplegui.KEY_MAP["s"]:
        vel2=0
    
    if key==simplegui.KEY_MAP["up"]:
        vel1=0
    if key==simplegui.KEY_MAP["down"]:
        vel1=0


frame.set_keyup_handler(key_handler2)        
def buttonh():
    ball_init() 
def buttons():
    ball_init() 

    
inp1 = frame.add_input("Enter player 1 name", input_handler1, 50)
inp2 = frame.add_input("Enter player 2 name", input_handler2, 50)
button = frame.add_button("Start game",buttons)
button = frame.add_button("Reset ball",buttonh)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler1)


frame.start()