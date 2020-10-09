
import pygame
import random

pygame.init()

display_width = 600
display_hight = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
purple = (128,0,128)
yellow = (255,255,0)
grey_light = (187,187,187)
grey_dark = (170,170,170)
green = (128,255,0)
fade = pygame.color

toggle_up = False
toggle_down = False
toggle_left = False
toggle_right = False
toggle_space = False


gameDisplay = pygame.display.set_mode((display_width,display_hight))
pygame.display.set_caption('KILL THE PIZZA')
clock = pygame.time.Clock()

dudeGreen = pygame.transform.scale(pygame.image.load('the green dude.png'), (100,100))
fire_ball = pygame.transform.scale(pygame.image.load('pappers.png'), (100,100))
enemy_pizza = pygame.transform.scale(pygame.image.load('angryPizza.png'), (100,100))

def set_dude_position(x,y):
    gameDisplay.blit(dudeGreen,(x,y))


enemys = [];
bullets = [];

enemy_death_counter = 0

my_font = pygame.font.SysFont("Arial",25,bold = True)
enemy_death_counter_x = 10
enemy_death_counter_y = 560

def death_of_pizza_enemy (x,y):
    text_one = my_font.render("SCORE = " + str(enemy_death_counter),True, yellow)
    gameDisplay.blit(text_one,(x,y))

def end_of_game (x,y):
    text_two = my_font.render("YOU DIED", True, red)
    gameDisplay.blit(text_two,(x,y))
def restart_game (x,y):
    text_three = my_font.render("Press A to restart", True, purple)
    gameDisplay.blit(text_three,(x,y))
def set_enemy_position (x,y):
    enemys.append([x,y])

def draw_enemys():
    global enemy_death_counter
    global damaged
    global damage_timer
    global damage_timeout
    global damage_timeout_status
    global health
    global health_status
    
    for enemy in enemys:

        if enemy[0] > character_x - 50 and enemy[0] < character_x + 50 and enemy[1] < character_y + 50 and enemy[1] > character_y - 50:
            damaged = True 
            damage_timeout = pygame.time.get_ticks()  
            damage_timeout_status = False
            

        for bullet in bullets:

            if enemy[0] > bullet[0] - 50 and enemy[0] < bullet[0] + 50 and enemy[1] < bullet[1] + 50 and enemy[1] > bullet[1] - 50:
                enemys.remove(enemy)
                bullets.remove(bullet)
                enemy_death_counter += 1

        gameDisplay.blit(enemy_pizza, enemy)
        enemy[1] = enemy[1] + 3

        if enemy[1] > display_hight:
            enemys.remove(enemy)
            #enemy_death_counter -= 10
            if health_status > 0:
                health += 37
                health_status -= 1
    
is_faded = False
def fade(width, height): 
    global is_faded
    is_faded = True
    fade = pygame.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        redrawWindow()
        gameDisplay.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(5)
       

def redrawWindow ():
    gameDisplay.fill (black)
    set_dude_position(character_x,character_y)
    draw_bullets()
    draw_enemys()
    pygame.draw.rect(gameDisplay,green,(0,550,600,50))
    pygame.draw.rect(gameDisplay,purple,(10,562.5,150,25))
    pygame.draw.rect(gameDisplay,white,(387.5,562.5,200,25))
    pygame.draw.rect(gameDisplay,green,(392.5,567.5,190,15))
    pygame.draw.rect(gameDisplay,red,(395 + health,570,185 - health,10))
    death_of_pizza_enemy(enemy_death_counter_x, enemy_death_counter_y)


# Add bulet to bullets array
def add_bullet(x,y):
    bullets.append([x,y])

# Draw Each bullet in bullets arrray
def draw_bullets():
    for bullet in bullets:
        gameDisplay.blit (fire_ball, bullet)
        bullet[1] = bullet[1] - 10
        if bullet[1] < -200:
            bullets.remove (bullet)


enemy_time = pygame.time.get_ticks()    

character_x = ((display_width * 0.5) - 50)
character_y = ((display_hight) - 150)

enemy_x = (random.randint(0,display_width-100))
enemy_y = (-100)

enemy_flow = 350

health = 0
health_status = 5
toggle_health_regen = False
damaged = False
damage_timer = 0
damage_timer_status = False
damage_timeout = 0
damage_timeout_status = False

crashed = False

while not crashed:


    #print(pygame.time.get_ticks())


    if health_status <= 0 and event.type == pygame.KEYDOWN: 
        fade (600,600)
        

    if damaged == True and damage_timer_status == False and health_status > 0 and damage_timeout_status == False:
        health_status -= 1
        health += 37
        print("hit")
        damage_timer = pygame.time.get_ticks() 
        damaged = False
        damage_timer_status = True

    if damage_timer_status == True and damage_timer < pygame.time.get_ticks() - 1000:
        damage_timer_status = False

    if damage_timeout < pygame.time.get_ticks() - 2000 and damage_timeout_status == False:
        damage_timeout_status = True

    if pygame.time.get_ticks() > enemy_time + enemy_flow and health_status > 0:
        if enemy_flow > 250:
            enemy_flow = enemy_flow - 5
            print(enemy_flow)
        set_enemy_position(enemy_x,enemy_y)
        enemy_time = pygame.time.get_ticks()
        enemy_x = (random.randint(0,display_width-100))

    for event in pygame.event.get():
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and is_faded:
                is_faded = False
                health_status = 5
                health = 0
                enemy_death_counter = 0
                enemy_flow = 350
                character_x = ((display_width * 0.5) - 50)
                character_y = ((display_hight) - 150)
            if health_status > 0:
                if event.key == pygame.K_SPACE:
                    toggle_space = True
                    add_bullet(character_x,character_y)
                if event.key == pygame.K_RIGHT:
                    toggle_right = True
                if event.key == pygame.K_DOWN:
                    toggle_down = True
                if event.key == pygame.K_LEFT:
                    toggle_left = True
                if event.key == pygame.K_UP:
                    toggle_up = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                toggle_space = False
            if event.key == pygame.K_RIGHT:
                toggle_right = False
            if event.key == pygame.K_DOWN:
                toggle_down = False
            if event.key == pygame.K_LEFT:
                toggle_left = False
            if event.key == pygame.K_UP:
                toggle_up = False

        if event.type == pygame.QUIT:
            crashed = True
            

   # if toggle_space:
   #     print ("space toggled lol")
    if toggle_up and character_y > 0:
        character_y -= 8

    if toggle_down and character_y < display_width - 150:
        character_y += 8

    if toggle_left and character_x > 0:
        character_x -= 8
    
    if toggle_right and character_x < display_width - 100:
        character_x += 8

    if not is_faded:
        redrawWindow()
    if is_faded:
        end_of_game(255,250)
        death_of_pizza_enemy(255,275)
        restart_game(255,300)
    #gameDisplay.fill 0(black)
    #set_dude_position(character_x,character_y)
    #draw_bullets()
    #draw_enemys()
    #pygame.draw.rect(gameDisplay,green,(0,550,600,50))
    #pygame.draw.rect(gameDisplay,purple,(10,562.5,150,25))
    #pygame.draw.rect(gameDisplay,white,(387.5,562.5,200,25))
    #pygame.draw.rect(gameDisplay,green,(392.5,567.5,190,15))
    #pygame.draw.rect(gameDisplay,red,(395 + health,570,185 - health,10))
    #death_of_pizza_enemy(enemy_death_counter_x, enemy_death_counter_y)
    

    pygame.display.update()
    clock.tick(60)


pygame.QUIT()
quit()


    


