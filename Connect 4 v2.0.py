#connect 4
import sys
import pygame
import numpy as np

pygame.init()

#display window
dis_width=720
dis_height=620
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Connect 4') #title of window


#create matrix of board for game purposes
board_mat=np.zeros((6,7)) #board_mat[row][column]

#2 arrays to translate pygame board with matrix board [[x_axis]]
pygame_translate_x=[60,160,260,360,460,560,660]

#2 arrays to translate pygame board with matrix board [[y_axis]]
mat_translate_y=[5,4,3,2,1,0]
pygame_translate_y=[560,460,360,260,160,60]

#colours
white = (255, 255, 255) 
yellow_d = (255, 255, 0) 
yellow_l = (255, 255, 166)
black = (0, 0, 0)
red_d = (255, 0, 0) 
red_l = (255, 166, 166)
green = (0, 255, 0)
blue = (0, 0, 255) 

font_style=pygame.font.SysFont("bahnschrift",25)


def draw_board():
    dis.fill(blue)
    rad=45
    for i in range(0,7): #width
        for j in range(0,6): #height
            pygame.draw.circle(dis,white,[60+100*i,60+100*j],rad)

def hilight_piece(player,board):
    draw_board() #draw the base board again (wiping the previous highlight piece)
    
    #code to redraw the current game board
    for i in range(6): #each row
        for j in range(7): #each column
            if board[i,j]==0:
                "do nothing"
            elif board[i,j]==1:
                index=mat_translate_y.index(i)
                pygame.draw.circle(dis,red_d,[pygame_translate_x[j],pygame_translate_y[index]],45)
            else:
                index=mat_translate_y.index(i)
                pygame.draw.circle(dis,yellow_d,[pygame_translate_x[j],pygame_translate_y[index]],45)
                
    #code to draw the next piece the mouse is hovered over
    pos=pygame.mouse.get_pos()[0]-60
    rounded=round(pos/100)*100
    if pygame.mouse.get_pos()[0] >=10 and pygame.mouse.get_pos()[0] <=710:
        for matrix_y_coord in mat_translate_y:
            index_x=pygame_translate_x.index(rounded+60)
            if board[matrix_y_coord][index_x]==0:
                index_y=mat_translate_y.index(matrix_y_coord)
                if player%2 == 0:
                    pygame.draw.circle(dis,red_l,[rounded+60,pygame_translate_y[index_y]],45)
                if player%2 == 1:
                    pygame.draw.circle(dis,yellow_l,[rounded+60,pygame_translate_y[index_y]],45)
                break

def win(player):
    run=False
    GameWin=True
    return run,GameWin
    #if player%2==0:
    #    winner="Player 1"
    #elif player%2==1:
    #    winner="Player 2"

def winMessage(msg,colour):
    mesg=font_style.render(msg,True,colour)
    pygame.draw.rect(dis,black,[280,50,155,35])
    dis.blit(mesg,[280,50])

def drawMessage(msg,colour):
    mesg=font_style.render(msg,True,colour)
    pygame.draw.rect(dis,black,[330,50,60,35])
    dis.blit(mesg,[330,50])


