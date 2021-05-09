import pygame
import time
import random
pygame.init()
gray=(119,118,110)
black=(0,0,0)
pygame.mixer.music.load('olurum-turkiyem.wav')

display_width=800
display_height=600
gamedisplays=pygame.display.set_mode((display_width,display_height)) 
pygame.display.set_caption("Car Race")
clock=pygame.time.Clock()
car_image=pygame.image.load('indir.jpg')
backgroundpic=pygame.image.load('maske.jpg')
yellow_strip=pygame.image.load('yellow strip.jpg')
strip=pygame.image.load('siyah_cizgi.jpg')
car_width=79

'''def background():
    gamedisplays.blit(backgroundpic,(0,0))
    gamedisplays.blit(backgroundpic,(0,312))
    gamedisplays.blit(backgroundpic,(0,468))
    gamedisplays.blit(backgroundpic,(0,156))
    gamedisplays.blit(backgroundpic,(730,0))
    gamedisplays.blit(backgroundpic,(730,312))
    gamedisplays.blit(backgroundpic,(730,468))
    gamedisplays.blit(backgroundpic,(730,156))
    gamedisplays.blit(yellow_strip,(400,0))
    gamedisplays.blit(yellow_strip,(400,100))
    gamedisplays.blit(yellow_strip,(400,200))
    gamedisplays.blit(yellow_strip,(400,300))
    gamedisplays.blit(yellow_strip,(400,400))
    gamedisplays.blit(yellow_strip,(400,500))
    gamedisplays.blit(strip,(80,198))
    gamedisplays.blit(strip,(80,396))
    gamedisplays.blit(strip,(80,0))
    gamedisplays.blit(strip,(705,198))
    gamedisplays.blit(strip,(705,396))
    gamedisplays.blit(strip,(705,0))'''
def text_objects(text,font):
    textsurface=font.render(text,True,black)
    return textsurface,textsurface.get_rect()

def message_display(text):
    largetext=pygame.font.Font("freesansbold.ttf",80)
    textsurf,textrect=text_objects(text,largetext)
    textrect.center=((display_width/2),(100))
    gamedisplays.blit(textsurf,textrect)
    pygame.display.update()
    time.sleep(3) # after crahs you need to wait 3 seconds
    game_loop()

def obstacle(obs_startx,obs_starty,obs):
    if obs==0:
        obs_pic=pygame.image.load('Bayrak3.jpg')
    elif obs==1:
        obs_pic=pygame.image.load('Bayrak2.jpg')
    elif obs==2:
        obs_pic=pygame.image.load('Bayrak1.jpg')
    elif obs==3:
        obs_pic=pygame.image.load('Bayrak4.jpg')
    elif obs==4:
        obs_pic=pygame.image.load('Bayrak5.jpg')
    elif obs==5:
        obs_pic=pygame.image.load('Bayrak6.jpg')
    elif obs==6:
        obs_pic=pygame.image.load('Bayrak7.jpg')
    gamedisplays.blit(obs_pic,(obs_startx,obs_starty))
def crash():
        message_display('You Crashed')
def car(x,y):
    gamedisplays.blit(car_image,(x,y))
    
def game_loop():
    x=(display_width*0.39)
    y=(display_height*0.8)
    x_change=0
    obstacle_speed=9
    obs=0
   # y_change=0
    obs_startx=random.randrange(100,630)
    obs_starty=-750
    obs_width=79
    obs_height=108
    y2=7

    
    bumped=False
    while not bumped :#True
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        if event.type==pygame.KEYDOWN: # if you press the key
            if event.key==pygame.K_a:
                obstacle_speed=15
            if event.key==pygame.K_b:
                obstacle_speed=3
            if event.key==pygame.K_LEFT:
                x_change=-5
            if event.key==pygame.K_RIGHT:
                x_change=5
        if event.type==pygame.KEYUP: # if you are not pressing anymore
         #   if event.key==pygame.K_LEFT:
          #      x_change=-5
           # if event.key==pygame.K_RIGHT:
            #    x_change=5
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT :
                x_change=0
        
        x = x + x_change
        gamedisplays.fill(gray)
        rel_y=y2%backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic,(730,rel_y-backgroundpic.get_rect().width))
        if rel_y<800:
            gamedisplays.blit(backgroundpic,(0,rel_y))
            gamedisplays.blit(backgroundpic,(0,rel_y+300))
            gamedisplays.blit(backgroundpic,(0,rel_y+450))
            gamedisplays.blit(backgroundpic,(0,rel_y+150))
            gamedisplays.blit(backgroundpic,(730,rel_y))
            gamedisplays.blit(backgroundpic,(730,rel_y+300))
            gamedisplays.blit(backgroundpic,(730,rel_y+450))
            gamedisplays.blit(backgroundpic,(730,rel_y+150))
            gamedisplays.blit(yellow_strip,(400,rel_y))
            gamedisplays.blit(yellow_strip,(400,rel_y+100))
            gamedisplays.blit(yellow_strip,(400,rel_y+200))
            gamedisplays.blit(yellow_strip,(400,rel_y+300))
            gamedisplays.blit(yellow_strip,(400,rel_y+400))
            gamedisplays.blit(yellow_strip,(400,rel_y+500))
            gamedisplays.blit(yellow_strip,(400,rel_y-100))
            gamedisplays.blit(strip,(80,rel_y+198))
            gamedisplays.blit(strip,(80,rel_y+396))
            gamedisplays.blit(strip,(80,rel_y))
            gamedisplays.blit(strip,(705,rel_y+198))
            gamedisplays.blit(strip,(705,rel_y+396))
            gamedisplays.blit(strip,(705,rel_y))
        y2+=obstacle_speed   
        gamedisplays.blit(backgroundpic,(0,rel_y-backgroundpic.get_rect().width))
        #background()
        obs_starty-=(obstacle_speed/4)
        obstacle(obs_startx,obs_starty,obs)
        obs_starty= obs_starty+obstacle_speed
        car(x,y)
        if x>705-car_width or x<90:
            crash()
        if obs_starty>display_height:
            obs_starty=0-obs_height
            obs_startx=random.randrange(100,(display_width-179))
            obs=random.randrange(0,7) 
            if obs==5:
                pygame.mixer.music.play(-1)
                obstacle_speed=4
            if obs!=5:
                pygame.mixer.music.stop()
                obstacle_speed=9
                
        if y<obs_starty+obs_height:
            if x>obs_startx and x < obs_startx + obs_width or x+car_width > obs_startx and x+car_width < obs_startx+obs_width:
                crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()