# Simple pygame program

# Import and initialize the pygame library
import pygame
from pygame.math import Vector2
from enum import IntEnum
from copy import copy

bigX = pygame.image.load('mark-x.png')
bigO = pygame.image.load('mark-o.png')

pause = False

class TikTakLetter:
    def __init__(self ):
        #postions
        self.x = 0
        self.y = 0
        self.pos = Vector2(self.x, self.y)
        self.type = 1
        self.size = Sizes.big

    def setSize(self, size):
        self.size = size
    
    def setType(self, type):
        self.type = type

    def setPos(self, x , y):
        self.pos.x = x
        self.pos.y = y

    def draw(self):
        if self.type == 1:
            self.drawX()
        else:
            self.drawO()
    
    def drawX(self):
        if(self.size == Sizes.small):
                x_rect = pygame.Rect((cell_size*self.pos.x) +cell_size/3,(cell_size*self.pos.y) + (cell_size/3), cell_size/3,cell_size/3)
                bigX_ = pygame.transform.scale(bigX, (cell_size/3,cell_size/3))
                screen.blit(bigX_, x_rect)

                #pygame.draw.rect(screen,(100,100,100),x_rect)

        elif(self.size == Sizes.mid):
                x_rect = pygame.Rect((cell_size*self.pos.x) +cell_size/4.5,(cell_size*self.pos.y) + (cell_size/4.5),cell_size/1.5,cell_size/1.5)
                bigX_ = pygame.transform.scale(bigX, (cell_size/2,cell_size/2))
                screen.blit(bigX_, x_rect)

        elif(self.size == Sizes.big):
                x_rect = pygame.Rect((cell_size*self.pos.x) + cell_size/7 ,(cell_size*self.pos.y) + cell_size/8,cell_size,cell_size)
                screen.blit(bigX, x_rect)

    def drawO(self):
        if(self.size == Sizes.small):
                o_rect = pygame.Rect((cell_size*self.pos.x) +cell_size/3,(cell_size*self.pos.y) + (cell_size/3), cell_size/3,cell_size/3)
                bigO_ = pygame.transform.scale(bigO, (cell_size/3,cell_size/3))
                screen.blit(bigO_, o_rect)

        elif(self.size ==Sizes.mid):
                o_rect = pygame.Rect((cell_size*self.pos.x) +cell_size/4.5,(cell_size*self.pos.y) + (cell_size/4.5),cell_size/1.5,cell_size/1.5)
                bigO_ = pygame.transform.scale(bigO, (cell_size/1.5,cell_size/1.5))
                screen.blit(bigO_, o_rect)


        elif(self.size == Sizes.big):
                o_rect = pygame.Rect((cell_size*self.pos.x) + cell_size/7 ,(cell_size*self.pos.y) + cell_size/8,cell_size,cell_size)
                screen.blit(bigO, o_rect)


      
class tikLines:
    def __init__(self) -> None:
        pass

    def drawLines(self):
        pygame.draw.line(screen, (255, 255, 255), (cell_size*(cell_number-2), 30),(cell_size*(cell_number-2), (cell_size-10)*cell_number), 3)
        pygame.draw.line(screen, (255, 255, 255), (cell_size*(cell_number-1), 30),(cell_size*(cell_number-1), (cell_size-10)*cell_number), 3)
        pygame.draw.line(screen, (255, 255, 255), (30, cell_size*(cell_number-2)), ((cell_size-10)*cell_number, cell_size*(cell_number-2)), 3)
        pygame.draw.line(screen, (255, 255, 255), (30, cell_size*(cell_number-1)), ((cell_size-10)*cell_number, cell_size*(cell_number-1)), 3)

pygame.init()

# Set up the drawing window
cell_size = 220
cell_number = 3
screen = pygame.display.set_mode([cell_size*cell_number+250, cell_number*cell_size]) # 660 * 660
clock = pygame.time.Clock() # to limit fps
lines = tikLines()

#fake_surf = pygame.Surface((100,200))
#fake_rec = fake_surf.get_rect(center = (400,300))
      

