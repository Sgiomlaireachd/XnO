from tkinter import *
from time import *
import random
number = 0
def Three(event):
    global number
    number = 3
    Table(3)
def Four(event):
    global number
    number = 4
    Table(4)
def Five(event):
    global number
    number = 5
    Table(5)
def Six(event):
    global number
    number = 6
    Table(6)
def Seven(event):
    global number
    number = 7
    Table(7)
def Eight(event):
    global number
    number = 8
    Table(8)

buttons = []
current = 0
goal = 1
table = 0
start = 0
def Click(event):
    global start
    global table
    global goal
    global current
    global number
    global mode
    gameMode = mode.get()
    if gameMode == 'Letter':
        title = chr(current+97) + " -> " + chr(goal+97)
    else:
        title = str(current+1) + " -> " + str(goal+1)
    btn = event.widget
    if gameMode == 'Letter':
        current = ord(btn.cget("text")) - 96
    else:
        current = btn.cget("text")
    if current == goal:
        goal += 1
        table.title(title)
        if goal - 1 == number ** 2:
            end = time()
            txt = "RESULT : " + str(round((end-start),2))
            table.title(txt)
def Table(number):
    global start
    start = time()
    global buttons
    global table
    global current
    global goal
    current = 0
    goal = 1
    table = Tk()
    table.title("0 -> 1")
    buttons = []
    texts = [i for i in range(1,number ** 2 +1)]
    global mode
    gameMode = mode.get()
    print('Gamemode:',gameMode)
    if gameMode == 'Letter':
        texts = [chr(i + 96) for i in texts]
    random.shuffle(texts)
    for i in range(number**2):
        buttons.append(Button(table,text=texts[i],width=10,height=5,font='Helvetica 18 bold'))
    # table.mainloop()
    for i in range(number):
        for j in range(number):
            buttons[i*number+j].grid(row =i, column =j)
    for button in buttons:
        button.bind("<Button-1>",Click)

root = Tk()
root.title('Shoolte tables')
btn3 = Button(root,text="3",width=10,height=5)
btn3.grid(row=1,column=1)
btn4 = Button(root,text="4",width=10,height=5)
btn4.grid(row=1,column=2)
btn5 = Button(root,text="5",width=10,height=5)
btn5.grid(row=1,column=3)
btn6 = Button(root,text="6",width=10,height=5)
btn6.grid(row=2,column=1)
btn7 = Button(root,text="7",width=10,height=5)
btn7.grid(row=2,column=2)
btn8 = Button(root,text="8",width=10,height=5)
btn8.grid(row=2,column=3)
btn3.bind("<Button-1>",Three)
btn4.bind("<Button-1>",Four)
btn5.bind("<Button-1>",Five)
btn6.bind("<Button-1>",Six)
btn7.bind("<Button-1>",Seven)
btn8.bind("<Button-1>",Eight)
mode = StringVar()
mode.set('Number')
Radiobutton(root, text="Numbers", variable=mode, value='Number').grid(row=3,column = 1)
Radiobutton(root, text="Letters", variable=mode, value='Letter').grid(row=3,column = 3)
root.mainloop()
