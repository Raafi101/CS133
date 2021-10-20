
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
    
    # === NEW: Measuring the elapsed time more accurately ===
    global previousTime
    time = clock()
    dt = time - previousTime # dt is the time elapsed since the previous update
    previousTime = time      # ball displacement is vel*dt

    # === NEW: Process keyboard events ===
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
    vely += 200 * dt # NEW: Add gravitational acceleration
    if x+velx*dt>300 or x+velx*dt<0:
        velx *= -0.8 # NEW: collisions dissipate ball's momentum
    if y+vely*dt>300 or y+vely*dt<0:
        vely *= -0.8 # NEW: collisions dissipate ball's momentum
    
    field.move(ball, velx*dt, vely*dt) # NEW: displacement is vel*dt
    field.after(20, animate)

startGame()
mainloop()

