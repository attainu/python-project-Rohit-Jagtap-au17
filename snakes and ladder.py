import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((620,500))
pygame.display.set_caption("Snakes And Ladders")
# background
backimage=pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/final.jpg")
stg = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/starts.jpg")
arrow = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/red1.png")
# players
red = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/redtoken.png")
blue = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/bluetoken.png")
green = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/greentoken.png")
yellow = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/yellowtoken.png")

# xy coedinates fo red pawn
rx = 80
ry = 270
# xy coedinates fo blue pawn
bx = 80
by = 330
# xy coedinates fo yellow pawn
yx = 80
yy = 380
# for dice roll
button = pygame.Rect(40,430,50,50)
# for game fonts
font1 = pygame.font.SysFont("comicsansms",30) # for player
font2 = pygame.font.SysFont("comicsansms",20) # for turn
score_font = pygame.font.SysFont("comicsansms",35) # for win

def back():
    screen.blit(stg,(0,0))
    screen.blit(backimage,(120,0))
    screen.blit(arrow,(40,440))

def redpawn(x,y):
    screen.blit(red,(x,y))
def bluepawn(x,y):
    screen.blit(blue,(x,y))
def yellowpawn(x,y):
    screen.blit(yellow,(x,y))
def Roll():
    diceroll = random.randint(1,6)
    if diceroll == 1:
        dice = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/dice1.png")
    elif diceroll == 2:
        dice = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/dice2.png")
    elif diceroll == 3:
        dice = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/dice3.png")
    elif diceroll == 4:
        dice = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/dice4.png")
    elif diceroll == 5:
        dice = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/dice5.png")
    elif diceroll == 6:
        dice = pygame.image.load("/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/dice6.png")
    return (dice,diceroll)

def players():
    massage = font1.render("Player 1", True, (255, 0, 0))
    screen.blit(massage,[0,290])
    massage1 = font1.render("Player 2", True, (0, 0, 255))
    screen.blit(massage1, [0, 350])
    massage2 = font1.render("Player 3", True, (255, 255, 0))
    screen.blit(massage2, [0, 400])
def redturn():
    msg = font2.render("YOUR TURN", True, (255,255,255))
    screen.blit(msg,[0,310])
def blueturn():
    msg1 = font2.render("YOUR TURN", True, (255, 255, 255))
    screen.blit(msg1, [0, 370])
def yellowturn():
    msg1 = font2.render("YOUR TURN", True, (255, 255, 255))
    screen.blit(msg1, [0, 420])
