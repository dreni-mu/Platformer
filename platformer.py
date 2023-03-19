#platformer test
import pygame

pygame.init()

#display window
dis_width=500 #500
dis_height=500 #500
player_width=20
player_height=35
dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption('Platform game (WIP)') #title of window

white = (255, 255, 255)
black = (0, 0, 0)
orange = (241, 188, 126)
blue = (108, 218, 242)
grey = (155, 155, 155)

floor_y=470


#====================================
def draw_player(x_pos,y_pos,player_width,player_height):
    dis.fill(grey)
    #pygame.draw.line(dis,orange,(0,floor_y),(dis_width,floor_y))
    pygame.draw.rect(dis,orange,[0, floor_y, 500, 10])
    pygame.draw.rect(dis,blue,[x_pos,y_pos,player_width,player_height])
#====================================





#main gameloop
run=True
x_pos=250
y_pos=50
x_vel=0 #implement me later :(
y_vel=0
a=-9.81
t=0.0035 #0.003 === #edit to change the acceleration rate

pressed_left=False
pressed_right=False

#coyote time
coyote=False
coyoteCount=0

#change these 2 values to change jump height and move speed
jump_vel=70 #40
horiz_vel=0.1

while run==True:
    draw_player(x_pos,y_pos,player_width,player_height)
    pygame.display.update()
    
    #calculate next position of player
    y_vel+=a*t
    print(y_vel)
    y_pos-=y_vel*t
    if y_pos >= floor_y-35:
        y_pos=floor_y-35
        y_vel=0
    
    #calculate coyot time so jumps feel better !
    #print(coyoteCount)
    if coyoteCount == 0:
        coyote=False
    else:
        coyoteCount-=1
        if y_pos == floor_y-35:
            y_vel=jump_vel
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
        if event.type == pygame.KEYDOWN:
            if y_pos == floor_y-35:
                if (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                    y_vel=jump_vel
            else:
                if (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                    coyote=True
                    coyoteCount=400 #200 is deecent  (#EDIT FOR TESTING)
            
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pressed_left=True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pressed_right=True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                pressed_left=False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                pressed_right=False
    
    if pressed_left==True:
        x_pos-=horiz_vel
    if pressed_right==True:
        x_pos+=horiz_vel
    
    #dont cross the left and right borders
    if x_pos <= 0:
        x_pos = 0
    if x_pos >= dis_width-player_width:
        x_pos = dis_width-player_width
#exit
pygame.quit()