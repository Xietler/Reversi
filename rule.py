import math
import numpy as np

valid = np.zeros((8,8)) #the matrix to store the 64 square's state valid or not

#state:current board state,0empty 1 black -1white,turn:the current player's turn
def valid_matrix(state,turn):
    global valid
    for i in range(8):
        for j in range(8):
            if state[i][j] == 0 and isvalid(state,turn,i,j):#the square is empty and the place is valid
                valid[i][j] = 1
            else:
                valid[i][j] = 0
    return valid

#judge if a matrix is zero matrix
def check(matrix):
    for i in range(8):
        for j in range(8):
            if matrix[i][j] != 0:
                return False
    return True

#judge if one player have nowhere to set and need to switch the turn
def is_switch(state,turn):
    valider = valid_matrix(state,turn)
    #print(valider)
    if check(valider):
        return True
    else:
        return False

#judge if one place is valid(key algorithm)
def get_judge(state,turn,x,y):
    if state[x][y] != 0:#the square is not empty
        print("Chess Exists!")
        return
    else:
        judge = np.zeros((8, 8))
        #eight circular to judge eight directions if reverse exists
        for i in range(y):
            if state[x][y - i - 1] == turn and i > 0:
                judge[0][0] = turn
                for j in range(i+1):
                    judge[0][j+1] = state[x][y - j - 1]
                break
            elif state[x][y - i - 1] == 0 or state[x][y-1] == turn:
                break
        for i in range(x):
            if state[x - i - 1][y] == turn and i > 0:
                judge[1][0] = turn
                for j in range(i+1):
                    judge[1][j+1] = state[x - j - 1][y]
                break
            elif state[x - i - 1][y] == 0 or state[x-1][y] == turn:
                break
        for i in range(7-y):
            if state[x][y + i + 1] == turn and i > 0:
                judge[2][0] = turn
                for j in range(i+1):
                    judge[2][j+1] = state[x][y + j + 1]
                break
            elif state[x][y + i + 1] == 0 or state[x][y+1] == turn:
                break
        for i in range(7-x):
            if state[x + i + 1][y] == turn and i > 0:
                judge[3][0] = turn
                for j in range(i+1):
                    judge[3][j+1] = state[x + j + 1][y]
                break
            elif state[x + i + 1][y] == 0 or state[x+1][y] == turn:
                break
        for i in range( y if y <= x else x):
            if state[x - i - 1][y - i - 1] == turn and i > 0:
                judge[4][0] = turn
                for j in range(i+1):
                    judge[4][j+1] = state[x - j - 1][y - j - 1]
                break
            elif state[x - i - 1][y - i - 1] == 0 or state[x-1][y-1] == turn:
                break
        for i in range( x if x <= 7 - y else 7 - y):
            if state[x - i - 1][y + i + 1] == turn and i > 0:
                judge[5][0] = turn
                for j in range(i+1):
                    judge[5][j+1] = state[x - j - 1][y + j + 1]
                break
            elif state[x - i - 1][y + i + 1] == 0 or state[x-1][y+1] == turn:
                break
        for i in range( 7 - x if 7 - x <= 7 - y else 7 - y):
            if state[x + i + 1][y + i + 1] == turn and i > 0:
                judge[6][0] = turn
                for j in range(i+1):
                    judge[6][j+1] = state[x + j + 1][y + j + 1]
                break
            elif state[x + i + 1][y + i + 1] == 0 or state[x+1][y+1] == turn:
                break
        for i in range( 7 - x if 7 - x <= y else y):
            if state[x + i + 1][y - i - 1] == turn and i > 0:
                judge[7][0] = turn
                for j in range(i+1):
                    judge[7][j+1] = state[x + j + 1][y - j - 1]
                break
            elif state[x + i + 1][y - i - 1] == 0 or state[x+1][y-1] == turn:
                judge[7][0] = 0
                break
        return judge

#to cope with the get_judged function to judge isvalid
def isvalid(state,turn,x,y):
    if state[x][y] != 0:
        print("Chess Exist!")
        return False
    judger = get_judge(state,turn,x,y)
    for i in range(8):
        if judger[i][0] != 0:
            return True
    return False

#the reverse function
def reverse(state,turn,x,y):
    if state[x][y] != 0:
        print("Chess Exists!")
        return state
    else:
        #search in eight directions and reverse the chesses
        state[x][y] = turn
        for i in range(y):
            if state[x][y - i - 1] == turn and i > 0:
                for j in range(i):
                    state[x][y - j - 1] = turn
                break
            elif state[x][y - i - 1] == 0 or state[x][y-1] == turn:
                break
        for i in range(x):
            if state[x - i - 1][y] == turn and i > 0:
                for j in range(i):
                    state[x - j - 1][y] = turn
                break
            elif state[x - i - 1][y] == 0 or state[x-1][y] == turn:
                break
        for i in range(7-y):
            if state[x][y + i + 1] == turn and i > 0:
                for j in range(i):
                    state[x][y + j + 1] = turn
                break
            elif state[x][y + i + 1] == 0 or state[x][y+1] == turn:
                break
        for i in range(7-x):
            if state[x + i + 1][y] == turn and i > 0:
                for j in range(i):
                    state[x + j + 1][y] = turn
                break
            elif state[x + i + 1][y] == 0 or state[x+1][y] == turn:
                break
        for i in range( y if y <= x else x):
            if state[x - i - 1][y - i - 1] == turn and i > 0:
                for j in range(i):
                    state[x - j - 1][y - j - 1] = turn
                break
            elif state[x - i - 1][y - i - 1] == 0 or state[x-1][y-1] == turn:
                break
        for i in range( x if x <= 7 - y else 7 - y):
            if state[x - i - 1][y + i + 1] == turn and i > 0:
                for j in range(i):
                    state[x - j - 1][y + j + 1] = turn
                break
            elif state[x - i - 1][y + i + 1] == 0 or state[x-1][y+1] == turn:
                break
        for i in range( 7 - x if 7 - x <= 7 - y else 7 - y):
            if state[x + i + 1][y + i + 1] == turn and i > 0:
                for j in range(i):
                    state[x + j + 1][y + j + 1] = turn
                break
            elif state[x + i + 1][y + i + 1] == 0 or state[x+1][y+1] == turn:
                break
        for i in range( 7 - x if 7 - x <= y else y):
            if state[x + i + 1][y - i - 1] == turn and i > 0:
                for j in range(i+1):
                    state[x + j + 1][y - j - 1] = turn
                break
            elif state[x + i + 1][y - i - 1] == 0 or state[x+1][y-1] == turn:
                break
        return state

def test():
    tester = np.zeros((8,8))
    tester[3][3] = 1
    tester[3][4] = -1
    tester[4][3] = -1
    tester[4][4] = 1
    tester[0][0] = -1
    tester[0][4] = -1
    tester[1][1] = 1
    tester[1][2] = -1
    tester[1][3] = 1
    tester[2][0] = 1
    tester[2][4] = 1
    tester[2][5] = -1
    tester[3][1] = 1
    tester[3][2] = 1
    tester[4][0] = -1
    tester[4][2] = 1
    tester[5][2] = 1
    tester[5][5] = -1
    tester[6][2] = -1
    #judger = get_judge(tester,-1,2,2)
    #print(tester)
    valider = isvalid(tester,1,1,6)
    print(valider)
