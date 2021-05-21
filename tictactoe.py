import pygame 
from playsound import playsound 
pygame.init()
display=pygame.display.set_mode((1080,780))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
font=pygame.font.SysFont('Serif',90)
font2=pygame.font.SysFont('Serif',45)
rect1=pygame.Rect(300, 300, 100, 100)
rect2=pygame.Rect(400, 300, 100, 100)
rect3=pygame.Rect(500, 300, 100, 100)
rect4=pygame.Rect(300, 400, 100, 100)
rect5=pygame.Rect(400, 400, 100, 100)
rect6=pygame.Rect(500, 400, 100, 100)
rect7=pygame.Rect(300, 500, 100, 100)
rect8=pygame.Rect(400, 500, 100, 100)
rect9=pygame.Rect(500, 500, 100, 100)
rectturn=pygame.Rect(200, 620, 500, 300)
reset=pygame.Rect(750, 620, 150, 80)
pygame.draw.rect(display,green, reset)
def check(tic):
    for i in range(3):
        if len(set(tic[i]))==1:
            if tic[i][0]=="X":
                return 1 
            elif tic[i][0]=="O":
                return 2 
        if (tic[0][i] == tic[1][i]) and (tic[2][i] == tic[1][i]) :
            if tic[0][i] =="X":
                return 1 
            if tic[0][i] =="O":
                return 2 
    if tic[0][0]==tic[1][1] and tic[1][1]==tic[2][2]:
        if tic[0][0]=="X":
            return 1
        elif tic[0][0]=="O":
            return 2
    if tic[2][0]==tic[1][1] and tic[1][1]==tic[0][2]:
        if tic[1][1]=="X" :
            return 1
        elif tic[1][1]=="O" :
            return 2
    return 0
def player1turn(count):
    pygame.draw.rect(display, white, rectturn)
    display.blit(font2.render(person1+"'s Turn ", True,blue), (300,620))
    display.blit(font2.render(person1+": " +str(score1)+'   '+person2+": "+str(score2), True,red), (200,720))
    pygame.display.update(rectturn)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                            pygame.quit()
                            quit()  
        if event.type==pygame.MOUSEBUTTONDOWN:         
            if rect1.collidepoint(pygame.mouse.get_pos()) and tic[0][0]=="_":
                display.blit(font.render("X", True,red), (320,310))
                count[0]+=1
                tic[0][0]="X"
                return True
            elif rect2.collidepoint(pygame.mouse.get_pos()) and tic[0][1]=="_":
                display.blit(font.render("X", True,red), (420,310))
                count[0]+=1
                tic[0][1]="X"
                return True
            elif rect3.collidepoint(pygame.mouse.get_pos()) and tic[0][2]=="_":
                display.blit(font.render("X", True,red), (520,310))
                count[0]+=1
                tic[0][2]="X"
                return True
            elif rect4.collidepoint(pygame.mouse.get_pos()) and tic[1][0]=="_":
                display.blit(font.render("X", True,red), (320,410))
                count[0]+=1
                tic[1][0]="X"
                return True
            elif rect5.collidepoint(pygame.mouse.get_pos()) and tic[1][1]=="_":
                display.blit(font.render("X", True,red), (420,410))
                count[0]+=1
                tic[1][1]="X"
                return True
            elif rect6.collidepoint(pygame.mouse.get_pos()) and tic[1][2]=="_":
                display.blit(font.render("X", True,red), (520,410))
                count[0]+=1
                tic[1][2]="X"
                return True
            elif rect7.collidepoint(pygame.mouse.get_pos()) and tic[2][0]=="_":
                display.blit(font.render("X", True,red), (320,510))
                count[0]+=1
                tic[2][0]="X"
                return True
            elif rect8.collidepoint(pygame.mouse.get_pos())  and tic[2][1]=="_":
                display.blit(font.render("X", True,red), (420,510))
                count[0]+=1
                tic[2][1]="X"
                return True
            elif rect9.collidepoint(pygame.mouse.get_pos()) and tic[2][2]=="_":
                display.blit(font.render("X", True,red), (520,510))
                count[0]+=1
                tic[2][2]="X"
                return True
            elif reset.collidepoint(pygame.mouse.get_pos()):
                count[0]=10
                return False  
def player2turn(count):
    pygame.draw.rect(display, white, rectturn)
    display.blit(font2.render(person2+"'s Turn ", True,blue), (300,620))
    display.blit(font2.render(person1+": " +str(score1)+'   '+person2+": "+str(score2), True,red), (200,720))
    pygame.display.update(pygame.display.update(rectturn))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                            pygame.quit()
                            quit()
        if event.type==pygame.MOUSEBUTTONDOWN: 
            if rect1.collidepoint(pygame.mouse.get_pos()) and tic[0][0]=="_":
                display.blit(font.render("O", True,red), (320,310))
                count[0]+=1
                tic[0][0]="O"
                return True
            elif rect2.collidepoint(pygame.mouse.get_pos()) and tic[0][1]=="_":
                display.blit(font.render("O", True,red), (420,310))
                count[0]+=1
                tic[0][1]="O"
                return True
            elif rect3.collidepoint(pygame.mouse.get_pos()) and tic[0][2]=="_":
                display.blit(font.render("O", True,red), (520,310))
                count[0]+=1
                tic[0][2]="O"
                return True
            elif rect4.collidepoint(pygame.mouse.get_pos()) and tic[1][0]=="_":
                display.blit(font.render("O", True,red), (320,410))
                count[0]+=1
                tic[1][0]="O"
                return True
            elif rect5.collidepoint(pygame.mouse.get_pos()) and tic[1][1]=="_":
                display.blit(font.render("O", True,red), (420,410))
                count[0]+=1
                tic[1][1]="O"
                return True
            elif rect6.collidepoint(pygame.mouse.get_pos()) and tic[1][2]=="_":
                display.blit(font.render("O", True,red), (520,410))
                count[0]+=1
                tic[1][2]="O"
                return True
            elif rect7.collidepoint(pygame.mouse.get_pos()) and tic[2][0]=="_":
                display.blit(font.render("O", True,red), (320,510))
                count[0]+=1
                tic[2][0]="O"
                return True
            elif rect8.collidepoint(pygame.mouse.get_pos()) and tic[2][1]=="_":
                display.blit(font.render("O", True,red), (420,510))
                count[0]+=1
                tic[2][1]="O"
                return True
            elif rect9.collidepoint(pygame.mouse.get_pos()) and tic[2][2]=="_":
                display.blit(font.render("O", True,red), (520,510))
                count[0]+=1
                tic[2][2]="O"
                return True
            elif reset.collidepoint(pygame.mouse.get_pos()):
                count[0]=10
                return False