def checkLoc(x,y):
    if(x>= 0 and x<= 220 and y>=0 and y <= 220):
        x, y = 0 ,0
    elif(x>= 220 and x<= 440 and y>=0 and y <= 220):
        x, y = 1 ,0
    elif(x>= 440 and x<= 660 and y>=0 and y <= 220):
        x, y = 2 ,0
    elif(x>= 0 and x<= 220 and y>=220 and y <= 440):
        x, y = 0, 1
    elif(x>= 220 and x<= 440 and y>=220 and y <= 440):
        x, y = 1 ,1
    elif(x>= 440 and x<= 660 and y>=220 and y <= 440):
        x, y = 2 ,1
    elif(x>= 0 and x<= 220 and y>=440 and y <= 660):
        x, y = 0 ,2
    elif(x>= 220 and x<= 440 and y>=440 and y <= 660):
        x, y = 1 ,2
    elif(x>= 440 and x<= 660 and y>=440 and y <= 660):
        x, y = 2 ,2
    elif(x> 660):
        return None

    return (x,y)


gameboard = [[0,0,0], [0,0,0], [0,0,0]]


def drawAll(letter: TikTakLetter):
    assert(type(letter)==TikTakLetter)

    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            if gameboard[i][j] == 1:
                letter.setPos(i,j)
                letter.setSize(Sizes.small)
                letter.drawX()
            elif gameboard[i][j] == 2:
                letter.setPos(i,j)
                letter.setSize(Sizes.mid)
                letter.drawX()
            elif gameboard[i][j] == 3:
                letter.setPos(i,j)
                letter.setSize(Sizes.big)
                letter.drawX()
            elif gameboard[i][j] == 4:
                letter.setPos(i,j)
                letter.setSize(Sizes.small)
                letter.drawO()
            elif gameboard[i][j] == 5:
                letter.setPos(i,j)
                letter.setSize(Sizes.mid)
                letter.drawO()
            elif gameboard[i][j] == 6:
                letter.setPos(i,j)
                letter.setSize(Sizes.big)
                letter.drawO()
            

class Players(IntEnum):
    X=1,
    Y=0,

class Sizes(IntEnum):
    big=0,
    mid=1,
    small=2,

