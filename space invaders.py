import pygame 
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((300, 500))
pygame.display.set_caption("Space Invaders")

player_x = 145
player_y = 440
player_width = 10
player_height = 20
player_vel = 10

laser_x = player_x + 5
laser_y = player_y
laser_width = 5
laser_height = 10
laser_vel = 100
button_down = False
score = 0

class Opponent:
  def __init__(self, x, y, width, height, vel):
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.vel = vel 

  def CreateMovementOpponent(self):
    pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
    pygame.display.update()
    
    

opponent_x = 20
opponent_y = 50
opponent_width = 20
opponent_height = 5
opponent_vel = 5
switch = 1
down = 0

o1 = Opponent(10, 30, opponent_width, opponent_height, opponent_vel)
o2 = Opponent(62, 30, opponent_width, opponent_height, opponent_vel)
o3 = Opponent(114, 30, opponent_width, opponent_height, opponent_vel)
o4 = Opponent(166, 30, opponent_width, opponent_height, opponent_vel)
o5 = Opponent(218, 30, opponent_width, opponent_height, opponent_vel)
o6 = Opponent(270, 30, opponent_width, opponent_height, opponent_vel)

o7 = Opponent(10, 50, opponent_width, opponent_height, opponent_vel)
o8 = Opponent(62, 50, opponent_width, opponent_height, opponent_vel)
o9 = Opponent(114, 50, opponent_width, opponent_height, opponent_vel)
o10 = Opponent(166, 50, opponent_width, opponent_height, opponent_vel)
o11 = Opponent(218, 50, opponent_width, opponent_height, opponent_vel)
o12 = Opponent(270, 50, opponent_width, opponent_height, opponent_vel)

o13 = Opponent(10, 70, opponent_width, opponent_height, opponent_vel)
o14 = Opponent(62, 70, opponent_width, opponent_height, opponent_vel)
o15 = Opponent(114, 70, opponent_width, opponent_height, opponent_vel)
o16 = Opponent(166, 70, opponent_width, opponent_height, opponent_vel)
o17 = Opponent(218, 70, opponent_width, opponent_height, opponent_vel)
o18 = Opponent(270, 70, opponent_width, opponent_height, opponent_vel)

o19 = Opponent(10, 90, opponent_width, opponent_height, opponent_vel)
o20 = Opponent(62, 90, opponent_width, opponent_height, opponent_vel)
o21 = Opponent(114, 90, opponent_width, opponent_height, opponent_vel)
o22 = Opponent(166, 90, opponent_width, opponent_height, opponent_vel)
o23 = Opponent(218, 90, opponent_width, opponent_height, opponent_vel)
o24 = Opponent(270, 90, opponent_width, opponent_height, opponent_vel)

o25 = Opponent(10, 110, opponent_width, opponent_height, opponent_vel)
o26 = Opponent(62, 110, opponent_width, opponent_height, opponent_vel)
o27 = Opponent(114, 110, opponent_width, opponent_height, opponent_vel)
o28 = Opponent(166, 110, opponent_width, opponent_height, opponent_vel)
o29 = Opponent(218, 110, opponent_width, opponent_height, opponent_vel)
o30 = Opponent(270, 110, opponent_width, opponent_height, opponent_vel)

def OpponentMoveRight():
    o1.x += 5
    o2.x += 5
    o3.x += 5
    o4.x += 5
    o5.x += 5
    o6.x += 5
    o7.x += 5
    o8.x += 5
    o9.x += 5
    o10.x += 5
    o11.x += 5
    o12.x += 5
    o13.x += 5
    o14.x += 5
    o15.x += 5
    o16.x += 5
    o17.x += 5
    o18.x += 5
    o19.x += 5
    o20.x += 5
    o21.x += 5
    o22.x += 5
    o23.x += 5
    o24.x += 5
    o25.x += 5
    o26.x += 5
    o27.x += 5
    o28.x += 5
    o29.x += 5
    o30.x += 5

def OpponentMoveLeft():
    o1.x -= 5
    o2.x -= 5
    o3.x -= 5
    o4.x -= 5
    o5.x -= 5
    o6.x -= 5
    o7.x -= 5
    o8.x -= 5
    o9.x -= 5
    o10.x -= 5
    o11.x -= 5
    o12.x -= 5
    o13.x -= 5
    o14.x -= 5
    o15.x -= 5
    o16.x -= 5
    o17.x -= 5
    o18.x -= 5
    o19.x -= 5
    o20.x -= 5
    o21.x -= 5
    o22.x -= 5
    o23.x -= 5
    o24.x -= 5
    o25.x -= 5
    o26.x -= 5
    o27.x -= 5
    o28.x -= 5
    o29.x -= 5
    o30.x -= 5
    
