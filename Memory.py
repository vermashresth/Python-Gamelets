import simplegui
import random
nos = [0,1,2,3,4,5,0,1,2,3,4,5]
state = 0
printpos = [""]
noprint = [""]
matchlist = [""]
matchpos = [0,0]
k = 1
moves = 0
random.shuffle(nos)
def mouse_handler(pos):
    global state,printpos,nopos,noprint,matchpos,matchlist, k, moves
    nopos = pos[0]//100
    if state == 0:
        state = 1
        printpos.pop(0)
        noprint.pop(0)
        printpos.append((nopos*100)+10)
        noprint = [nos[nopos]]
        moves = moves +1
        label.set_text("moves = "+str(moves))
    elif state == 1:
        printpos.append((nopos*100)+10)
        noprint.append(nos[nopos])
        if printpos[0] != printpos[1]:
            state = 2
            moves = moves +1
            label.set_text("moves = "+str(moves))
        else:
            printpos.pop(1)
            noprint.pop(1)
    elif state == 2:
        printpos.append((nopos*100)+10)
        noprint.append(nos[nopos])
        if printpos[1] != printpos[2]:
            state = 1
            if noprint[1] == noprint[2]:
                if matchpos == [0,0]:
                    matchlist.pop(0)
                    matchpos = []
                else :
                    k = k + 1
                matchlist.append(noprint[1])
                matchpos.extend([printpos[1],printpos[2]])           
            printpos = []
            noprint = []
            printpos.append((nopos*100)+10)
            noprint.append(nos[nopos])
            moves = moves +1
            label.set_text("moves = "+str(moves))
        else:
            printpos.pop(1)
            noprint.pop(1)

def matchif():
    global matchpos, matchlist, k    
    if state == 2:
        if noprint[0] == noprint[1] :
            if matchpos == [0,0]:
                matchlist.pop(0)
                matchpos = []
            else :
                k = k + 1
            matchlist.append(noprint[0])
            matchpos.extend([printpos[0],printpos[1]])    

def draw_handler(canvas):
    global k,state,nopos,printpos, matchlist, matchpos
    abc = range(k)
    xyz = range(12)
    if state == 0:
        canvas.draw_text(str(noprint[0]), (50, 50), 12, "darkslategrey")
    elif state == 1:
        canvas.draw_text(str(noprint[0]), (printpos[0], 50), 35, "darkslategrey")
    elif state == 2:
        canvas.draw_text(str(noprint[0]), (printpos[0], 50), 35, "darkslategrey")
        canvas.draw_text(str(noprint[1]), (printpos[1], 50), 35, "darkslategrey")
    for i in range(k) :
        canvas.draw_text(str(matchlist[i]),(matchpos[i+i], 50), 35, "navy")
        canvas.draw_text(str(matchlist[i]),(matchpos[i+i+1], 50), 35, "navy")
    for c in range(12):
        canvas.draw_line((c*100,0), (c*100,100), 1, "Blue")
    matchif()
    
def reset():
    global matchpos, matchlist, printpos, printlist,state,k,moves
    state = 0
    printpos = []
    noprint = []
    matchlist = []
    matchpos = []
    printpos = [""]
    noprint = [""]
    matchlist = [""]
    matchpos = [0,0]
    k = 1
    moves = 0
    random.shuffle(nos)
      
# Create a frame and assign callbacks to event handlers
frame = simplegui.create_frame("memory", 1200, 100)
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background("MediumTurquoise ")
button1 = frame.add_button("Reset",reset)
label = frame.add_label("moves = "+str(moves))
# Start the frame animation
frame.start()