def drawHud(currentPlayer:Players, currentSelection:Sizes):
    assert(type(currentPlayer)==Players)
    assert(type(currentSelection)==Sizes)
    # bigO_ = pygame.transform.scale(bigO, (cell_size/3,cell_size/3))
    # screen.blit(bigO_, o_rect)
    #Current Player
    font = pygame.font.Font('freesansbold.ttf', 18)
    partial_text = currentPlayer.name
    text = font.render('Current Player: ', True, (222,171,171))
    partial_text = font.render(partial_text, True, (252,233,137))
    textRect = text.get_rect(center = (780, 70))
    screen.blit(text, textRect)
    textRect = partial_text.get_rect(center = (860, 70))
    screen.blit(partial_text, textRect)

    # Player X
    text = font.render('Player: X', True, (222,171,171))
    textRect = text.get_rect(center = (750, 160))
    screen.blit(text, textRect)

    xImage = pygame.image.load('mark-x.png')
    rectImg = pygame.Rect(710,180,cell_size/10,cell_size/10)
    xSmall = pygame.transform.scale(xImage, (cell_size/10,cell_size/10))
    screen.blit(xSmall, rectImg)
    rectImg = pygame.Rect(710,220,cell_size/8,cell_size/8)
    xMid = pygame.transform.scale(xImage, (cell_size/8,cell_size/8))
    screen.blit(xMid, rectImg)

    rectImg = pygame.Rect(710,260,cell_size/6,cell_size/6)
    xBig = pygame.transform.scale(xImage, (cell_size/6,cell_size/6))
    screen.blit(xBig, rectImg)


    # Player O
    text = font.render('Player: O', True, (222,171,171))
    textRect = text.get_rect(center = (750, 400))
    screen.blit(text, textRect)

    yImage = pygame.image.load('mark-o.png')
    rectImg = pygame.Rect(710,420,cell_size/10,cell_size/10)
    ySmall = pygame.transform.scale(yImage, (cell_size/10,cell_size/10))
    screen.blit(ySmall, rectImg)

    rectImg = pygame.Rect(710,460,cell_size/8,cell_size/8)
    yMid = pygame.transform.scale(yImage, (cell_size/8,cell_size/8))
    screen.blit(yMid, rectImg)

    rectImg = pygame.Rect(710,500,cell_size/6,cell_size/6)
    yBig = pygame.transform.scale(yImage, (cell_size/6,cell_size/6))
    screen.blit(yBig, rectImg)


    #Selected One
    if currentPlayer.value == 0:
        if currentSelection.value == 0:
            _yImage = copy(yImage)
            colorImage = _yImage.convert_alpha()
            colorImage.fill(pygame.Color("yellow"))
            _yImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            rectImg = pygame.Rect(710,500,cell_size/6,cell_size/6)
            yBig = pygame.transform.scale(_yImage, (cell_size/6,cell_size/6))
            screen.blit(yBig, rectImg)
        elif currentSelection.value == 1:
            _yImage = copy(yImage)
            colorImage = _yImage.convert_alpha()
            colorImage.fill(pygame.Color("yellow"))
            _yImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            rectImg = pygame.Rect(710,460,cell_size/8,cell_size/8) 
            yMid = pygame.transform.scale(_yImage, (cell_size/8,cell_size/8))
            screen.blit(yMid, rectImg)
        elif currentSelection.value == 2:
            _yImage = copy(yImage)
            colorImage = _yImage.convert_alpha()
            colorImage.fill(pygame.Color("yellow"))
            _yImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            rectImg = pygame.Rect(710,420,cell_size/10,cell_size/10)
            ySmall = pygame.transform.scale(_yImage, (cell_size/10,cell_size/10))
            screen.blit(ySmall, rectImg)
    
    elif currentPlayer.value == 1:
        if currentSelection.value == 0:
            _xImage = pygame.image.load('mark-x1.png')
            colorImage = _xImage.convert_alpha()
            colorImage.fill(pygame.Color("yellow"))
            _xImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            rectImg = pygame.Rect(710,260,cell_size/6,cell_size/6)
            xBig = pygame.transform.scale(_xImage, (cell_size/6,cell_size/6))
            screen.blit(xBig, rectImg)
        elif currentSelection.value == 1:
            _xImage = pygame.image.load('mark-x1.png')
            colorImage = _xImage.convert_alpha()
            colorImage.fill(pygame.Color("yellow"))
            _xImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            rectImg = pygame.Rect(710,220,cell_size/8,cell_size/8) 
            xMid = pygame.transform.scale(_xImage, (cell_size/8,cell_size/8))
            screen.blit(xMid, rectImg)
        elif currentSelection.value == 2:
            _xImage = pygame.image.load('mark-x1.png')
            colorImage = _xImage.convert_alpha()
            colorImage.fill(pygame.Color("yellow"))
            _xImage.blit(colorImage, (0,0), special_flags = pygame.BLEND_RGBA_MULT)
            rectImg = pygame.Rect(710,180,cell_size/10,cell_size/10)
            xSmall = pygame.transform.scale(_xImage, (cell_size/10,cell_size/10))
            screen.blit(xSmall, rectImg)
   