def OpponentMoveDown():
    o1.y += 5
    o2.y += 5
    o3.y += 5
    o4.y += 5
    o5.y += 5
    o6.y += 5
    o7.y += 5
    o8.y += 5
    o9.y += 5
    o10.y += 5
    o11.y += 5
    o12.y += 5
    o13.y += 5
    o14.y += 5
    o15.y += 5
    o16.y += 5
    o17.y += 5
    o18.y += 5
    o19.y += 5
    o20.y += 5
    o21.y += 5
    o22.y += 5
    o23.y += 5
    o24.y += 5
    o25.y += 5
    o26.y += 5
    o27.y += 5
    o28.y += 5
    o29.y += 5
    o30.y += 5
    
font = pygame.font.SysFont("comicsans", 24, True)
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get ():
        if event.type == pygame.QUIT:
            run = False
    
    if(player_y<=o30.y or player_y<=o29.y or player_y<=o28.y or player_y<=o27.y or player_y<=o26.y or player_y<=o25.y or player_y<=o24.y or player_y<=o23.y or player_y<=o22.y or player_y<=o21.y or player_y<=o20.y or player_y<=o19.y or player_y<=o18.y or player_y<=o17.y or player_y<=o16.y or player_y<=o15.y or player_y<=o14.y or player_y<=o13.y or player_y<=o12.y or player_y<=o11.y or player_y<=o10.y or player_y<=o9.y or player_y<=o8.y or player_y<=o7.y or player_y<=o6.y or player_y<=o5.y or player_y<=o4.y or player_y<=o3.y or player_y<=o2.y or player_y<=o1.y):
        run = False
        print("Game Over")
        print("Your Score was " + str(score))
    
    if(o1.y<=0 and o2.y<=0 and o3.y<=0 and o4.y<=0 and o5.y<=0 and o6.y<=0):
        run = False
        print("You win with " + str(score) + " points. ")
    
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and player_x>10:
        player_x -= player_vel
        if(button_down == False):
            laser_x = player_x + 5

    if keys[pygame.K_d] and player_x<280:
        player_x += player_vel
        if(button_down == False):
            laser_x = player_x + 5

    if keys[pygame.K_w] and player_y>10:
        player_y -= player_vel
        if(button_down == False):
            laser_y = player_y
        
    if keys[pygame.K_s] and player_y<470:
        player_y += player_vel
        if(button_down == False):
            laser_y = player_y
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        button_down = True
    if(button_down == True):
        if(laser_y <= 10):
            button_down == False
            laser_y = player_y
            laser_x = player_x
            button_down = False
        else:
            laser_y -= laser_vel
            
    
    
    
    screen.fill((0, 0, 0))
    text = font.render("Score: " + str(score), 1, (255, 255, 255))
    screen.blit(text, (125, 10))
    
    o1.CreateMovementOpponent()
    o2.CreateMovementOpponent()
    o3.CreateMovementOpponent()
    o4.CreateMovementOpponent()
    o5.CreateMovementOpponent()
    o6.CreateMovementOpponent()
    o7.CreateMovementOpponent()
    o8.CreateMovementOpponent()
    o9.CreateMovementOpponent()
    o10.CreateMovementOpponent()
    o11.CreateMovementOpponent()
    o12.CreateMovementOpponent()
    o13.CreateMovementOpponent()
    o14.CreateMovementOpponent()
    o15.CreateMovementOpponent()
    o16.CreateMovementOpponent()
    o17.CreateMovementOpponent()
    o18.CreateMovementOpponent()
    o19.CreateMovementOpponent()
    o20.CreateMovementOpponent()
    o21.CreateMovementOpponent()
    o22.CreateMovementOpponent()
    o23.CreateMovementOpponent()
    o24.CreateMovementOpponent()
    o25.CreateMovementOpponent()
    o26.CreateMovementOpponent()
    o27.CreateMovementOpponent()
    o28.CreateMovementOpponent()
    o29.CreateMovementOpponent()
    o30.CreateMovementOpponent()
    
    if(o6.x>=280):
        switch = 2
        down = 1
    elif(o6.x<=260):
        switch = 1
        down = 1
    else:
        down = 0
    
    if(switch==2):
        OpponentMoveLeft()
    elif(switch==1):
        OpponentMoveRight()
    if(down==1):
        OpponentMoveDown()
    
    if(laser_y!=player_y):
        if(laser_y<=o30.y or laser_y<= o29.y or laser_y<= o28.y or laser_y<= o27.y or laser_y<= o26.y or laser_y<= o25.y):
            if(laser_x >= 0 and laser_x <= 40):
                o25.y = -1000
                score+=1
            elif(laser_x >= 52 and laser_x <= 92):
                o26.y = -1000
                score+=1
            elif(laser_x >= 104 and laser_x <= 144):
                o27.y = -1000
                score+=1
            elif(laser_x >= 156 and laser_x <= 196):
                o28.y = -1000
                score+=1
            elif(laser_x >= 208 and laser_x <= 248):
                o29.y = -1000
                score+=1
            elif(laser_x >= 260 and laser_x <= 300):
                o30.y = -1000
                score+=1
            else:
                button_down == False
                laser_y = player_y
                laser_x = player_x
                button_down = False
                
        elif(laser_y<=o24.y or laser_y<= o23.y or laser_y<= o22.y or laser_y<= o21.y or laser_y<= o20.y or laser_y<= o19.y):
            if(laser_x >= 0 and laser_x <= 40):
                o19.y = -1000
                score+=1
            elif(laser_x >= 52 and laser_x <= 92):
                o20.y = -1000
                score+=1
            elif(laser_x >= 104 and laser_x <= 144):
                o21.y = -1000
                score+=1
            elif(laser_x >= 156 and laser_x <= 196):
                o22.y = -1000
                score+=1
            elif(laser_x >= 208 and laser_x <= 248):
                o23.y = -1000
                score+=1
            elif(laser_x >= 260 and laser_x <= 300):
                o24.y = -1000
                score+=1
            else:
                button_down == False
                laser_y = player_y
                laser_x = player_x
                button_down = False
        
        elif(laser_y<=o18.y or laser_y<= o17.y or laser_y<= o16.y or laser_y<= o15.y or laser_y<= o14.y or laser_y<= o13.y):
            if(laser_x >= 0 and laser_x <= 40):
                o13.y = -1000
                score+=1
            elif(laser_x >= 52 and laser_x <= 92):
                o14.y = -1000
                score+=1
            elif(laser_x >= 104 and laser_x <= 144):
                o15.y = -1000
                score+=1
            elif(laser_x >= 156 and laser_x <= 196):
                o16.y = -1000
                score+=1
            elif(laser_x >= 208 and laser_x <= 248):
                o17.y = -1000
                score+=1
            elif(laser_x >= 260 and laser_x <= 300):
                o18.y = -1000
                score+=1
            else:
                button_down == False
                laser_y = player_y
                laser_x = player_x
                button_down = False
                
        elif(laser_y<=o12.y or laser_y<= o11.y or laser_y<= o10.y or laser_y<= o9.y or laser_y<= o8.y or laser_y<= o7.y):
            if(laser_x >= 0 and laser_x <= 40):
                o7.y = -1000
                score+=1
            elif(laser_x >= 52 and laser_x <= 92):
                o8.y = -1000
                score+=1
            elif(laser_x >= 104 and laser_x <= 144):
                o9.y = -1000
                score+=1
            elif(laser_x >= 156 and laser_x <= 196):
                o10.y = -1000
                score+=1
            elif(laser_x >= 208 and laser_x <= 248):
                o11.y = -1000
                score+=1
            elif(laser_x >= 260 and laser_x <= 300):
                o12.y = -1000
                score+=1
            else:
                button_down == False
                laser_y = player_y
                laser_x = player_x
                button_down = False
                
        elif(laser_y<=o6.y or laser_y<= o5.y or laser_y<= o4.y or laser_y<= o3.y or laser_y<= o2.y or laser_y<= o1.y):
            if(laser_x >= 0 and laser_x <= 40):
                o1.y = -1000
                score+=1
            elif(laser_x >= 52 and laser_x <= 92):
                o2.y = -1000
                score+=1
            elif(laser_x >= 104 and laser_x <= 144):
                o3.y = -1000
                score+=1
            elif(laser_x >= 156 and laser_x <= 196):
                o4.y = -1000
                score+=1
            elif(laser_x >= 208 and laser_x <= 248):
                o5.y = -1000
                score+=1
            elif(laser_x >= 260 and laser_x <= 300):
                o6.y = -1000
                score+=1
            else:
                button_down == False
                laser_y = player_y
                laser_x = player_x
                button_down = False
        
        
        

    pygame.draw.rect(screen, (31, 161, 204), (player_x, player_y, player_width, player_height))
    pygame.display.update()
    pygame.draw.rect(screen, (219, 29, 0), (laser_x, laser_y, laser_width, laser_height))
    pygame.display.update()


pygame.quit()