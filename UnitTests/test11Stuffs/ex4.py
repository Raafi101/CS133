
from tkinter import *
from random import choice
import time

def clock():
    return time.perf_counter()

# Ball and its velocity
ball, velx, vely = None, 100, 100
field = None
previousTime = 0
keyboard = {'Up': False, 'Left': False, 'Down': False, 'Right': False}

blocks = []

# NEW: checks which side of the block was hit
def hitBlock(block, x0, y0, x1, y1):
    bx0, by0, bx1, by1 = field.coords(block)
    if bx0 <= x1 <= bx1 and by0 <= y1 <= by1:
        if y0 < by0:
            return 'top'
        elif y0 > by1:
            return 'bottom'
        elif x0 < bx0:
            return 'left'
        else:
            return 'right'
    else:
        return 'no-collision'

# returns position of the *center* of the ball
def ballPosition():
    x1, y1, x2, y2 = list(field.coords(ball))
    return [(x1+x2)/2, (y1+y2)/2]

def startGame():
    global field, ball, previousTime
    root = Tk()
    field = Canvas(root, width=300, height=300, bg='light blue')
    field.pack()
    # place ball at random
    upperLeftX = choice(list(range(290)))
    upperLeftY = choice(list(range(290)))
    ball = field.create_oval(upperLeftX, upperLeftY, upperLeftX+10, upperLeftY+10, fill='blue')
  
    # NEW: add blocks
    for i in range(2):
        for j in range(3):
            w = 50
            h = 20
            block = field.create_rectangle(100 + w*i, 100 + h*j, 100 + w*(i+1), 100 + h*(j+1), fill='red')
            blocks.append(block)

    def key_press(event):
        if event.keysym == 'Up':
            keyboard['Up'] = True
        if event.keysym == 'Down':
            keyboard['Down'] = True
        if event.keysym == 'Left':
            keyboard['Left'] = True
        if event.keysym == 'Right':
            keyboard['Right'] = True
    
    def key_release(event):
        if event.keysym == 'Up':
            keyboard['Up'] = False
        if event.keysym == 'Down':
            keyboard['Down'] = False
        if event.keysym == 'Left':
            keyboard['Left'] = False
        if event.keysym == 'Right':
            keyboard['Right'] = False

    root.bind("<Key>", key_press) 
    root.bind("<KeyRelease>", key_release) 
    previousTime = clock()
    animate()

def animate():
    global velx, vely
    
    # === Measuring the elapsed time more accurately ===
    global previousTime
    time = clock()
    dt = time - previousTime # dt is the time elapsed since the previous update
    previousTime = time      # ball displacement is vel*dt

    # === Process keyboard events ===
    acceleration = 300
    if keyboard['Up']:
        vely -= acceleration*dt
    if keyboard['Down']:
        vely += acceleration*dt
    if keyboard['Left']:
        velx -= acceleration*dt
    if keyboard['Right']:
        velx += acceleration*dt

    # === Update the game state ===
    x, y = ballPosition()
    vely += 200 * dt 
    
    # collisions with walls
    if x+velx*dt>300 or x+velx*dt<0:
        velx *= -0.8 
    if y+vely*dt>300 or y+vely*dt<0:
        vely *= -0.8 
   
    # NEW: collisions with blocks
    x1 = x + velx*dt
    y1 = y + vely*dt
    for block in blocks:
        res = hitBlock(block, x, y, x1, y1)
        if res == 'left' or res == 'right':
            velx *= -0.8 # dissipating collisions
        elif res == 'top' or res == 'bottom':
            vely *= -0.8 # dissipating collisions

    field.move(ball, velx*dt, vely*dt) 
    field.after(20, animate)

startGame()
mainloop()

