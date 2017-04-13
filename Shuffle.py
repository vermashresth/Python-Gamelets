import simplegui
import random
image = simplegui.load_image("https://www.dropbox.com/s/7angizxm17ofeqk/marlll.png?dl=1")
width = 640
height = 480
whs=[width/3,height/3]
listr = []
listw =[]
s = 0
state = 0
listx=[]
work = 0
shuffled = False
while s<3:
    listx.append((width*s)/3+(width/6))
    s+=1
t = 0
listy=[]
while t<3:
    listy.append((height*t)/3+(height/6))
    t+=1
a,b,c,d,e,f,g,h,i=(listx[0],listy[0]),(listx[0],listy[1]),(listx[0],listy[2]),(listx[1],listy[0]),(listx[1],listy[1]),(listx[1],listy[2]),(listx[2],listy[0]),(listx[2],listy[1]),(listx[2],listy[2])

sv = [[listx[0],listy[0]],[listx[0],listy[1]],[listx[0],listy[2]],[listx[1],listy[0]],[listx[1],listy[1]],[listx[1],listy[2]],[listx[2],listy[0]],[listx[2],listy[1]],[listx[2],listy[2]]]
      
ultdict = {a:sv[0],b:sv[1],c:sv[2],d:sv[3],e:sv[4],f:sv[5],g:sv[6],h:sv[7],i:sv[8]}
def draw_handler(canvas):
    p = 0
    
    while p<9:
        canvas.draw_image(image,(ultdict.values()[p][0],ultdict.values()[p][1]),whs,(ultdict.keys()[p][0],ultdict.keys()[p][1]),whs)
        p +=1 
        
    i,j = 1,1
    while i<3:
        canvas.draw_line([0,(image.get_height())*i/3 ], [image.get_width(),(image.get_height())*i/3 ],2 , 'Black')
        i +=1
    while j<3:
        canvas.draw_line([(image.get_width())*j/3,0 ], [image.get_width()*j/3,image.get_height()],2 , 'Black')
        j +=1
def mouse_handler(pos):
    global listr,state,work,listw
    print "before",ultdict
    print "hello"
    if state>1:
        listr = []
        listw = []
        state = 0
    listr.append([((pos[0]//(width/3))*width/3)+width/6,(pos[1]//((height/3))*height/3)+height/6])
    listw.append(ultdict[tuple(listr[-1])])
    work = 0
    state+=1
    print state
    print "",listr
    
    if (state==2 and state!=0) :
        k = state-2
        work = 0
        ultdict[tuple(listr[1])]=listw[0]
        ultdict[tuple(listr[0])]=listw[1]
        print "bye"
    print "after",ultdict    
def button_handler() :
    global shuffled,sv,ultdict
    random.shuffle(sv)
    ultdict = {a:sv[0],b:sv[1],c:sv[2],d:sv[3],e:sv[4],f:sv[5],g:sv[6],h:sv[7],i:sv[8]}
    shuffled = True

frame = simplegui.create_frame('Testing', 640,480)
button = frame.add_button("Shuffle", button_handler)    
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw_handler)
frame.start()