def next_move(player,pos,GameWin): #also checks if the game is won
    rounded=round(pos/100)*100
    if pygame.mouse.get_pos()[0] >=10 and pygame.mouse.get_pos()[0] <=710:
        index_x=pygame_translate_x.index(rounded+60)
        for matrix_y_coord in mat_translate_y:
            if board_mat[matrix_y_coord][index_x]==0:
                index_y=mat_translate_y.index(matrix_y_coord)
                if player%2 == 0:
                    pygame.draw.circle(dis,red_d,[rounded+60,pygame_translate_y[index_y]],45)
                    board_mat[matrix_y_coord][index_x]=1
                if player%2 == 1:
                    pygame.draw.circle(dis,yellow_d,[rounded+60,pygame_translate_y[index_y]],45)
                    board_mat[matrix_y_coord][index_x]=2
                
                
                
                
                #check if win
                #                     ==== VERTICAL WINS ====
                if matrix_y_coord >= 3:
                    "vertical spaces too short for win so dont need to look :)"
                else:
                    if board_mat[matrix_y_coord][index_x] == board_mat[matrix_y_coord+1][index_x] == board_mat[matrix_y_coord+2][index_x] == board_mat[matrix_y_coord+3][index_x]:
                        run,GameWin=win(player)
                
                
                #                     ==== HORIZONTAL WINS ====
                for i in range(0,4):
                    if board_mat[matrix_y_coord][i] == board_mat[matrix_y_coord][i+1] == board_mat[matrix_y_coord][i+2] == board_mat[matrix_y_coord][i+3] != 0:
                        run,GameWin=win(player)
                
                
                m=np.copy(board_mat)
                #                     ==== DIAG 1 WINS ==== (top left to bottom right)
                if board_mat[0][3] == board_mat[1][4] == board_mat[2][5] == board_mat[3][6] != 0:
                    #most upper-right possible win
                    run,GameWin=win(player)
                if board_mat[2][0] == board_mat[3][1] == board_mat[4][2] == board_mat[5][3] != 0:
                    #most bottom-left possible win
                    run,GameWin=win(player)
                #all inbetween diag 1 wins!
                if (m[0,2]==m[1,3]==m[2,4]==m[3,5]!=0) or (m[1,3]==m[2,4]==m[3,5]==m[4,6]!=0):
                    run,GameWin=win(player)
                if (m[0,1]==m[1,2]==m[2,3]==m[3,4]!=0) or (m[1,2]==m[2,3]==m[3,4]==m[4,5]!=0) or (m[2,3]==m[3,4]==m[4,5]==m[5,6]!=0):
                    run,GameWin=win(player)
                if (m[0,0]==m[1,1]==m[2,2]==m[3,3]!=0) or (m[1,1]==m[2,2]==m[3,3]==m[4,4]!=0) or (m[2,2]==m[3,3]==m[4,4]==m[5,5]!=0):
                    run,GameWin=win(player)
                if (m[1,0]==m[2,1]==m[3,2]==m[4,3]!=0) or (m[2,1]==m[3,2]==m[4,3]==m[5,4]!=0):
                    run,GameWin=win(player)
                
                
                #                     ==== DIAG 2 WINS ==== (top right to bottom left)
                if board_mat[0][3] == board_mat[1][2] == board_mat[2][1] == board_mat[3][0] != 0:
                    #most upper-left possible win
                    run,GameWin=win(player)
                if board_mat[2][6] == board_mat[3][5] == board_mat[4][4] == board_mat[5][3] != 0:
                    #most bottom-right possible win
                    run,GameWin=win(player)
                #all inbetween diag 1 wins!
                if (m[0,4]==m[1,3]==m[2,2]==m[3,1]!=0) or (m[1,3]==m[2,2]==m[3,1]==m[4,0]!=0):
                    run,GameWin=win(player)
                if (m[0,5]==m[1,4]==m[2,3]==m[3,2]!=0) or (m[1,4]==m[2,3]==m[3,2]==m[4,1]!=0) or (m[2,3]==m[3,2]==m[4,1]==m[5,0]!=0):
                    run,GameWin=win(player)
                if (m[0,6]==m[1,5]==m[2,4]==m[3,3]!=0) or (m[1,5]==m[2,4]==m[3,3]==m[4,2]!=0) or (m[2,4]==m[3,3]==m[4,2]==m[5,1]!=0):
                    run,GameWin=win(player)
                if (m[1,6]==m[2,5]==m[3,4]==m[4,3]!=0) or (m[2,5]==m[3,4]==m[4,3]==m[5,2]!=0):
                    run,GameWin=win(player)
                
                #== end of win check == 
                
                if GameWin==True:
                    while True:
                        if player%2 == 0:
                            winMessage('Player 1 Wins',green)
                        elif player%2 == 1:
                            winMessage('Player 2 Wins',green)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                quits()
                    
                break
            else:
                "do nothing"
    player+=1
    return player

def quits():
    pygame.quit()
    sys.exit() #quits the program



#main gameloop
run=True
GameWin=False
player=0
draw_board()
while run==True:
    hilight_piece(player,board_mat) #update player number thingy
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()[0]-60
            player = next_move(player,pos,GameWin)
            print(board_mat,"\n") ###DELETE
    pygame.display.update()
    if (board_mat[0,0] and board_mat[0,1] and board_mat[0,2] and board_mat[0,3] and board_mat[0,4] and board_mat[0,5] and board_mat[0,6])!=0:
        while True:
            drawMessage('Draw',green)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quits()
        

quits()