#2:02
import pygame
from sys import exit
player_grounded = False
playing = True
debug = 0
debug_menu = False
highscore = 0
diff = 1
facing_righ = True
running = False
diff_start = 0
color = (64, 64, 64)
win = False
no_clip = False
global time_tick
time_tick = 0

def display_score():

    
    time_tick = int((pygame.time.get_ticks() - start_time)/1000)
    score_surface = test_font.render(str(int(time_tick)), False, (64, 64, 64))
    score_rect = score_surface.get_rect(topleft = (0, 0))
    screen.blit(score_surface, score_rect)

def player_animation():
    global player_surf, player_index
    
    if not player_grounded:
        
        player_index = 0
        if facing_righ:
            player_surf = player_jump_right_surf
            
        else:
            player_surf = player_jump_left_surf
            
    if player_grounded:
        
        if facing_righ:
            
            if running:
                
                player_index += 0.1
                if player_index >= len(player_run_right):
                    player_index = 0
                player_surf = player_run_right[int(player_index)]
                    
            else: # if not running
                player_surf = player_standing_right_surface
                
        else:   #facing left 
            if running:
                
                player_index += 0.1
                
                if player_index >= len(player_run_left):
                    player_index = 0
                    
                player_surf = player_run_left[int(player_index)]

                    
            else: # if not running
                player_surf = player_standing_left_surface
        
            
                
    
        
        
    
empty = (0, 0, 0, 0)
#starting pygame and making a window
pygame.init()
screen = pygame.display.set_mode((800, 600)) 

#title
pygame.display.set_caption("hecker")

clock = pygame.time.Clock()
start_time = 0

#surfaces and rects

test_font = pygame.font.Font("images/Pixeltype.ttf", 50)
debug_font = pygame.font.Font("images/Pixeltype.ttf", 25)
text_surface = test_font.render("Press Enter", True, "Red")
text_rect = text_surface.get_rect(center = (400, 300))

background_surface= pygame.image.load("images/background.jpeg").convert()
floor_surface = pygame.image.load("images/ground.png").convert()


player_standing_right_surface = pygame.image.load("images/standing_right.png").convert_alpha()
player_standing_left_surface = pygame.image.load("images/standing_left.png").convert_alpha()
player_run_right1_surf = pygame.image.load("images/running_right1.png").convert_alpha()
player_run_right2_surf = pygame.image.load("images/running_right2.png").convert_alpha()
player_run_left1_surf = pygame.image.load("images/running_left1.png").convert_alpha()
player_run_left2_surf = pygame.image.load("images/running_left2.png").convert_alpha()
player_jump_right_surf = pygame.image.load("images/jump_right.png").convert_alpha()
player_jump_left_surf = pygame.image.load("images/jump_left.png").convert_alpha()
player_surf = 0
player_run_right = [player_run_right1_surf, player_run_right2_surf]
player_run_left = [player_run_left1_surf, player_run_left2_surf]

player_index = 0
player_rect = player_standing_right_surface.get_rect(midbottom = (400, 540))
player_grav = 0

star_surface = pygame.image.load("images/wall.png").convert_alpha()
star_rect = star_surface.get_rect(midbottom = (800, 540))
pygame.display.set_icon(star_surface)
pygame.draw.line(screen, (255, 189, 60), (0, 0), (800, 600))

