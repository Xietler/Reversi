import sys,random,pygame,math
import rule
import numpy as np
from pygame.locals import *
from rule import *

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Reversi")
font = pygame.font.Font(None,18)

start = False
#load the pictures needed by gui
initimage = pygame.image.load("init.jpg")
initimage = pygame.transform.smoothscale(initimage,(800,600))
startbutton = pygame.image.load("startbutton.jpg")
startbutton = pygame.transform.smoothscale(startbutton,(200,100))
board = pygame.image.load("background.jpg")
board = pygame.transform.smoothscale(board,(600,600))
blackimage = pygame.image.load("black.png")
blackimage = pygame.transform.smoothscale(blackimage,(60,60))
whiteimage = pygame.image.load("white.png")
whiteimage = pygame.transform.smoothscale(whiteimage,(60,60))

laughimage = pygame.image.load("laugh.png")
laughimage = pygame.transform.smoothscale(laughimage,(60,60))
cryimage = pygame.image.load("cry.png")
cryimage = pygame.transform.smoothscale(cryimage,(60,60))

start_x = 33
start_y = 29
distance = 68

#the state matrix to store:0 is empty,1 is black and -1 is white
state = np.zeros((8,8))
state[3,3] = 1
state[3,4] = -1
state[4,3] = -1
state[4,4] = 1

#the mouse position
mouse_x = 0
mouse_y = 0

#calculate which square the mouse in,according to the mouse position
area_x = -1
area_y = -1

#record the current player turn,1 is black turn and 0 is white turn
turn = 1

#to show the player if the square your mouse at is valid in the reverse's rule.
valid_view = False

#record the score of black and white
black_count = 0
white_count = 0

#the function to calc area of mouse(convert mouse position to two-dimense position)
def mouse_area(x,y):
    global area_x,area_y
    area_y = int((x - start_x)/distance)
    area_x = int((y - start_y)/distance)
    #print(area_x)
    #print(area_y)

#the function to judge if the position is in the chess board
def gamearea(x,y):
    if x >= 0 and x <= 7 and y >=0 and y <= 7:
        return True
    else:
        return False

#the function of events when mouseleft click
def mouseleft():
    global turn
    global state
    if gamearea(area_x,area_y) and state[area_x,area_y]==0 and turn == 1:#the square is empty
        if isvalid(state,turn,area_x,area_y) == False:#the square is against the rule
            print("invalid")
            return
        screen.blit(blackimage, (start_x + area_x * distance, start_y + area_y * distance))
        state = reverse(state,turn,area_x,area_y) #reverse
        turn = -turn #change the turn
        return

#the function of events when mouseright click
def mouseright():
    global turn
    global state
    if gamearea(area_x,area_y) and state[area_x,area_y]==0 and turn == -1:
        if isvalid(state,turn,area_x,area_y) == False:
            print("invalid")
            return
        screen.blit(blackimage, (start_x + area_x * distance, start_y + area_y * distance))
        state = reverse(state,turn,area_x,area_y)
        turn = -turn
        return

#when one player cannot find a valid position,change the turn
def switch():
    global turn
    turn = -turn
    print("The turn is changed")

#the main function to redraw the board and chess
def redraw():
    global valid_view
    for i in range(8):
        for j in range(8):
            if state[i, j] == 1:
                screen.blit(blackimage,(start_x + j*distance,start_y + i*distance))
            elif state[i,j] == -1:
                screen.blit(whiteimage, (start_x + j * distance, start_y + i * distance))
    draw_valid(valid_view)#draw the notice of laugh and cry

#draw the notice of laugh and cry
def draw_valid(valid_view):
    if gamearea(area_x,area_y) and state[area_x][area_y] == 0:
        if valid_view:
            screen.blit(laughimage,(start_x + area_y * distance,start_y + area_x * distance))
        else:
            screen.blit(cryimage,(start_x + area_y * distance,start_y + area_x * distance))

#count the scores
def count():
    global black_count
    global white_count
    for i in range(8):
        for j in range(8):
            if state[i][j] == 1:
                black_count += 1
            elif state[i][j] == -1:
                white_count += 1

#end the game and judge who wins
def gameover():
    global black_count,white_count
    if black_count > white_count:
        print("Black Win!!")
    elif black_count == white_count:
        print("Draw!")
    else:
        print("White Win!!")

#the init scene(zhazhahui)
def init():
    global start
    while True:
        screen.blit(initimage, (0, 0))
        screen.blit(startbutton,(300,250))
        for event in pygame.event.get():#get mouse and key events
            if event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if pressed_array[0]:
                    pos = pygame.mouse.get_pos()
                    pos_x = pos[0]
                    pos_y = pos[1]
                    if pos_x >= 300 and pos_x <= 500 and pos_y >= 250 and pos_y <= 350:
                        start = True

        if start == True:
            break
        pygame.display.update()

def game():
    init()
    global valid_view
    while True:
        screen.blit(board,(0,0)) #draw the chess board
        redraw()
        count()
        turn1_switch = is_switch(state,turn)
        turn2_switch = is_switch(state,-turn)
        if turn1_switch and turn2_switch: #judge if player1 and player2 have place to set
            gameover()
            print("Game over")
            break
        elif turn1_switch: #else,judge if one player nowhere to set
            switch()
        if turn == 1:
            print("Black's turn")
        else:
            print("White's turn")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            #print('Pressed LEFT Button!')
                            mouseleft()
                        elif index == 2:
                            #print('Pressed RIGHT Button!')
                            mouseright()
            elif event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                mouse_area(pos_x,pos_y)
                if gamearea(area_x,area_y):
                    valid_view = isvalid(state,turn,area_x,area_y)#judge if mouse area is valid(follow the rule)
                    #print(valid_view)
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        pygame.display.update()

if __name__ == '__main__':
    game()