def writeRem():
    font = pygame.font.Font('freesansbold.ttf', 18)

    #player X 
    text = font.render('Remaining: ', True, (222,171,171))
    textRect = text.get_rect(center = (810, 280))
    screen.blit(text, textRect)
    text = font.render(str(playerX[Sizes.big]), True, (222,171,171))
    textRect = text.get_rect(center = (870, 280))
    screen.blit(text, textRect)
    

    text = font.render('Remaining: ', True, (222,171,171))
    textRect = text.get_rect(center = (810, 235))
    screen.blit(text, textRect)
    text = font.render(str(playerX[Sizes.mid]), True, (222,171,171))
    textRect = text.get_rect(center = (870, 235))
    screen.blit(text, textRect)

    text = font.render('Remaining: ', True, (222,171,171))
    textRect = text.get_rect(center = (810, 190))
    screen.blit(text, textRect)
    text = font.render(str(playerX[Sizes.small]), True, (222,171,171))
    textRect = text.get_rect(center = (870, 190))
    screen.blit(text, textRect)

    #player Y 400 , 460 , 500
    text = font.render('Remaining: ', True, (222,171,171))
    textRect = text.get_rect(center = (810, 520))
    screen.blit(text, textRect)
    text = font.render(str(playerY[Sizes.big]), True, (222,171,171))
    textRect = text.get_rect(center = (870, 520))
    screen.blit(text, textRect)

    text = font.render('Remaining: ', True, (222,171,171))
    textRect = text.get_rect(center = (810, 475))
    screen.blit(text, textRect)
    text = font.render(str(playerY[Sizes.mid]), True, (222,171,171))
    textRect = text.get_rect(center = (870, 475))
    screen.blit(text, textRect)

    text = font.render('Remaining: ', True, (222,171,171))
    textRect = text.get_rect(center = (810, 435))
    screen.blit(text, textRect)
    text = font.render(str(playerY[Sizes.small]), True, (222,171,171))
    textRect = text.get_rect(center = (870, 435))
    screen.blit(text, textRect)
    
def checkWin():
    # player X won! 
    Xwon = False
    Owon = False
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            # player X won
            if(not Xwon and not Owon):
                if(j % 2 == 0 and j != 0):
                    if( gameboard[i][j] < 4 and  gameboard[i][j-1] < 4 and  gameboard[i][j-2] < 4 and  
                    gameboard[i][j] > 0 and gameboard[i][j-1] > 0  and gameboard[i][j-2] > 0):
                        Xwon = True

                if(i % 2 == 0 and i != 0):
                    if( gameboard[i][j] < 4 and  gameboard[i-1][j] < 4 and  gameboard[i-2][j] < 4 and  
                    gameboard[i][j] > 0 and gameboard[i-1][j] > 0  and gameboard[i-2][j] > 0):
                        Xwon = True
                
                #player O won
                if(j % 2 == 0 and j != 0):
                    if( gameboard[i][j] > 3 and  gameboard[i][j-1] > 3 and  gameboard[i][j-2] > 3):
                        Owon = True

                if(i % 2 == 0 and i != 0):
                    if( gameboard[i][j] > 3 and  gameboard[i-1][j] > 3 and  gameboard[i-2][j] > 3):
                        Owon = True

    # dayagonal win for X:
    if(gameboard[0][0] < 4 and gameboard[0][0] > 0 and gameboard[1][1] < 4 
    and gameboard[1][1] > 0 and gameboard[2][2] < 4 and gameboard[2][2] > 0 and not Xwon and not Owon):
        Xwon = True
    if(gameboard[0][0] > 3 and gameboard[1][1] > 3 and gameboard[2][2] > 3 and not Xwon and not Owon):
        Owon = True   

    if(gameboard[0][2] < 4 and gameboard[0][2] > 0 and gameboard[1][1] < 4 
    and gameboard[1][1] > 0 and gameboard[2][0] < 4 and gameboard[2][0] > 0 and not Xwon and not Owon):
        Xwon = True
    if(gameboard[0][2] > 3 and gameboard[1][1] > 3 and gameboard[2][0] > 3 and not Xwon and not Owon):
        Owon = True   

    if(Owon):
        font = pygame.font.Font('ComicNeue-Bold.ttf', 60)

        rect = pygame.Rect(150, 150, 400,400)
        pygame.draw.rect(screen,(0,0,0),rect)

        text = font.render('Winner!: ', True, (255,255,255))
        textRect = text.get_rect(center = (330, 350))
        screen.blit(text, textRect)
        text = font.render('O', True, (255,233,0))
        textRect = text.get_rect(center = (480, 350))
        screen.blit(text, textRect)
        pause = True

    if(Xwon):
        font = pygame.font.Font('freesansbold.ttf', 60)

        rect = pygame.Rect(150, 150, 400,400)
        pygame.draw.rect(screen,(0,0,0),rect)

        text = font.render('Winner!: ', True, (255,255,255))
        textRect = text.get_rect(center = (330, 350))
        screen.blit(text, textRect)
        text = font.render('X', True, (255,233,0))
        textRect = text.get_rect(center = (480, 350))
        screen.blit(text, textRect)
        pause = True