while True:
    
    for event in pygame.event.get():
        # makes exit possible
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

        #get mouse pos
        #if event.type == pygame.MOUSEMOTION:
            #print(event.pos)
            #if player_rect.collidepoint(event.pos):
                #print("test")
        #if mouse is pressed down or up
        #if event.type == pygame.MOUSEBUTTONUP:
            #print("up")
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #print("down")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_grounded:
                player_grav -= 20 
            if event.key == pygame.K_7:
                no_clip = not no_clip
                print(no_clip)
            if event.key == pygame.K_1:
                debug_menu = not debug_menu
            
    
        #if event.type == pygame.KEYUP:
            #print("up")
        #star speed
    
    star_rect.x += (5 * diff)
    
    if playing:
        
        if int((pygame.time.get_ticks()/1000) - diff_start) == 5:
            diff += 0.3
        
            diff_start += 5

        
        
        #gravity
     
        if player_rect.bottom >= 540:
            if player_grounded == False:
                player_grav = 0
            player_grounded = True 
            if player_rect.bottom > 540:
                player_rect.bottom  = 539
        else:
            player_grounded = False
        if not player_grounded:
            player_grav += 1 
        player_rect.y += player_grav

        
        if star_rect.colliderect(player_rect) and no_clip == False:
            playing = False
            
            

        #rendering surfaces
        screen.blit(background_surface,(0, 0))

        screen.blit(floor_surface, (0, 540))

        player_animation()

        screen.blit(player_surf, player_rect)

        display_score()
        debug_surf = debug_font.render(f"No_clip:{no_clip}", True, (0, 0, 0))
        debug_rect = debug_surf.get_rect(topleft = (0, 50))
        if debug_menu:
            screen.blit(debug_surf, debug_rect)

        # makes sure the star doesn't move of the screen
        if star_rect.left >= 800:
            star_rect.right = 0
        elif star_rect.right <= -50: 
            star_rect.left = 800
        screen.blit(star_surface, star_rect)
        if player_rect.left >= 800:
            player_rect.right = 799
        elif player_rect.right <= 0: 
            player_rect.left = 1
        screen.blit(star_surface, star_rect)

        #if player_rect.colliderect(star_rect):
        #   print("yay") 

        #collision with mouse and check if mouse pressed
            #mouse_pos=pygame.mouse.get_pos()
        #if player_rect.collidepoint(mouse_pos):
            #print(pygame.mouse.get_pressed())
    
        #if key is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            #player speed
            player_rect.x += (5 * diff)
            if not facing_righ:
                player_index = 0
            
            running = True
            facing_righ = True
        elif keys[pygame.K_a]:
            player_rect.x -= (5 * diff)
            if facing_righ:
                player_index = 0
            running = True
            facing_righ = False
        else:
            running = False
    elif playing == False:
        end_score = int((pygame.time.get_ticks()-start_time)/1000)
        while not playing:
            
            if int((pygame.time.get_ticks()/1000) - diff_start) == 5:
                diff += 1
                diff_start += 5
                
            
            
            
            end_score_surf = test_font.render(f"Score: {end_score}", False, (64, 64, 64))
            end_score_rect = end_score_surf.get_rect(center = (400, 450))
            highscore_surf = test_font.render(f"Highscore: {highscore}", False, (64, 64,64))

            highscore_rect = highscore_surf.get_rect(center =(400, 400))
            
            screen.blit(background_surface,(0, 0))
            screen.blit(text_surface, text_rect)
            screen.blit(floor_surface, (0, 540))
            
            

            if end_score > highscore:
                print("diadjwdka")
                newhighscore_text_surf = test_font.render("New Highscore", False, "yellow")
                newhighscore_text_rect = newhighscore_text_surf.get_rect(center = (400, 350))
                screen.blit(newhighscore_text_surf, newhighscore_text_rect)
            
                
                
               
            

                
            screen.blit(end_score_surf, end_score_rect)
            screen.blit(highscore_surf, highscore_rect)
            

            
            
            player_grounded = False
            pygame.display.update()
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_RETURN:
                        playing = True
                        start_time = pygame.time.get_ticks()
                        player_rect.midbottom = 400, 540
                        star_rect.midbottom = 800, 540
                        
                    
                        if end_score > highscore:
                            highscore = end_score
                        diff = 1
                        screen.blit(star_surface, star_rect)
                        
                        
            # detects space pressed causes glitch
            #keys = pygame.key.get_pressed()
            #if keys[pygame.K_SPACE]:
                #playing = True
                #screen.blit(player_standing_surface, player_rect)
                #screen.blit(star_surface, star_rect)
            
    pygame.display.update()

    #clock.tick(max fps)
    clock.tick(60)