import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((650, 500))
white = (255, 255, 255)
pygame.display.set_caption("Snakes And Ladders")
# bckground image
bckimg = pygame.image.load('/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/board.jpg')
# img = pygame.image.load('dice (6).png')
arrow = pygame.image.load('/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/red1.png')
stg = pygame.image.load('/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/starts.jpg')
# players
r1 = pygame.image.load('/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/redtoken.png')
b1 = pygame.image.load('/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/bluetoken.png')
y1 = pygame.image.load('/home/rohit/Desktop/python-project-Rohit-Jagtap-au17/images/yellowtoken.png')
rx = 100
ry = 251

b1x = 100
b1y = 362

yx = 100
yy = 447

def bck():
    screen.blit(stg, (0, 0))
    screen.blit(bckimg, (155, 10))
    screen.blit(arrow, (10, 50))
def rplayer(x, y):
    screen.blit(r1, (x, y))
def bplayer(x, y):
    screen.blit(b1, (x, y))
def yplayer(x, y):
    screen.blit(y1, (x, y))

button = pygame.Rect(10, 50, 40, 40)
score_font = pygame.font.SysFont("comicsansms", 35)
score_font1 = pygame.font.SysFont("comicsansms", 25)
score_font2 = pygame.font.SysFont("comicsansms", 20)
clock = pygame.time.Clock()
def players():
    value2= score_font1.render("Player 1", True, (255, 0, 0))
    screen.blit(value2, [5, 251])
    value3= score_font1.render("Player 2", True, (0, 0, 255))
    screen.blit(value3, [5, 362])
    value4 = score_font1.render("Player 3", True, (255, 255, 255))
    screen.blit(value4, [5, 447])
def rollr():
    val1= score_font2.render("Your turn", True, (255, 255, 255))
    screen.blit(val1, [25, 288])
def rollb():
    val1= score_font2.render("Your turn", True, (255, 255, 255))
    screen.blit(val1, [25, 399])
def rolly():
    val1= score_font2.render("Your turn", True, (255, 255, 255))
    screen.blit(val1, [25, 457])