# Run until the user asks to quit
running = True
xLoc , yLoc = -1,-1
clickCheck = False
player = 1
letter = TikTakLetter()
pygame.display.set_caption('Tic Tac Toe')
currentSize = Sizes.big
currentPlayer = Players.X
mouseState = None
playerCheck = False

playerX = {Sizes.big : 1, Sizes.mid: 2, Sizes.small: 3} 
playerY = {Sizes.big : 1, Sizes.mid: 2, Sizes.small: 3}



while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not pause:
        if event.type == pygame.MOUSEBUTTONDOWN and clickCheck == False:
            mouseState = pygame.mouse.get_pressed()
            clickCheck = True

        if event.type == pygame.MOUSEBUTTONUP and clickCheck == True:
            state = mouseState
            mouseState = None
            if (state[2]):
                currentSize = Sizes(int((currentSize.value) +1) %3)
            if (state[0]):
                
                x, y = pygame.mouse.get_pos()
                print(f'Mouse clicked at {x}, {y}')
                location = checkLoc(x,y)
                if location:
                    currentLoc = gameboard[location[0]][location[1]]
                    letter.setSize(currentSize)
                    letter.setType(currentPlayer.value)
                    if currentPlayer.value == 1 and playerX[currentSize] > 0:
                        if currentSize.value == 0:
                            if currentLoc == 0 or currentLoc < 3 or (currentLoc > 3 and currentLoc < 6):
                                gameboard[location[0]][location[1]] = 3
                                playerCheck = True
                                playerX[currentSize] = playerX[currentSize] - 1
                        elif currentSize.value == 1:
                            if currentLoc == 0 or currentLoc < 2 or (currentLoc == 4):
                                gameboard[location[0]][location[1]] = 2
                                playerCheck = True
                                playerX[currentSize] = playerX[currentSize] - 1
                        elif currentSize.value == 2:
                            if currentLoc == 0:
                                gameboard[location[0]][location[1]] = 1
                                playerCheck = True
                                playerX[currentSize] = playerX[currentSize] - 1
                    elif currentPlayer.value == 0 and playerY[currentSize] > 0:
                        if currentSize.value == 0:
                            if currentLoc == 0 or currentLoc < 3 or (currentLoc > 3 and currentLoc < 6) :
                                gameboard[location[0]][location[1]] = 6
                                playerCheck = True
                                playerY[currentSize] = playerY[currentSize] - 1
                        elif currentSize.value == 1:
                            if currentLoc == 0 or currentLoc == 4 or currentLoc < 2 :
                                gameboard[location[0]][location[1]] = 5
                                playerCheck = True
                                playerY[currentSize] = playerY[currentSize] - 1
                        elif currentSize.value == 2:
                            if currentLoc == 0:
                                gameboard[location[0]][location[1]] = 4
                                playerCheck = True
                                playerY[currentSize] = playerY[currentSize] - 1
                    if(playerCheck):
                        currentPlayer = Players(int((currentPlayer.value) +1)%2)

            playerCheck = False       
            clickCheck = False

        # Fill the background with white
        screen.fill((20,0,25))
        lines.drawLines()

        drawHud(currentPlayer, currentSize)

        drawAll(letter)

        writeRem()

        checkWin()

        # Flip the display
        pygame.display.flip()
        clock.tick(60)

# Done! Time to quit.
pygame.quit()