while True:
    display.fill(white)
    pygame.display.update()
    score1=0
    score2=0
    p1=""
    p2=""
    person1=""
    person2=""
    name1=True
    while name1:
        for ele in pygame.event.get():
            if ele.type==pygame.QUIT:
                            pygame.quit()
                            quit()
            if ele.type==pygame.KEYDOWN:
                if ele.key==pygame.K_BACKSPACE:
                    display.fill(white)
                    pygame.display.update()
                    p1=p1[:-1]
                elif ele.key==pygame.K_RETURN:
                    if len(p1)>0:
                        person1=p1
                        name1=False
                        break                       
                    else:
                        display.fill(white)
                        display.blit(font.render("invalid entry.Try Again", True, red),(200,200))
                        pygame.display.update()
                        p1=""
                else:
                    p1+=ele.unicode
        display.blit(font2.render("name of person 1:-->  "+p1, True, black),(200,300))
        pygame.display.update()
    name2=True
    display.fill(white)
    pygame.display.update()
    while name2:
        for ele in pygame.event.get():
            if ele.type==pygame.QUIT:
                            pygame.quit()
                            quit()
            if ele.type==pygame.KEYDOWN:
                if ele.key==pygame.K_BACKSPACE:
                    display.fill(white)
                    pygame.display.update()
                    p2=p2[:-1]
                elif ele.key==pygame.K_RETURN:
                    if len(p2)>0:
                        person2=p2
                        name2=False
                        break  
                    else:
                        display.fill(white)
                        display.blit(font.render("invalid entry.Try Again", True, red),(200,200))
                        pygame.display.update()
                        p2=""
                else:
                    p2+=ele.unicode
        display.blit(font2.render("name of person 2:-->  "+p2, True, black),(200,300))
        pygame.display.flip()
    playsound("theme.wav",False)
    newgame=True
    while newgame:
        count=[0]
        tic=[["_","_","_"],["_","_","_"],["_","_","_"]]
        display.fill(white)
        display.blit(font.render("TIC-TAC-TOE", True, green), (200,150))
        pygame.display.update()
        pygame.time.wait(1000)
        for el in pygame.event.get():
                        if el.type==pygame.QUIT:
                            pygame.quit()
                            quit()
        pygame.draw.line(display,black,(400,300), (400,600),5)
        pygame.display.update()
        pygame.time.wait(500)
        pygame.draw.line(display,black,(500,300), (500,600),5)
        pygame.display.update()
        pygame.time.wait(500)
        pygame.draw.line(display,black,(300,500), (600,500),5)
        pygame.display.update()
        pygame.time.wait(500)
        pygame.draw.line(display,black,(300,400), (600,400),5)
        pygame.display.update()
        pygame.time.wait(500)
        endgame=False
        p2marked=False
        p1marked=True
        while not endgame and count[0]<=9:
            display.blit(font2.render("Reset", True,green), (755,620))
            pygame.display.update()
            if  p1marked:
                p2marked=player1turn(count)
                pygame.display.update()
                if check(tic)!=0:
                    if check(tic)==1:
                        score1+=1
                        display.blit(font2.render("RESULT-----> "+person1+" has WON this round", True,green), (200,50))
                        pygame.display.update()
                        pygame.time.wait(2*1000)
                    elif check(tic)==2:
                        score2+=1
                        display.blit(font2.render("RESULT-----> "+person2+" has WON this round", True,green), (200,50))
                        pygame.display.update()
                        pygame.time.wait(2*1000)
                    endgame=True
                    break
            if count[0]==9:
                display.blit(font2.render("RESULT-----> DRAW", True,green), (200,50))
                pygame.display.update()
                pygame.time.wait(2*1000)
                count[0]=10
                break
            
            if  p2marked and count[0]<=9:
                p1marked=player2turn(count)
                pygame.display.update()
                if check(tic)!=0:
                    if check(tic)==1:
                        score1+=1
                        display.blit(font2.render("RESULT-----> "+person1+" has WON this round", True,green), (200,50))
                        pygame.display.update()
                        pygame.time.wait(2*1000)
                    elif check(tic)==2:
                        score2+=1
                        display.blit(font2.render("RESULT-----> "+person2+" has WON this round", True,green), (200,50))
                        pygame.display.update()
                        pygame.time.wait(2*1000)
                    endgame=True