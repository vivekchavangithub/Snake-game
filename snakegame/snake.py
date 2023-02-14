import pygame
import random
pygame.init()
pygame.mixer.init()

#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
purple=(160,32,240)

#creating Game window
screen_width=900
screen_hight=500
game_window=pygame.display.set_mode((screen_width,screen_hight))
# Food_window=pygame.display.set_mode((900,400))

#Background image
bgimg=pygame.image.load("start.jpg")
bgimg=pygame.transform.scale(bgimg,(screen_width,screen_hight)).convert_alpha()

bgimg1=pygame.image.load("middle.jpg")
bgimg1=pygame.transform.scale(bgimg1,(screen_width,screen_hight)).convert_alpha()

bgimg2=pygame.image.load("end.jpg")
bgimg2=pygame.transform.scale(bgimg2,(screen_width,screen_hight)).convert_alpha()

#game title
Title=pygame.display.set_caption("Snake Game")
pygame.display.update()

#screen score text
def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

#length increse snake
def plot_snake(game_window,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)

def homeloop():
    exit_game=False
    fps=30
    game_window.fill((233,221,78))
    game_window.blit(bgimg,(0,0))
    # text_screen("Welcome to Snake game!!",red,180,200)
    # text_screen("Press Space To Start!",red,200,250)
    
    while not exit_game:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
                
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    gameloop()            

        pygame.display.update()
        clock.tick(fps)            

    pygame.quit()
    quit()
    
#game loop
def gameloop():

    #variable
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0
    init_velocity=5
    snake_size=20
    food_size=15
    score=0
    snk_list=[]
    snk_length=1 
    with open("hiscore.txt","r") as f:
        Hiscore=f.read()

    food_x=random.randint(20,screen_width/2)
    food_y=random.randint(20,400/2)
    fps=30

    while not exit_game:
        #for game over condition
        if game_over:
            with open("hiscore.txt","w") as f:
                f.write(str(Hiscore))
            game_window.fill((189,154,122))
            # text_screen("Game Over!Press Enter to continue",red,100,200)
            game_window.blit(bgimg2,(0,0))
            text_screen(str(score),black,470,364)
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        homeloop()
                        

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x= init_velocity
                        velocity_y= 0
                
                    if event.key==pygame.K_LEFT:
                        velocity_x= - init_velocity
                        velocity_y= 0
                    
                    if event.key==pygame.K_UP:
                        velocity_y= - init_velocity
                        velocity_x= 0
                    
                    if event.key==pygame.K_DOWN:
                        velocity_y= init_velocity
                        velocity_x= 0
            
            snake_x= snake_x + velocity_x
            snake_y= snake_y + velocity_y
            #score and food position after eat food
            if abs(snake_x - food_x)<10 and abs(snake_y-food_y)<10:
                score +=10
                # print("score: ",score)
                food_x=random.randint(40,screen_width/2)
                food_y=random.randint(40,screen_hight/2)
                snk_length +=5
                if score>int(Hiscore):
                    Hiscore=score


            #game start from the point
            game_window.fill((0,128,0))
            game_window.blit(bgimg1,(0,0))
            text_screen("score: "+str(score)+"  Hiscore: "+str(Hiscore),purple,5,5)
            pygame.draw.rect(game_window,red,[food_x,food_y,food_size,food_size])

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over=True
                    
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_hight:
                game_over=True

            # pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(game_window,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)            

    pygame.quit()
    quit()

# gameloop()
homeloop()