def pickNumber():
    diceroll = random.randint(1, 6)
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
# game loop
running = True
turn='red'
while running:
    screen.fill((0, 255, 195))
    bck()
    players()
    if turn =='red':
        rollr()
    elif turn =='blue':
        rollb()
    elif turn =='yellow':
        rolly()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice,diceroll = pickNumber()
                screen.blit(dice, (58, 48))
                print(diceroll, turn,(yx,yy))
            if pickNumber() and turn=='red':
                turn='blue'
                if diceroll == 6 and rx<162 and ry==251:
                    rx=rx+62
                    ry=447
                    turn='red'
                elif rx>=162 and rx<358 and(ry==447 or ry==349 or ry==251 or ry==153 or ry==55)and diceroll!=6:
                    rx=rx+(49*diceroll)
                    if rx==309 and ry==447:
                        rx=358
                        ry=349
                    elif rx==456 and ry==349:
                        rx=358
                        ry=447
                    elif rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    elif rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                    elif rx==554 and ry==55:
                        rx=505
                        ry=202
                elif rx>=162 and rx<358 and(ry==447 or ry==349 or ry==251 or ry==153 or ry==55)and diceroll==6:
                    rx=rx+(49*diceroll)
                    if rx==309 and ry==447:
                        rx=358
                        ry=349
                    elif rx==456 and ry==349:
                        rx=358
                        ry=447
                    elif rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    elif rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                    elif rx==554 and ry==55:
                        rx=505
                        ry=202
                    turn='red'
                elif rx>=358 and rx<407 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*diceroll)
                    if rx==456 and ry==349:
                        rx=358
                        ry=447
                    elif rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                    elif rx==554 and ry==55 and diceroll==4:
                        rx=505
                        ry=202
                elif rx>=358 and rx<407 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*5)-(49*(diceroll-6))
                    ry=ry-49
                    turn='red'
                elif rx>=407 and rx<456 and diceroll<=4 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):#7
                    rx=rx+(49*diceroll)
                    if rx==456 and ry==349:
                        rx=358
                        ry=447
                    elif rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==554 and ry==55 and diceroll==3:
                        rx=505
                        ry=202
                elif rx>=407 and rx<456 and diceroll>4 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*4)-(49*(diceroll-5))
                    ry=ry-49
                elif rx>=407 and rx<456 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*4)-(49*(diceroll-5))
                    ry=ry-49
                    turn='red'
                elif rx>=456 and rx<505 and diceroll<=3 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):#8
                    rx=rx+(49*diceroll)
                    if rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==554 and ry==55 and diceroll==2:
                        rx=505
                        ry=202
                elif rx>=456 and rx<505 and diceroll>3 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*3)-(49*(diceroll-4))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                elif rx>=456 and rx<505 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*3)-(49*(diceroll-4))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    turn='red'
                elif rx>=505 and rx<554 and diceroll<=2 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):#9
                    rx=rx+(49*diceroll)
                    if rx==603 and ry==251:
                        rx=554
                        ry=153
                    elif rx==554 and ry==55 and diceroll==1:
                        rx=505
                        ry=202
                elif rx>=505 and rx<554 and diceroll>2 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*2)-(49*(diceroll-3))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                elif rx>=505 and rx<554 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*2)-(49*(diceroll-3))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    turn='red'
                elif rx>=554 and rx<603 and diceroll==1 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55): #10
                    rx=rx+(49*diceroll)
                    if rx==603 and ry==251:
                        rx=554
                        ry=153
                elif rx>=554 and rx<603 and diceroll>1 and diceroll!=6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*1)-(49*(diceroll-2))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                elif rx>=554 and rx<603 and diceroll==6 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55):
                    rx=rx+(49*1)-(49*(diceroll-2))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    turn='red'
                elif rx>=603 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55)and diceroll!=6:
                    rx=rx-(49*(diceroll-1))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    elif rx==358 and ry==104:
                        rx=260
                        ry=202
                elif rx>=603 and (ry==447 or ry==349 or ry==251 or ry==153 or ry==55)and diceroll==6:
                    rx=rx-(49*(diceroll-1))
                    ry=ry-49
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    elif rx==358 and ry==104:
                        rx=260
                        ry=202
                    turn='red'
                #c2 starts from here
                elif rx>358 and rx<=603 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6) and diceroll!=6:
                    rx=rx-(49*diceroll)
                    if rx==505 and ry==398:
                        rx=407
                        ry=251
                    elif rx==505 and ry==300:
                        rx=554
                        ry=251
                    elif rx==456 and ry==202:
                        rx=603
                        ry=300
                    elif rx==456 and ry==104:
                        rx=554
                        ry=6
                    elif rx==162 and ry==300:
                        rx=260
                        ry=447
                    elif rx==358 and ry==104:
                        rx=260
                        ry=202
                elif rx>407 and rx<=603 and diceroll!=6 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6):
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6:
                        rx=162
                        ry=251
                    elif rx==162 and ry==300:
                        rx=260
                        ry=447
                    elif rx==211 and ry==6:
                        rx=162
                        ry=251
                elif rx>407 and rx<=603 and diceroll==6 and (ry==398 or ry==300 or ry==202 or ry==104 or ry==6):
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6:
                        rx=162
                        ry=251
                    elif rx==162 and ry==300:
                        rx=260
                        ry=447
                    elif rx==211 and ry==6:
                        rx=162
                        ry=251
                    turn='red'
                elif rx==407 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll!=6:
                    rx=rx-(49*diceroll)
                    if rx==358 and ry==104:
                        rx=260
                        ry=202
                    elif rx==211 and ry==6:
                        rx=162
                        ry=251
                elif rx==407 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6:
                    rx=rx-(49*5)
                    ry=ry-49
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                    turn='red'
                elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll<5:
                    rx=rx-(49*diceroll)
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll==5:
                    rx=rx-(49*4)+(49*(diceroll-5))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                elif rx==358 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll==6:
                    rx=rx-(49*4)+(49*(diceroll-5))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    turn='red'
                elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll<4:
                    rx=rx-(49*diceroll)
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll>=4 and diceroll!=6:
                    rx=rx-(49*3)+(49*(diceroll-4))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                elif rx==309 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6:
                    rx=rx-(49*3)+(49*(diceroll-4))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    turn='red'
                elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll<3:
                    rx=rx-(49*diceroll)
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll>=3 and diceroll!=6:
                    rx=rx-(49*2)+(49*(diceroll-3))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                elif rx==260 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll==6:
                    rx=rx-(49*2)+(49*(diceroll-3))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    turn='red'
                elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll<2:
                    rx=rx-(49*diceroll)
                    if rx==162 and ry==300:
                        rx=260
                        ry=447
                elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll!=6 and diceroll>=2:
                    rx=rx-49+(49*(diceroll-2))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                elif rx==211 and (ry==398 or ry==300 or ry==202 or ry==104) and diceroll==6 :
                    rx=rx-49+(49*(diceroll-2))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    turn='red'
                elif rx==162 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll!=6:
                    rx=rx+(49*(diceroll-1))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                elif rx==162 and (ry==398 or ry==300 or ry==202 or ry==104 ) and diceroll==6:
                    rx=rx+(49*(diceroll-1))
                    ry=ry-49
                    if rx==211 and ry==251:
                        rx=260
                        ry=153
                    elif rx==211 and ry==153:
                        rx=162
                        ry=55
                    elif rx==260 and ry==251:
                        rx=260
                        ry=398
                    elif rx==407 and ry==153:
                        rx=358
                        ry=251
                    turn='red'
                #final row
                elif ry==6 and (rx==554 or rx==603) and diceroll!=6:
                    rx=rx-(49*diceroll)
                elif ry==6 and (rx==554 or rx==603) and diceroll==6:
                    rx=rx-(49*diceroll)
                    turn='red'
                elif ry==6 and rx==456 and diceroll<5:
                    rx=rx-(49*diceroll)
                elif ry==6 and rx==456 and diceroll==5:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==5:
                        rx=162
                        ry=251
                elif ry==6 and rx==456 and diceroll==6:
                    rx=rx
                elif ry==6 and rx==505 and diceroll!=6:
                    rx=rx-(49*diceroll)
                elif ry==6 and rx==505 and diceroll==6:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==6:
                        rx=162
                        ry=251
                elif ry==6 and rx==407 and diceroll <6:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==4:
                        rx=162
                        ry=251
                elif ry==6 and rx==407 and rx>=162  and diceroll ==6:
                    rx=rx
                elif ry==6 and rx==358 and rx>=162  and diceroll >=5:
                    rx=rx
                elif ry==6 and rx==358 and rx>=162  and diceroll <5:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==3:
                        rx=162
                        ry=251
                elif ry==6 and rx==309 and rx>=162  and diceroll >=4:
                    rx=rx
                elif ry==6 and rx==309 and rx>=162  and diceroll <4:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==2:
                        rx=162
                        ry=251
                elif ry==6 and rx==260 and rx>=162  and diceroll >=3:
                    rx=rx
                elif ry==6 and rx==260 and rx>=162  and diceroll <3:
                    rx=rx-(49*diceroll)
                    if rx==211 and ry==6 and diceroll==1:
                        rx=162
                        ry=251
                elif ry==6 and rx==211 and rx>162 and diceroll >=2:
                    rx=rx
            #blue
            elif pickNumber() and turn=='blue':
                turn='yellow'
                if diceroll == 6 and b1x<162 and b1y==362:
                    b1x = b1x + 62
                    b1y=450
                    turn='blue'
                elif b1x>=162 and b1x<358 and(b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58)and diceroll!=6:
                    b1x=b1x+(49*diceroll)
                    if b1x==309 and b1y==450:
                        b1x=358
                        b1y=352
                    elif b1x==456 and b1y==352:
                        b1x=358
                        b1y=450
                    elif b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    elif b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                    elif b1x==407 and b1y==156:
                        b1x=358
                        b1y=254
                    elif b1x==554 and b1y==58:
                        b1x=505
                        b1y=205
                elif b1x>=162 and b1x<358 and(b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58)and diceroll==6:
                    b1x=b1x+(49*diceroll)
                    if b1x==309 and b1y==450:
                        b1x=358
                        b1y=352
                    elif b1x==456 and b1y==352:
                        b1x=358
                        b1y=450
                    elif b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    elif b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                    elif b1x==407 and b1y==156:
                        b1x=358
                        b1y=254
                    elif b1x==554 and b1y==58:
                        b1x=505
                        b1y=205
                    turn='blue'
                elif b1x>=358 and b1x<407 and diceroll!=6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*diceroll)
                    if b1x==456 and b1y==352:
                        b1x=358
                        b1y=450
                    elif b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                    elif b1x==407 and b1y==156:
                        b1x=358
                        b1y=254
                    elif b1x==554 and b1y==58 and diceroll==4:
                        b1x=505
                        b1y=205
                elif b1x>=358 and b1x<407 and diceroll==6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*5)-(49*(diceroll-6))
                    b1y=b1y-49
                    turn='blue'
                elif b1x>=407 and b1x<456 and diceroll<=4 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):#7
                    b1x=b1x+(49*diceroll)
                    if b1x==456 and b1y==352:
                        b1x=358
                        b1y=450
                    elif b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                    elif b1x==554 and b1y==58 and diceroll==3:
                        b1x=505
                        b1y=205
                elif b1x>=407 and b1x<456 and diceroll>4 and diceroll!=6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*4)-(49*(diceroll-5))
                    b1y=b1y-49
                elif b1x>=407 and b1x<456 and diceroll==6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*4)-(49*(diceroll-5))
                    b1y=b1y-49
                    turn='blue'
                elif b1x>=456 and b1x<505 and diceroll<=3 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):#8
                    b1x=b1x+(49*diceroll)
                    if b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                    elif b1x==554 and b1y==58 and diceroll==2:
                        b1x=505
                        b1y=205
                elif b1x>=456 and b1x<505 and diceroll>3 and diceroll!=6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*3)-(49*(diceroll-4))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                elif b1x>=456 and b1x<505 and diceroll==6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*3)-(49*(diceroll-4))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    turn='blue'
                elif b1x>=505 and b1x<554 and diceroll<=2 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):#9
                    b1x=b1x+(49*diceroll)
                    if b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                    elif b1x==554 and b1y==58 and diceroll==1:
                        b1x=505
                        b1y=205
                elif b1x>=505 and b1x<554 and diceroll>2 and diceroll!=6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*2)-(49*(diceroll-3))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                elif b1x>=505 and b1x<554 and diceroll==6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*2)-(49*(diceroll-3))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                    turn='blue'
                elif b1x>=554 and b1x<603 and diceroll==1 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58): #10
                    b1x=b1x+(49*diceroll)
                    if b1x==603 and b1y==254:
                        b1x=554
                        b1y=156
                elif b1x>=554 and b1x<603 and diceroll>1 and diceroll!=6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*1)-(49*(diceroll-2))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                elif b1x>=554 and b1x<603 and diceroll==6 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58):
                    b1x=b1x+(49*1)-(49*(diceroll-2))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                    turn='blue'
                elif b1x>=603 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58)and diceroll!=6:
                    b1x=b1x-(49*(diceroll-1))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                    elif b1x==358 and b1y==107:
                        b1x=260
                        b1y=205
                elif b1x>=603 and (b1y==450 or b1y==352 or b1y==254 or b1y==156 or b1y==58)and diceroll==6:
                    b1x=b1x-(49*(diceroll-1))
                    b1y=b1y-49
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                    elif b1x==358 and b1y==107:
                        b1x=260
                        b1y=205
                    turn='blue'
                #c2 starts from here
                elif b1x>358 and b1x<=603 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 or b1y==9) and diceroll!=6:
                    b1x=b1x-(49*diceroll)
                    if b1x==505 and b1y==401:
                        b1x=407
                        b1y=254
                    elif b1x==505 and b1y==303:
                        b1x=554
                        b1y=254
                    elif b1x==456 and b1y==205:
                        b1x=603
                        b1y=303
                    elif b1x==456 and b1y==107:
                        b1x=554
                        b1y=9
                    elif b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                    elif b1x==358 and b1y==107:
                        b1x=260
                        b1y=205
                elif b1x>407 and b1x<=603 and diceroll!=6 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 or b1y==9):
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9:
                        b1x=162
                        b1y=254
                    elif b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                    elif b1x==211 and b1y==9:
                        b1x=162
                        b1y=254
                elif b1x>407 and b1x<=603 and diceroll==6 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 or b1y==9):
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9:
                        b1x=162
                        b1y=254
                    elif b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                    elif b1x==211 and b1y==9:
                        b1x=162
                        b1y=254
                    turn='blue'
                elif b1x==407 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll!=6:
                    b1x=b1x-(49*diceroll)
                    if b1x==358 and b1y==107:
                        b1x=260
                        b1y=205
                    elif b1x==211 and b1y==9:
                        b1x=162
                        b1y=254
                elif b1x==407 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll==6:
                    b1x=b1x-(49*5)
                    b1y=b1y-49
                    if b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                    turn='blue'
                elif b1x==358 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll<5:
                    b1x=b1x-(49*diceroll)
                    if b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                elif b1x==358 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll==5:
                    b1x=b1x-(49*4)+(49*(diceroll-5))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                elif b1x==358 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll==6:
                    b1x=b1x-(49*4)+(49*(diceroll-5))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    turn='blue'
                elif b1x==309 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll<4:
                    b1x=b1x-(49*diceroll)
                    if b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                elif b1x==309 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll>=4 and diceroll!=6:
                    b1x=b1x-(49*3)+(49*(diceroll-4))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                elif b1x==309 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll==6:
                    b1x=b1x-(49*3)+(49*(diceroll-4))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    turn='blue'
                elif b1x==260 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll<3:
                    b1x=b1x-(49*diceroll)
                    if b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                elif b1x==260 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll>=3 and diceroll!=6:
                    b1x=b1x-(49*2)+(49*(diceroll-3))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                elif b1x==260 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll==6:
                    b1x=b1x-(49*2)+(49*(diceroll-3))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    turn='blue'
                elif b1x==211 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll<2:
                    b1x=b1x-(49*diceroll)
                    if b1x==162 and b1y==303:
                        b1x=260
                        b1y=450
                elif b1x==211 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll!=6 and diceroll>=2:
                    b1x=b1x-49+(49*(diceroll-2))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                elif b1x==211 and (b1y==401 or b1y==303 or b1y==205 or b1y==107) and diceroll==6 :
                    b1x=b1x-49+(49*(diceroll-2))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    turn='blue'
                elif b1x==162 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll!=6:
                    b1x=b1x+(49*(diceroll-1))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    elif b1x==407 and b1y==156:
                        b1x=358
                        b1y=254
                elif b1x==162 and (b1y==401 or b1y==303 or b1y==205 or b1y==107 ) and diceroll==6:
                    b1x=b1x+(49*(diceroll-1))
                    b1y=b1y-49
                    if b1x==211 and b1y==254:
                        b1x=260
                        b1y=156
                    elif b1x==211 and b1y==156:
                        b1x=162
                        b1y=58
                    elif b1x==260 and b1y==254:
                        b1x=260
                        b1y=401
                    elif b1x==407 and b1y==156:
                        b1x=358
                        b1y=254
                    turn='blue'
                #final row
                elif b1y==9 and (b1x==554 or b1x==603) and diceroll!=6:
                    b1x=b1x-(49*diceroll)
                elif b1y==9 and (b1x==554 or b1x==603) and diceroll==6:
                    b1x=b1x-(49*diceroll)
                    turn='blue'
                elif b1y==9 and b1x==456 and diceroll<5:
                    b1x=b1x-(49*diceroll)
                elif b1y==9 and b1x==456 and diceroll==5:
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9 and diceroll==5:
                        b1x=162
                        b1y=254
                elif b1y==9 and b1x==456 and diceroll==6:
                    b1x=b1x
                elif b1y==9 and b1x==505 and diceroll!=6:
                    b1x=b1x-(49*diceroll)
                elif b1y==9 and b1x==505 and diceroll==6:
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9 and diceroll==6:
                        b1x=162
                        b1y=254
                elif b1y==9 and b1x==407 and diceroll <6:
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9 and diceroll==4:
                        b1x=162
                        b1y=254
                elif b1y==9 and b1x==407 and b1x>=162  and diceroll ==6:
                    b1x=b1x
                elif b1y==9 and b1x==358 and b1x>=162  and diceroll >=5:
                    b1x=b1x
                elif b1y==9 and b1x==358 and b1x>=162  and diceroll <5:
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9 and diceroll==3:
                        b1x=162
                        b1y=254
                elif b1y==9 and b1x==309 and b1x>=162  and diceroll >=4:
                    b1x=b1x
                elif b1y==9 and b1x==309 and b1x>=162  and diceroll <4:
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9 and diceroll==2:
                        b1x=162
                        b1y=254
                elif b1y==9 and b1x==260 and b1x>=162  and diceroll >=3:
                    b1x=b1x
                elif b1y==9 and b1x==260 and b1x>=162  and diceroll <3:
                    b1x=b1x-(49*diceroll)
                    if b1x==211 and b1y==9 and diceroll==1:
                        b1x=162
                        b1y=254
                elif b1y==9 and b1x==211 and b1x>162 and diceroll >=2:
                    b1x=b1x
                    # for yellow

            elif pickNumber() and turn == 'yellow':
                turn = 'red'
                if diceroll == 6 and yx < 162 and yy == 447:
                    yx = yx + 62
                    yy = 447
                    turn = 'yellow'
                elif yx >= 162 and yx < 358 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55) and diceroll != 6:
                    yx = yx + (49 * diceroll)
                    if yx == 309 and yy == 447:
                        yx = 358
                        yy = 349
                    elif yx == 456 and yy == 349:
                        yx = 358
                        yy = 447
                    elif yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    elif yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                    elif yx == 407 and yy == 153:
                        yx = 358
                        yy = 251
                    elif yx == 554 and yy == 55:
                        yx = 505
                        yy = 202
                elif yx >= 162 and yx < 358 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55) and diceroll == 6:
                    yx = yx + (49 * diceroll)
                    if yx == 309 and yy == 447:
                        yx = 358
                        yy = 349
                    elif yx == 456 and yy == 349:
                        yx = 358
                        yy = 447
                    elif yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    elif yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                    elif yx == 407 and yy == 153:
                        yx = 358
                        yy = 251
                    elif yx == 554 and yy == 55:
                        yx = 505
                        yy = 202
                    turn = 'yellow'
                elif yx >= 358 and yx < 407 and diceroll != 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * diceroll)
                    if yx == 456 and yy == 349:
                        yx = 358
                        yy = 447
                    elif yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                    elif yx == 407 and yy == 153:
                        yx = 358
                        yy = 251
                    elif yx == 554 and yy == 55 and diceroll == 4:
                        yx = 505
                        yy = 202
                elif yx >= 358 and yx < 407 and diceroll == 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 5) - (49 * (diceroll - 6))
                    yy = yy - 49
                    turn = 'yellow'
                elif yx >= 407 and yx < 456 and diceroll <= 4 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):  # 7
                    yx = yx + (49 * diceroll)
                    if yx == 456 and yy == 349:
                        yx = 358
                        yy = 447
                    elif yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                    elif yx == 554 and yy == 55 and diceroll == 3:
                        yx = 505
                        yy = 202
                elif yx >= 407 and yx < 456 and diceroll > 4 and diceroll != 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 4) - (49 * (diceroll - 5))
                    yy = yy - 49
                elif yx >= 407 and yx < 456 and diceroll == 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 4) - (49 * (diceroll - 5))
                    yy = yy - 49
                    turn = 'yellow'
                elif yx >= 456 and yx < 505 and diceroll <= 3 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):  # 8
                    yx = yx + (49 * diceroll)
                    if yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                    elif yx == 554 and yy == 55 and diceroll == 2:
                        yx = 505
                        yy = 202
                elif yx >= 456 and yx < 505 and diceroll > 3 and diceroll != 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 3) - (49 * (diceroll - 4))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                elif yx >= 456 and yx < 505 and diceroll == 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 3) - (49 * (diceroll - 4))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    turn = 'yellow'
                elif yx >= 505 and yx < 554 and diceroll <= 2 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):  # 9
                    yx = yx + (49 * diceroll)
                    if yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                    elif yx == 554 and yy == 55 and diceroll == 1:
                        yx = 505
                        yy = 202
                elif yx >= 505 and yx < 554 and diceroll > 2 and diceroll != 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 2) - (49 * (diceroll - 3))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                elif yx >= 505 and yx < 554 and diceroll == 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 2) - (49 * (diceroll - 3))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                    turn = 'yellow'
                elif yx >= 554 and yx < 603 and diceroll == 1 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):  # 10
                    yx = yx + (49 * diceroll)
                    if yx == 603 and yy == 251:
                        yx = 554
                        yy = 153
                elif yx >= 554 and yx < 603 and diceroll > 1 and diceroll != 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 1) - (49 * (diceroll - 2))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                elif yx >= 554 and yx < 603 and diceroll == 6 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55):
                    yx = yx + (49 * 1) - (49 * (diceroll - 2))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                    turn = 'yellow'
                elif yx >= 603 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55) and diceroll != 6:
                    yx = yx - (49 * (diceroll - 1))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                    elif yx == 358 and yy == 104:
                        yx = 260
                        yy = 202
                elif yx >= 603 and (yy == 447 or yy == 349 or yy == 251 or yy == 153 or yy == 55) and diceroll == 6:
                    yx = yx - (49 * (diceroll - 1))
                    yy = yy - 49
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                    elif yx == 358 and yy == 104:
                        yx = 260
                        yy = 202
                    turn = 'yellow'
                # c2 starts from here
                elif yx > 358 and yx <= 603 and (yy == 398 or yy == 300 or yy == 202 or yy == 104 or yy == 6) and diceroll != 6:
                    yx = yx - (49 * diceroll)
                    if yx == 505 and yy == 398:
                        yx = 407
                        yy = 251
                    elif yx == 505 and yy == 300:
                        yx = 554
                        yy = 251
                    elif yx == 456 and yy == 202:
                        yx = 603
                        yy = 300
                    elif yx == 456 and yy == 104:
                        yx = 554
                        yy = 6
                    elif yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                    elif yx == 358 and yy == 104:
                        yx = 260
                        yy = 202
                elif yx > 407 and yx <= 603 and diceroll != 6 and (yy == 398 or yy == 300 or yy == 202 or yy == 104 or yy == 6):
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6:
                        yx = 162
                        yy = 251
                    elif yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                    elif yx == 211 and yy == 6:
                        yx = 162
                        yy = 251
                elif yx > 407 and yx <= 603 and diceroll == 6 and (yy == 398 or yy == 300 or yy == 202 or yy == 104 or yy == 6):
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6:
                        yx = 162
                        yy = 251
                    elif yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                    elif yx == 211 and yy == 6:
                        yx = 162
                        yy = 251
                    turn = 'yellow'
                elif yx == 407 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll != 6:
                    yx = yx - (49 * diceroll)
                    if yx == 358 and yy == 104:
                        yx = 260
                        yy = 202
                    elif yx == 211 and yy == 6:
                        yx = 162
                        yy = 251
                elif yx == 407 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 6:
                    yx = yx - (49 * 5)
                    yy = yy - 49
                    if yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                    turn = 'yellow'
                elif yx == 358 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll < 5:
                    yx = yx - (49 * diceroll)
                    if yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                elif yx == 358 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 5:
                    yx = yx - (49 * 4) + (49 * (diceroll - 5))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                elif yx == 358 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 6:
                    yx = yx - (49 * 4) + (49 * (diceroll - 5))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    turn = 'yellow'
                elif yx == 309 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll < 4:
                    yx = yx - (49 * diceroll)
                    if yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                elif yx == 309 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll >= 4 and diceroll != 6:
                    yx = yx - (49 * 3) + (49 * (diceroll - 4))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                elif yx == 309 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 6:
                    yx = yx - (49 * 3) + (49 * (diceroll - 4))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    turn = 'yellow'
                elif yx == 260 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll < 3:
                    yx = yx - (49 * diceroll)
                    if yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                elif yx == 260 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll >= 3 and diceroll != 6:
                    yx = yx - (49 * 2) + (49 * (diceroll - 3))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                elif yx == 260 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 6:
                    yx = yx - (49 * 2) + (49 * (diceroll - 3))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    turn = 'yellow'
                elif yx == 211 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll < 2:
                    yx = yx - (49 * diceroll)
                    if yx == 162 and yy == 300:
                        yx = 260
                        yy = 447
                elif yx == 211 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll != 6 and diceroll >= 2:
                    yx = yx - 49 + (49 * (diceroll - 2))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                elif yx == 211 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 6:
                    yx = yx - 49 + (49 * (diceroll - 2))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    turn = 'yellow'
                elif yx == 162 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll != 6:
                    yx = yx + (49 * (diceroll - 1))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    elif yx == 407 and yy == 153:
                        yx = 358
                        yy = 251
                elif yx == 162 and (yy == 398 or yy == 300 or yy == 202 or yy == 104) and diceroll == 6:
                    yx = yx + (49 * (diceroll - 1))
                    yy = yy - 49
                    if yx == 211 and yy == 251:
                        yx = 260
                        yy = 153
                    elif yx == 211 and yy == 153:
                        yx = 162
                        yy = 55
                    elif yx == 260 and yy == 251:
                        yx = 260
                        yy = 398
                    elif yx == 407 and yy == 153:
                        yx = 358
                        yy = 251
                    turn = 'yellow'
                # final row
                elif yy == 6 and (yx == 554 or yx == 603) and diceroll != 6:
                    yx = yx - (49 * diceroll)
                elif yy == 6 and (yx == 554 or yx == 603) and diceroll == 6:
                    yx = yx - (49 * diceroll)
                    turn = 'yellow'
                elif yy == 6 and yx == 456 and diceroll < 5:
                    yx = yx - (49 * diceroll)
                elif yy == 6 and yx == 456 and diceroll == 5:
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6 and diceroll == 5:
                        yx = 162
                        yy = 251
                elif yy == 6 and yx == 456 and diceroll == 6:
                    yx = yx
                elif yy == 6 and yx == 505 and diceroll != 6:
                    yx = yx - (49 * diceroll)
                elif yy == 6 and yx == 505 and diceroll == 6:
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6 and diceroll == 6:
                        yx = 162
                        yy = 251
                elif yy == 6 and yx == 407 and diceroll < 6:
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6 and diceroll == 4:
                        yx = 162
                        yy = 251
                elif yy == 6 and yx == 407 and yx >= 162 and diceroll == 6:
                    yx = yx
                elif yy == 6 and yx == 358 and yx >= 162 and diceroll >= 5:
                    yx = yx
                elif yy == 6 and yx == 358 and yx >= 162 and diceroll < 5:
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6 and diceroll == 3:
                        yx = 162
                        yy = 251
                elif yy == 6 and yx == 309 and yx >= 162 and diceroll >= 4:
                    yx = yx
                elif yy == 6 and yx == 309 and yx >= 162 and diceroll < 4:
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6 and diceroll == 2:
                        yx = 162
                        yy = 251
                elif yy == 6 and yx == 260 and yx >= 162 and diceroll >= 3:
                    yx = yx
                elif yy == 6 and yx == 260 and yx >= 162 and diceroll < 3:
                    yx = yx - (49 * diceroll)
                    if yx == 211 and yy == 6 and diceroll == 1:
                        yx = 162
                        yy = 251
                elif yy == 6 and yx == 211 and yx > 162 and diceroll >= 2:
                    yx = yx
    rplayer(rx, ry)
    bplayer(b1x, b1y)
    yplayer(yx,yy)
    pygame.display.update()
    if rx==162 and ry==6 :
        screen.fill((255, 0, 0))
        value = score_font.render("Red won", True, (0, 0, 0))
        screen.blit(value, [250, 200])
        print("RED WON")
        running = False
    if b1x==162 and b1y==9 :
        screen.fill((0, 0, 255)))
        value = score_font.render("Blue won", True, (0, 0, 255))
        screen.blit(value, [250, 200])
        print("BLUE WON")
        running = False
    if yx==162 and yy==6 :
        screen.fill((255, 255, 0))
        value = score_font.render("Yellow won", True, (255, 255, 0))
        screen.blit(value, [250, 200])
        print("YELLOW WON")
        running = False
    time.sleep(1.3)
pygame.display.update()
clock.tick(5)
pygame.quit()
quit()