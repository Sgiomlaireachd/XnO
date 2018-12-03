import random as R
def checkHUmanStep(matrix,step):
        if step[0] >=0 and step[0] < 3 and step[1] >= 0 and step[1] < 3:
            if matrix[step[0]][step[1]] == '.':
                return True
        return False
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
        if matrix[i].count('O') == 2 and matrix[i].count('.') == 1:
            print("won horizontal.")
            return [i,matrix[i].index('.')]

    for i in range(len(matrix)):
        if matrix[i].count('X') == 2 and matrix[i].count('.') == 1:
            print("predicted horizontal.")
            return [i,matrix[i].index('.')]
    # CHECK FOR HUMAN WIN (VERTICAL)
    matrix1 = getTransposed(matrix)
    for i in range(len(matrix1)):
        if matrix1[i].count('O') == 2 and matrix1[i].count('.') == 1:
            print("won vertical.")
            return [matrix1[i].index('.'),i]

    for i in range(len(matrix1)):
        if matrix1[i].count('X') == 2 and matrix1[i].count('.') == 1:
            print("predicted vertical.")
            return [matrix1[i].index('.'),i]
    # PREDICT DIAGONAL:
    list = []
    for i in range(len(matrix)):
        list.append(matrix[i][i])
    if list.count('O') == 2 and list.count('.') == 1:
        print("won diagonal.")
        return [list.index('.'),list.index('.')]
    if list.count('X') == 2 and list.count('.') == 1:
        print("predicted diagonal.")
        return [list.index('.'),list.index('.')]
    # PREDICT REVERSE-DIAGONAL:
    l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix) - i - 1:
                l.append(matrix[i][j])
    if l.count('O') == 2 and l.count('.') == 1:
        print("won revere diagonal.")
        return [l.index('.'),len(matrix) - l.index('.') - 1]
    if l.count('X') == 2 and l.count('.') == 1:
        print("predicted revere diagonal.")
        return [l.index('.'),len(matrix) - l.index('.') - 1]
    # IF HUMAN CAN`T WIN AND BOT CAN`T WIN, BOT MAKES RANDOM MOVE:
    s = 3
    while(s != ''):
        s = [R.randint(0,2),R.randint(0,2)]
        if matrix[s[0]][s[1]] == '.':
            return s
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
def checkFull(matrix):
    result = False
    for i in matrix:
        for j in i:
            if j == '.': result = True
    return result

def Print(m):
    for i in m:
        for j in i:
            print(j,end="\t")
        print()
def main():
    matrix=[['.' for i in range(3)] for j in range(3)]
    step = 0
    while(checkWin(matrix) == 'D'):
        Print(matrix)
        step = [-1,-1]
        while(not checkHUmanStep(matrix,step)):
            step = [int(input("Input step i:")),int(input("Input step j:"))]
            if(not checkHUmanStep(matrix,step)): print("Invalid step.")
        matrix[step[0]][step[1]] = 'X'
        if not checkFull(matrix) :
            Print(matrix)
            break
        botstep = botStep(matrix)
        matrix[botstep[0]][botstep[1]] = 'O'
    print("Result:", checkWin(matrix))
if __name__ == "__main__": main()
