from tkinter import *
import random as R
matrix=[['' for i in range(3)] for j in range(3)]
root = Tk()
lbl = Label(root,text="")
lbl.grid(row=3,column = 1)
root.resizable(False,False)
end = False
def Print(m):
    for i in m:
        for j in i:
            print(j,end="\t")
        print()
class button:
    def __init__(self,i,j):
        self.turn = True
        self.i = i
        self.j = j
        self.btn = Button(root,text = "",width = 15,height = 5,bg = "white")
        self.btn.grid(row = self.i,column = self.j)
        self.btn.bind("<Button-1>".format(self.i,self.j),self.Click)
    def getText(self):
        return self.btn.cget("text")
    def Click(self,event):
        global end
        global matrix
        if end: sys.exit(0)
        if self.HuUmanStep() != "error":
            matrix = refreshMatrix(buttons)
            if not checkFull(matrix):
                lbl.configure(text="DRAW")
                end = True
                return 0
            if checkWin(matrix) != "D":
                Print(matrix)
                end = True
                lbl.configure(text="HUMAN WON")
                return 0
            bot_step = botStep(matrix)
            buttons[bot_step[1] + bot_step[0] * 3].btn.configure(text="O")
            matrix = refreshMatrix(buttons)
            if not checkFull(matrix):
                lbl.configure(text="DRAW")
                end = True
                return 0
            if checkWin(matrix) != "D":
               Print(matrix)
               end = True
               lbl.configure(text="BOT WON")
               return 0
            Print(matrix)
        else:
            print("Invalid step.")
    def HuUmanStep(self):
        if self.btn.cget("text") == '':
            self.btn.configure(text="X")
        else:
            return "error"

def getTransposed(matrix):
    res = []
    for i in range(len(matrix)):
        r = []
        for j in range(len(matrix[i])):
            r.append(matrix[j][i])
        res.append(r)
    return res

def botStep(matrix):
    # CHECK FOR HUMAN WIN (HORIZONTAL)
    for i in range(len(matrix)):
        if matrix[i].count('O') == 2 and matrix[i].count('') == 1:
            print("won horizontal.")
            return [i,matrix[i].index('')]

    for i in range(len(matrix)):
        if matrix[i].count('X') == 2 and matrix[i].count('') == 1:
            print("predicted horizontal.")
            return [i,matrix[i].index('')]
    # CHECK FOR HUMAN WIN (VERTICAL)
    matrix1 = getTransposed(matrix)
    for i in range(len(matrix1)):
        if matrix1[i].count('O') == 2 and matrix1[i].count('') == 1:
            print("won vertical.")
            return [matrix1[i].index(''),i]

    for i in range(len(matrix1)):
        if matrix1[i].count('X') == 2 and matrix1[i].count('') == 1:
            print("predicted vertical.")
            return [matrix1[i].index(''),i]
    # PREDICT DIAGONAL:
    list = []
    for i in range(len(matrix)):
        list.append(matrix[i][i])
    if list.count('O') == 2 and list.count('') == 1:
        print("won diagonal.")
        return [list.index(''),list.index('')]
    if list.count('X') == 2 and list.count('') == 1:
        print("predicted diagonal.")
        return [list.index(''),list.index('')]
    # PREDICT REVERSE-DIAGONAL:
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix) - i - 1:
                l.append(matrix[i][j])
    if l.count('O') == 2 and l.count('') == 1:
        print("won revere diagonal.")
        return [l.index(''),len(matrix) - l.index('') - 1]
    if l.count('X') == 2 and l.count('') == 1:
        print("predicted revere diagonal.")
        return [l.index(''),len(matrix) - l.index('') - 1]
    # IF HUMAN CAN`T WIN AND BOT CAN`T WIN, BOT MAKES RANDOM MOVE:
    s = 3
    while(s != ''):
        s = [R.randint(0,2),R.randint(0,2)]
        if matrix[s[0]][s[1]] == '':
            return s

def checkFull(matrix):
    result = False
    for i in matrix:
        for j in i:
            if j == '': result = True
    return result

def checkWin(matrix):
    # HORIZONTAL:
    for i in range(len(matrix)):
        if matrix[i].count('X') == 3: return 'X'
        if matrix[i].count('O') == 3: return 'O'
    #VERTICAL:
    matrix1 = getTransposed(matrix)
    for i in range(len(matrix1)):
        if matrix1[i].count('X') == 3: return 'X'
        if matrix1[i].count('O') == 3: return 'O'
    # DIAGONAL
    l = []
    for i in range(len(matrix)):
        l.append(matrix[i][i])
    if l.count('X') == 3: return 'X'
    if l.count('O') == 3: return 'O'
    # REVERSE DIAGONAL
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix) - i - 1:
                l.append(matrix[i][j])
    if l.count('X') == 3: return 'X'
    if l.count('O') == 3: return 'O'
    return 'D'

def refreshMatrix(buttons):
    matrix = []
    for i in range(3):
        m = []
        for j in range(3):
            m.append(buttons[j + i*3].getText())
        matrix.append(m)
    return matrix

buttons = []
for i in range(3):
    for j in range(3):
        buttons.append(button(i,j))
root.mainloop()