#Game Loop
running = True
turn = 'Player 1 (RED)'
while running:
    screen.fill((0,255,195))
    back()
    players()
    if turn == 'Player 1 (RED)':
        redturn()
    elif turn == 'Player 2 (BLUE)':
        blueturn()
    else:
        yellowturn()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                Roll()
                dice,diceroll = Roll()
                screen.blit(dice,(5,100))
                print(turn,diceroll)

            # for player one
            if Roll() and turn == 'Player 1 (RED)':
                turn = 'Player 2 (BLUE)'
                if diceroll == 6 and rx == 80 and ry == 270:
                    rx = 125
                    ry = 430
                    turn = 'Player 1 (RED)'
                    # for row one
                elif rx in range(125, 325) and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * diceroll)
                    if rx == 275 and ry == 430: #ladder at no 4
                        rx = 325
                        ry = 180
                    if rx == 275 and ry == 280:# snake at 37
                        rx = 225
                        ry = 430
                elif rx in range(125, 325) and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * diceroll)
                    if rx == 275 and ry == 280:# snake at 37
                        rx = 225
                        ry = 430
                    turn = 'Player 1 (RED)'
                elif rx == 325 and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * diceroll)
                    if rx == 275 and ry == 430: #ladder at no 4
                        rx = 325
                        ry = 180
                elif rx == 325 and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 5)
                    ry = ry - 50
                    turn = 'Player 1 (RED)'
                elif rx == 375 and diceroll <= 4 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30): # 7
                    rx = rx + (50 * diceroll)
                elif rx == 375 and diceroll > 4 and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 4)
                    ry = ry - 50
                elif rx == 375 and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 4) - (50 * (diceroll - 5))
                    ry = ry - 50
                    turn = 'Player 1 (RED)'
                elif rx == 425 and diceroll <= 3 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):  # 8
                    rx = rx + (50 * diceroll)
                    if rx == 425 and ry == 230:# snake at 47
                        rx = 325
                        ry = 380
                elif rx == 425 and diceroll > 3 and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 3) - (50 * (diceroll - 4))
                    ry = ry - 50
                    if rx == 425 and ry == 230:# snake at 47
                        rx = 325
                        ry = 380
                elif rx == 425 and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 3) - (50 * (diceroll - 4))
                    ry = ry - 50
                    if rx == 425 and ry == 230:# snake at 47
                        rx = 325
                        ry = 380
                    turn = 'Player 1 (RED)'
                elif rx == 475 and diceroll <= 2 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):  # 9
                    rx = rx + (50 * diceroll)
                elif rx == 475 and diceroll > 2 and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 2) - (50 * (diceroll - 3))
                    ry = ry - 50
                elif rx == 475 and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 2) - (50 * (diceroll - 3))
                    ry = ry - 50
                    turn = 'Player 1 (RED)'
                elif rx == 525 and diceroll <= 1 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):  # 10
                    rx = rx + (50 * diceroll)
                    # ladder at number 12
                    if rx == 525 and ry == 380: #ladder at 12
                        rx = 575
                        ry = 230
                elif rx == 525 and diceroll > 1 and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 1) - (50 * (diceroll - 2))
                    ry = ry - 50
                    if rx == 525 and ry == 380: #ladder at 12
                        rx = 575
                        ry = 230
                elif rx == 525 and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx + (50 * 1) - (50 * (diceroll - 2))
                    ry = ry - 50
                    if rx == 525 and ry == 380: #ladder at 12
                        rx = 575
                        ry = 230
                    turn = 'Player 1 (RED)'
                elif rx >= 575 and diceroll != 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx - (50 * (diceroll - 1))
                    ry = ry - 50
                elif rx == 575 and diceroll == 6 and (ry == 430 or ry == 330 or ry == 230 or ry == 130 or ry == 30):
                    rx = rx - (50 * (diceroll - 1))
                    ry = ry - 50
                    turn = 'Player 1 (RED)'
                # row two
                elif rx > 325 and rx <= 575 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll !=6:
                    rx = rx-(50*diceroll)
                    if rx == 525 and ry == 380: #ladder at 12
                        rx = 575
                        ry = 230
                    elif rx == 425 and ry == 380: # ladder at 14
                        rx = 375
                        ry = 180
                    elif rx == 475 and ry ==330:# snake at 28
                        rx = 575
                        ry = 430
                    elif rx == 425 and ry == 230:# snake at 47
                        rx = 325
                        ry = 380
                    elif rx == 425 and ry == 180:#ladder at 54
                        rx = 475
                        ry = 30
                    elif rx == 375 and ry == 80:# snake at 75
                        rx = 525
                        ry = 280
                    elif rx == 425 and ry == -20:# snake 94
                        rx = 575
                        ry = 80
                    elif rx == 325 and ry == -20:# snake at 96
                        rx = 175
                        ry = 230
                elif rx > 375 and rx <= 575 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll !=6:
                    rx = rx-(50* 5)
                    ry = ry - 50
                    if rx == 525 and ry == 380:# ladder at 12
                        rx = 575
                        ry = 230
                    elif rx == 425 and ry == 380: # ladder at 14
                        rx = 375
                        ry = 180
                    elif rx == 475 and ry ==330:# snake at 28
                        rx = 575
                        ry = 430
                    elif rx == 425 and ry == 230:# snake at 47
                        rx = 325
                        ry = 380
                    elif rx == 425 and ry == 180:#ladder at 54
                        rx = 475
                        ry = 30
                    elif rx == 375 and ry == 80:# snake at 75
                        rx = 525
                        ry = 280
                    elif rx == 425 and ry == -20:# snake 94
                        rx = 575
                        ry = 80
                    elif rx == 325 and ry == -20:# snake at 96
                        rx = 175
                        ry = 230
                elif rx > 375 and rx <= 575 and diceroll == 6 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20):
                    rx = rx-(50*diceroll)
                    if rx == 525 and ry == 380:# ladder at 12
                        rx = 575
                        ry = 230
                    elif rx == 425 and ry == 380: # ladder at 14
                        rx = 375
                        ry = 180
                    elif rx == 475 and ry ==330:# snake at 28
                        rx = 575
                        ry = 430
                    elif rx == 425 and ry == 230:# snake at 47
                        rx = 325
                        ry = 380
                        turn = "Player 1 (RED)"
                    elif rx == 425 and ry == 180:#ladder at 54
                        rx = 475
                        ry = 30
                    elif rx == 375 and ry == 80:# snake at 75
                        rx = 525
                        ry = 280
                    elif rx == 425 and ry == -20:# snake 94
                        rx = 575
                        ry = 80
                    elif rx == 325 and ry == -20:# snake at 96
                        rx = 175
                        ry = 230
                elif rx == 375 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll !=6:
                    rx = rx-(50*diceroll)
                elif rx == 375 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll ==6:
                    rx = rx-(50*5)
                    ry = ry - 50
                    turn = "Player 1 (RED)"
                elif rx == 325 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll < 5:
                    rx = rx-(50*diceroll)
                elif rx == 325 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll == 5:
                    rx = rx-(50*4) + (50 *(diceroll - 5))
                    ry = ry-50
                elif rx == 325 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll == 6:
                    rx = rx-(50*4) + (50 *(diceroll - 5))
                    ry = ry-50
                    turn = "Player 1 (RED)"
                elif rx == 275 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll < 4:
                    rx = rx-(50*diceroll)
                    if rx == 275 and ry == 280:# snake at 37
                        rx = 225
                        ry = 430
                    elif rx == 325 and ry == -20:# snake at 96
                        rx = 175
                        ry = 230
                elif rx == 275 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll >= 4 and diceroll != 6:
                    rx = rx - (50*3) + (50 *(diceroll - 4))
                    ry = ry-50
                    if rx == 275 and ry == 280:# snake at 37
                        rx = 225
                        ry = 430
                    elif rx == 325 and ry == -20:# snake at 96
                        rx = 175
                        ry = 230
                elif rx == 275 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll == 6:
                    rx = rx-(50*3) + (50 *(diceroll - 4))
                    ry = ry-50
                    if rx == 275 and ry == 280:# snake at 37
                        rx = 225
                        ry = 430
                    elif rx == 325 and ry == -20:# snake at 96
                        rx = 175
                        ry = 230
                    turn = "Player 1 (RED)"
                elif rx == 225 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll < 3:
                    rx = rx - (50 * diceroll)
                elif rx == 225 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll >= 3 and diceroll != 6:
                    rx = rx - (50 * 2) + (50 * (diceroll - 3))
                    ry = ry-50
                elif rx == 225 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll == 6:
                    rx = rx-(50 * 2) + (50 * (diceroll - 3))
                    ry = ry - 50
                    turn = "Player 1 (RED)"
                elif rx == 175 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll < 2:
                    rx = rx - (50 * diceroll)
                    if rx == 175 and ry == 330:# ladder at 22
                        rx = 225
                        ry = 180
                elif rx == 175 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll >= 2 and diceroll != 6:
                    rx = rx - 50 + (50 * (diceroll - 2))
                    ry = ry-50
                    if rx == 175 and ry == 330:# ladder at 22
                        rx = 225
                        ry = 180
                elif rx == 175 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll == 6:
                    rx = rx - 50 + (50 * (diceroll - 2))
                    ry = ry - 50
                    if rx == 175 and ry == 330:# ladder at 22
                        rx = 225
                        ry = 180
                    turn = "Player 1 (RED)"
                elif rx == 125 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll != 6:
                    rx = rx + (50*(diceroll-1))
                    ry = ry-50
                    if rx == 125 and ry == 230: #ladder at 41
                        rx = 175
                        ry = 80
                elif rx == 125 and (ry == 380 or ry == 280 or ry == 180 or ry == 80 or ry == -20) and diceroll == 6:
                    rx = rx + (50*(diceroll-1))
                    ry = ry - 50
                    if rx == 125 and ry == 230: #ladder at 41
                        rx = 175
                        ry = 80
                    turn = "Player 1 (RED)"
                # final row
                elif ry == -20 and (rx == 525 or rx == 575) and diceroll != 6:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and (rx == 525 or rx == 575) and diceroll == 6:
                    rx = rx - (50 * diceroll)
                    turn = 'red'
                elif ry == -20 and rx == 475 and diceroll < 5:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 475 and diceroll == 5:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 475 and diceroll == 6:
                    rx = rx
                elif ry == -20 and rx == 425 and diceroll != 6:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 425 and diceroll == 6:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 375 and diceroll < 6:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 375 and rx >= 125 and diceroll == 6:
                    rx = rx
                elif ry == -20 and rx == 325 and rx >= 125 and diceroll >= 5:
                    rx = rx
                elif ry == -20 and rx == 325 and rx >= 125 and diceroll < 5:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 275 and rx >= 125 and diceroll >= 4:
                    rx = rx
                elif ry == -20 and rx == 275 and rx >= 125 and diceroll < 4:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 225 and rx >= 125 and diceroll >= 3:
                    rx = rx
                elif ry == -20 and rx == 225 and rx >= 125 and diceroll < 3:
                    rx = rx - (50 * diceroll)
                elif ry == -20 and rx == 175 and rx > 125 and diceroll >= 2:
                    rx = rx
                # for player two
            elif Roll() and turn == 'Player 2 (BLUE)':
                turn = 'Player 3 (YELLOW)'
                if diceroll == 6 and bx == 80 and by == 330:
                    bx = 125
                    by = 430
                    turn = 'Player 2 (BLUE)'
                # for row one
                elif bx in range(125, 325) and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                    bx = bx + (50 * diceroll)
                if bx == 275 and by == 430:  # ladder at no 4
                    bx = 325
                    by = 180
                if bx == 275 and by == 280:  # snake at 37
                    bx = 225
                    by = 430
            elif bx in range(125, 325) and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * diceroll)
            if bx == 275 and by == 280:  # snake at 37
                bx = 225
                by = 430
                turn = 'Player 2 (BLUE)'
            elif bx == 325 and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * diceroll)
            if bx == 275 and by == 430:  # ladder at no 4
                bx = 325
                by = 180
            elif bx == 325 and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 5)
                by = by - 50
                turn = 'Player 2 (BLUE)'
            elif bx == 375 and diceroll <= 4 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):  # 7
                bx = bx + (50 * diceroll)
            elif bx == 375 and diceroll > 4 and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 4)
                by = by - 50
            elif bx == 375 and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 4) - (50 * (diceroll - 5))
                by = by - 50
                turn = 'Player 2 (BLUE)'
            elif bx == 425 and diceroll <= 3 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):  # 8
                bx = bx + (50 * diceroll)
            if bx == 425 and by == 230:  # snake at 47
                bx = 325
                by = 380
            elif bx == 425 and diceroll > 3 and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 3) - (50 * (diceroll - 4))
                by = by - 50
            if bx == 425 and by == 230:  # snake at 47
                bx = 325
                by = 380
            elif bx == 425 and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 3) - (50 * (diceroll - 4))
                by = by - 50
            if bx == 425 and by == 230:  # snake at 47
                bx = 325
                by = 380
                turn = 'Player 2 (BLUE)'
            elif bx == 475 and diceroll <= 2 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):  # 9
                bx = bx + (50 * diceroll)
            elif bx == 475 and diceroll > 2 and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 2) - (50 * (diceroll - 3))
                by = by - 50
            elif bx == 475 and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 2) - (50 * (diceroll - 3))
                by = by - 50
                turn = 'Player 2 (BLUE)'
            elif bx == 525 and diceroll <= 1 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):  # 10
                bx = bx + (50 * diceroll)
            # ladder at number 12
            if bx == 525 and by == 380:  # ladder at 12
                bx = 575
                by = 230
            elif bx == 525 and diceroll > 1 and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 1) - (50 * (diceroll - 2))
                by = by - 50
            if bx == 525 and by == 380:  # ladder at 12
                bx = 575
                by = 230
            elif bx == 525 and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx + (50 * 1) - (50 * (diceroll - 2))
                by = by - 50
            if bx == 525 and by == 380:  # ladder at 12
                bx = 575
                by = 230
                turn = 'Player 2 (BLUE)'
            elif bx >= 575 and diceroll != 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx - (50 * (diceroll - 1))
                by = by - 50
            elif bx == 575 and diceroll == 6 and (by == 430 or by == 330 or by == 230 or by == 130 or by == 30):
                bx = bx - (50 * (diceroll - 1))
                by = by - 50
                turn = 'Player 2 (BLUE)'
            # row two
            elif bx > 325 and bx <= 575 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll != 6:
                bx = bx - (50 * diceroll)
            if bx == 525 and by == 380:  # ladder at 12
                bx = 575
                by = 230
            elif bx == 425 and by == 380:  # ladder at 14
                bx = 375
                by = 180
            elif bx == 475 and by == 330:  # snake at 28
                bx = 575
                by = 430
            elif bx == 425 and by == 230:  # snake at 47
                bx = 325
                by = 380
            elif bx == 425 and by == 180:  # ladder at 54
                bx = 475
                by = 30
            elif bx == 375 and by == 80:  # snake at 75
                bx = 525
                by = 280
            elif bx == 425 and by == -20:  # snake 94
                bx = 575
                by = 80
            elif bx == 325 and by == -20:  # snake at 96
                bx = 175
                by = 230
            elif bx > 375 and bx <= 575 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll != 6:
                bx = bx - (50 * 5)
                by = by - 50
            if bx == 525 and by == 380:  # ladder at 12
                bx = 575
                by = 230
            elif bx == 425 and by == 380:  # ladder at 14
                bx = 375
                by = 180
            elif bx == 475 and by == 330:  # snake at 28
                bx = 575
                by = 430
            elif bx == 425 and by == 230:  # snake at 47
                bx = 325
                by = 380
            elif bx == 425 and by == 180:  # ladder at 54
                bx = 475
                by = 30
            elif bx == 375 and by == 80:  # snake at 75
                bx = 525
                by = 280
            elif bx == 425 and by == -20:  # snake 94
                bx = 575
                by = 80
            elif bx == 325 and by == -20:  # snake at 96
                bx = 175
                by = 230
            elif bx > 375 and bx <= 575 and diceroll == 6 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20):
                bx = bx - (50 * diceroll)
            if bx == 525 and by == 380:  # ladder at 12
                bx = 575
                by = 230
            elif bx == 425 and by == 380:  # ladder at 14
                bx = 375
                by = 180
            elif bx == 475 and by == 330:  # snake at 28
                bx = 575
                by = 430
            elif bx == 425 and by == 230:  # snake at 47
                bx = 325
                by = 380
                turn = "Player 2 (BLUE)"
            elif bx == 425 and by == 180:  # ladder at 54
                bx = 475
                by = 30
            elif bx == 375 and by == 80:  # snake at 75
                bx = 525
                by = 280
            elif bx == 425 and by == -20:  # snake 94
                bx = 575
                by = 80
            elif bx == 325 and by == -20:  # snake at 96
                bx = 175
                by = 230
            elif bx == 375 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll != 6:
                bx = bx - (50 * diceroll)
            elif bx == 375 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 6:
                bx = bx - (50 * 5)
                by = by - 50
                turn = "Player 2 (BLUE)"
            elif bx == 325 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll < 5:
                bx = bx - (50 * diceroll)
            elif bx == 325 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 5:
                bx = bx - (50 * 4) + (50 * (diceroll - 5))
                by = by - 50
            elif bx == 325 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 6:
                bx = bx - (50 * 4) + (50 * (diceroll - 5))
                by = by - 50
                turn = "Player 2 (BLUE)"
            elif bx == 275 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll < 4:
                bx = bx - (50 * diceroll)
            if bx == 275 and by == 280:  # snake at 37
                bx = 225
                by = 430
            elif bx == 325 and by == -20:  # snake at 96
                bx = 175
                by = 230
            elif bx == 275 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll >= 4 and diceroll != 6:
                bx = bx - (50 * 3) + (50 * (diceroll - 4))
                by = by - 50
            if bx == 275 and by == 280:  # snake at 37
                bx = 225
                by = 430
            elif bx == 325 and by == -20:  # snake at 96
                bx = 175
                by = 230
            elif bx == 275 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 6:
                bx = bx - (50 * 3) + (50 * (diceroll - 4))
                by = by - 50
            if bx == 275 and by == 280:  # snake at 37
                bx = 225
                by = 430
            elif bx == 325 and by == -20:  # snake at 96
                bx = 175
                by = 230
                turn = "Player 2 (BLUE)"
            elif bx == 225 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll < 3:
                bx = bx - (50 * diceroll)
            elif bx == 225 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll >= 3 and diceroll != 6:
                bx = bx - (50 * 2) + (50 * (diceroll - 3))
                by = by - 50
            elif bx == 225 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 6:
                bx = bx - (50 * 2) + (50 * (diceroll - 3))
                by = by - 50
                turn = "Player 2 (BLUE)"
            elif bx == 175 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll < 2:
                bx = bx - (50 * diceroll)
            if bx == 175 and by == 330:  # ladder at 22
                bx = 225
                by = 180
            elif bx == 175 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll >= 2 and diceroll != 6:
                bx = bx - 50 + (50 * (diceroll - 2))
                by = by - 50
            if bx == 175 and by == 330:  # ladder at 22
                bx = 225
                by = 180
            elif bx == 175 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 6:
                bx = bx - 50 + (50 * (diceroll - 2))
                by = by - 50
            if bx == 175 and by == 330:  # ladder at 22
                bx = 225
                by = 180
                turn = "Player 2 (BLUE)"
            elif bx == 125 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll != 6:
                bx = bx + (50 * (diceroll - 1))
                by = by - 50
            if bx == 125 and by == 230:  # ladder at 41
                bx = 175
                by = 80
            elif bx == 125 and (by == 380 or by == 280 or by == 180 or by == 80 or by == -20) and diceroll == 6:
                bx = bx + (50 * (diceroll - 1))
                by = by - 50
            if bx == 125 and by == 230:  # ladder at 41
                bx = 175
                by = 80
                turn = "Player 2 (BLUE)"
            # final row
            elif by == -20 and (bx == 525 or bx == 575) and diceroll != 6:
                bx = bx - (50 * diceroll)
            elif by == -20 and (bx == 525 or bx == 575) and diceroll == 6:
                bx = bx - (50 * diceroll)
                turn = 'red'
            elif by == -20 and bx == 475 and diceroll < 5:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 475 and diceroll == 5:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 475 and diceroll == 6:
                bx = bx
            elif by == -20 and bx == 425 and diceroll != 6:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 425 and diceroll == 6:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 375 and diceroll < 6:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 375 and bx >= 125 and diceroll == 6:
                bx = bx
            elif by == -20 and bx == 325 and bx >= 125 and diceroll >= 5:
                bx = bx
            elif by == -20 and bx == 325 and bx >= 125 and diceroll < 5:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 275 and bx >= 125 and diceroll >= 4:
                bx = bx
            elif by == -20 and bx == 275 and bx >= 125 and diceroll < 4:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 225 and bx >= 125 and diceroll >= 3:
                bx = bx
            elif by == -20 and bx == 225 and bx >= 125 and diceroll < 3:
                bx = bx - (50 * diceroll)
            elif by == -20 and bx == 175 and bx > 125 and diceroll >= 2:
                bx = bx
            # # for player three
            elif Roll() and turn == 'Player 3 (YELLOW)':
                turn = 'Player 1 (RED)'
                if diceroll == 6 and yx == 80 and yy == 380:
                    yx = 125
                    yy = 430
                    turn = 'Player 3 (YELLOW)'
            elif yx in range(125, 325) and diceroll != 6 and (
                    yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * diceroll)
            if yx == 275 and yy == 430:  # ladder at no 4
                yx = 325
                yy = 180
            if yx == 275 and yy == 280:  # snake at 37
                yx = 225
                yy = 430
            elif yx in range(125, 325) and diceroll == 6 and (
                    yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * diceroll)
            if yx == 275 and yy == 280:  # snake at 37
                yx = 225
                yy = 430
                turn = 'Player 3 (YELLOW)'
            elif yx == 325 and diceroll != 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * diceroll)
            if yx == 275 and yy == 430:  # ladder at no 4
                yx = 325
                yy = 180
            elif yx == 325 and diceroll == 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 5)
                yy = yy - 50
                turn = 'Player 3 (YELLOW)'
            elif yx == 375 and diceroll <= 4 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):  # 7
                yx = yx + (50 * diceroll)
            elif yx == 375 and diceroll > 4 and diceroll != 6 and (
                    yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 4)
                yy = yy - 50
            elif yx == 375 and diceroll == 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 4) - (50 * (diceroll - 5))
                yy = yy - 50
                turn = 'Player 3 (YELLOW)'
            elif yx == 425 and diceroll <= 3 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):  # 8
                yx = yx + (50 * diceroll)
            if yx == 425 and yy == 230:  # snake at 47
                yx = 325
                yy = 380
            elif yx == 425 and diceroll > 3 and diceroll != 6 and (
                    yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 3) - (50 * (diceroll - 4))
                yy = yy - 50
            if yx == 425 and yy == 230:  # snake at 47
                yx = 325
                yy = 380
            elif yx == 425 and diceroll == 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 3) - (50 * (diceroll - 4))
                yy = yy - 50
            if yx == 425 and yy == 230:  # snake at 47
                yx = 325
                yy = 380
                turn = 'Player 3 (YELLOW)'
            elif yx == 475 and diceroll <= 2 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):  # 9
                yx = yx + (50 * diceroll)
            elif yx == 475 and diceroll > 2 and diceroll != 6 and (
                    yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 2) - (50 * (diceroll - 3))
                yy = yy - 50
            elif yx == 475 and diceroll == 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 2) - (50 * (diceroll - 3))
                yy = yy - 50
                turn = 'Player 3 (YELLOW)'
            elif yx == 525 and diceroll <= 1 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):  # 10
                yx = yx + (50 * diceroll)
            # ladder at number 12
            if yx == 525 and yy == 380:  # ladder at 12
                yx = 575
                yy = 230

            elif yx == 525 and diceroll > 1 and diceroll != 6 and (
                    yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 1) - (50 * (diceroll - 2))
                yy = yy - 50
            if yx == 525 and yy == 380:  # ladder at 12
                yx = 575
                yy = 230
            elif yx == 525 and diceroll == 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx + (50 * 1) - (50 * (diceroll - 2))
                yy = yy - 50
            if yx == 525 and yy == 380:  # ladder at 12
                yx = 575
                yy = 230
                turn = 'Player 3 (YELLOW)'
            elif yx >= 575 and diceroll != 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx - (50 * (diceroll - 1))
                yy = yy - 50
            elif yx == 575 and diceroll == 6 and (yy == 430 or yy == 330 or yy == 230 or yy == 130 or yy == 30):
                yx = yx - (50 * (diceroll - 1))
                yy = yy - 50
                turn = 'Player 3 (YELLOW)'
            # row two
            elif yx > 325 and yx <= 575 and (
                    yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll != 6:
                yx = yx - (50 * diceroll)
            if yx == 525 and yy == 380:  # ladder at 12
                yx = 575
                yy = 230
            elif yx == 425 and yy == 380:  # ladder at 14
                yx = 375
                yy = 180
            elif yx == 475 and yy == 330:  # snake at 28
                yx = 575
                yy = 430
            elif yx == 425 and yy == 230:  # snake at 47
                yx = 325
                yy = 380
            elif yx == 425 and yy == 180:  # ladder at 54
                yx = 475
                yy = 30
            elif yx == 375 and yy == 80:  # snake at 75
                yx = 525
                yy = 280
            elif yx == 425 and yy == -20:  # snake 94
                yx = 575
                yy = 80
            elif yx == 325 and yy == -20:  # snake at 96
                yx = 175
                yy = 230
            elif yx > 375 and yx <= 575 and (
                    yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll != 6:
                yx = yx - (50 * 5)
                yy = yy - 50
            if yx == 525 and yy == 380:  # ladder at 12
                yx = 575
                yy = 230
            elif yx == 425 and yy == 380:  # ladder at 14
                yx = 375
                yy = 180
            elif yx == 475 and yy == 330:  # snake at 28
                yx = 575
                yy = 430
            elif yx == 425 and yy == 230:  # snake at 47
                yx = 325
                yy = 380
            elif yx == 425 and yy == 180:  # ladder at 54
                yx = 475
                yy = 30
            elif yx == 375 and yy == 80:  # snake at 75
                yx = 525
                yy = 280
            elif yx == 425 and yy == -20:  # snake 94
                yx = 575
                yy = 80
            elif yx == 325 and yy == -20:  # snake at 96
                yx = 175
                yy = 230
            elif yx > 375 and yx <= 575 and diceroll == 6 and (
                    yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20):
                yx = yx - (50 * diceroll)
            if yx == 525 and yy == 380:  # ladder at 12
                yx = 575
                yy = 230
            elif yx == 425 and yy == 380:  # ladder at 14
                yx = 375
                yy = 180
            elif yx == 475 and yy == 330:  # snake at 28
                yx = 575
                yy = 430
            elif yx == 425 and yy == 230:  # snake at 47
                yx = 325
                yy = 380
                turn = "Player 2 (BLUE)"
            elif yx == 425 and yy == 180:  # ladder at 54
                yx = 475
                yy = 30
            elif yx == 375 and yy == 80:  # snake at 75
                yx = 525
                yy = 280
            elif yx == 425 and yy == -20:  # snake 94
                yx = 575
                yy = 80
            elif yx == 325 and yy == -20:  # snake at 96
                yx = 175
                yy = 230
            elif yx == 375 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll != 6:
                yx = yx - (50 * diceroll)
            elif yx == 375 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 6:
                yx = yx - (50 * 5)
                yy = yy - 50
                turn = "Player 2 (BLUE)"
            elif yx == 325 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll < 5:
                yx = yx - (50 * diceroll)
            elif yx == 325 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 5:
                yx = yx - (50 * 4) + (50 * (diceroll - 5))
                yy = yy - 50
            elif yx == 325 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 6:
                yx = yx - (50 * 4) + (50 * (diceroll - 5))
                yy = yy - 50
                turn = "Player 2 (BLUE)"
            elif yx == 275 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll < 4:
                yx = yx - (50 * diceroll)
            if yx == 275 and yy == 280:  # snake at 37
                yx = 225
                yy = 430
            elif yx == 325 and yy == -20:  # snake at 96
                yx = 175
                yy = 230
            elif yx == 275 and (
                    yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll >= 4 and diceroll != 6:
                yx = yx - (50 * 3) + (50 * (diceroll - 4))
                yy = yy - 50
            if yx == 275 and yy == 280:  # snake at 37
                yx = 225
                yy = 430
            elif yx == 325 and yy == -20:  # snake at 96
                yx = 175
                yy = 230
            elif yx == 275 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 6:
                yx = yx - (50 * 3) + (50 * (diceroll - 4))
                yy = yy - 50
            if yx == 275 and yy == 280:  # snake at 37
                yx = 225
                yy = 430
            elif yx == 325 and yy == -20:  # snake at 96
                yx = 175
                yy = 230
                turn = "Player 2 (BLUE)"
            elif yx == 225 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll < 3:
                yx = yx - (50 * diceroll)
            elif yx == 225 and (
                    yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll >= 3 and diceroll != 6:
                yx = yx - (50 * 2) + (50 * (diceroll - 3))
                yy = yy - 50
            elif yx == 225 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 6:
                yx = yx - (50 * 2) + (50 * (diceroll - 3))
                yy = yy - 50
                turn = "Player 2 (BLUE)"
            elif yx == 175 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll < 2:
                yx = yx - (50 * diceroll)
            if yx == 175 and yy == 330:  # ladder at 22
                yx = 225
                yy = 180
            elif yx == 175 and (
                    yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll >= 2 and diceroll != 6:
                yx = yx - 50 + (50 * (diceroll - 2))
                yy = yy - 50
            if yx == 175 and yy == 330:  # ladder at 22
                yx = 225
                yy = 180
            elif yx == 175 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 6:
                yx = yx - 50 + (50 * (diceroll - 2))
                yy = yy - 50
            if yx == 175 and yy == 330:  # ladder at 22
                yx = 225
                yy = 180
                turn = "Player 2 (BLUE)"
            elif yx == 125 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll != 6:
                yx = yx + (50 * (diceroll - 1))
                yy = yy - 50
            if yx == 125 and yy == 230:  # ladder at 41
                yx = 175
                yy = 80
            elif yx == 125 and (yy == 380 or yy == 280 or yy == 180 or yy == 80 or yy == -20) and diceroll == 6:
                yx = yx + (50 * (diceroll - 1))
                yy = yy - 50
            if yx == 125 and yy == 230:  # ladder at 41
                yx = 175
                yy = 80
                turn = "Player 2 (BLUE)"
            # final row
            elif yy == -20 and (yx == 525 or yx == 575) and diceroll != 6:
                yx = yx - (50 * diceroll)
            elif yy == -20 and (yx == 525 or yx == 575) and diceroll == 6:
                yx = yx - (50 * diceroll)
                turn = 'red'
            elif yy == -20 and yx == 475 and diceroll < 5:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 475 and diceroll == 5:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 475 and diceroll == 6:
                yx = yx
            elif yy == -20 and yx == 425 and diceroll != 6:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 425 and diceroll == 6:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 375 and diceroll < 6:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 375 and yx >= 125 and diceroll == 6:
                yx = yx
            elif yy == -20 and yx == 325 and yx >= 125 and diceroll >= 5:
                yx = yx
            elif yy == -20 and yx == 325 and yx >= 125 and diceroll < 5:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 275 and yx >= 125 and diceroll >= 4:
                yx = yx
            elif yy == -20 and yx == 275 and yx >= 125 and diceroll < 4:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 225 and yx >= 125 and diceroll >= 3:
                yx = yx
            elif yy == -20 and yx == 225 and yx >= 125 and diceroll < 3:
                yx = yx - (50 * diceroll)
            elif yy == -20 and yx == 175 and yx > 125 and diceroll >= 2:
                yx = yx
    redpawn(rx, ry)
    bluepawn(bx, by)
    yellowpawn(yx, yy)
    pygame.display.update()
    if rx == 125 and ry == -20:
        screen.fill((50, 153, 213,))
        value = score_font.render("RED WON", True, (0, 0, 0))
        screen.blit(value, [250, 200])
        running = False
    if bx == 125 and by == -20:
        screen.fill((50, 153, 213,))
        value = score_font.render("BLUE WON", True, (0, 0, 0))
        screen.blit(value, [250, 200])
        running = False
    if yx == 125 and yy == -20:
        screen.fill((50, 153, 213,))
        value = score_font.render("YELLOW WON", True, (0, 0, 0))
        screen.blit(value, [250, 200])
        running = False
    time.sleep(1.3)
pygame.display.update()
pygame.quit()
quit()