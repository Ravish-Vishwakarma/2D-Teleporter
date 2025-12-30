import pygame
import sys
import random
pygame.init()

screen_w,screen_h = 980,660
screen = pygame.display.set_mode((screen_w,screen_h))
pygame.display.set_caption('My Game')

#variables
running = True
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
pink = (255, 192, 203)
yellow = (255, 255, 0)
orange = (255, 165, 0)
rect_w , rect_h = 20,20
rect_x , rect_y = screen_w // 2 - rect_w//2 , screen_h // 2 - rect_h//2 
rect_speed = 5
# background = pygame.image.load('background.jpg')
increase = pygame.mixer.Sound('increase.wav')
decrease = pygame.mixer.Sound('decrease.wav')
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial',25)
obstacles = [
    (pygame.Rect(200, 150, 100, 50), black),
    (pygame.Rect(400, 300, 50, 100), green),
    (pygame.Rect(600, 100, 75, 75), blue),
    (pygame.Rect(100, 400, 120, 60), yellow),
    (pygame.Rect(700, 350, 40, 110), pink)
]
food_y = random.randint(10,640)
food_x = random.randint(10,960)
food_h = 20
food_w = 20

# def generate_food():
#     while True:
#         food_y = random.randint(10, 640)
#         food_x = random.randint(10, 960)

#         # Exclude range (e.g., 200-300 for both x and y)
#         if not (200 <= food_x <= 300 and 200 <= food_y <= 300):
#             return True

while running:
    screen.fill(white)
    # screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_LEFT]: #and rect_x > 0:
        rect_x -= rect_speed
    if key_pressed[pygame.K_RIGHT]:# and rect_x < screen_w - rect_w:
        rect_x += rect_speed
    if key_pressed[pygame.K_UP]: #and rect_y > 0:
        rect_y -= rect_speed
    if key_pressed[pygame.K_DOWN]:#and rect_y < screen_h - rect_h:
        rect_y += rect_speed
    if key_pressed[pygame.K_r]:

        rect_x = screen_w // 2 - rect_w//2 
        rect_y = screen_h // 2 - rect_h//2
        rect_w = 20
        rect_h = 20
    if key_pressed[pygame.K_i]:
        rect_w += 2
        rect_h += 2
        increase.play()
    if key_pressed[pygame.K_d]:
        if (rect_w >20 and rect_h>20):    
            rect_w -= 2
            rect_h -= 2
            decrease.play()
    if (rect_x == screen_w-screen_w):
        rect_x = screen_w
    if (rect_y == screen_h-screen_h):
        rect_y = screen_h
    if rect_x == screen_w+rect_w:
        rect_x = 0
    if rect_y == screen_h+rect_h:
        rect_y = 0
    

    # food_x, food_y = generate_food()
    pygame.draw.rect(screen, orange, pygame.Rect(food_x, food_y, food_w, food_h))

    player_rect = pygame.Rect(rect_x, rect_y, rect_w, rect_h)
    for obstacle,color in obstacles:
        if player_rect.colliderect(obstacle):
            rect_x, rect_y = screen_w // 2 - rect_w // 2, screen_h // 2 - rect_h // 2
            decrease.play()
            break

    for obstacle, color in obstacles:
        pygame.draw.rect(screen, color, obstacle)

    
    pygame.draw.rect(screen,red,(rect_x,rect_y,rect_w,rect_h))
    position_txt = font.render(f'Position: ({rect_x}, {rect_y})', True, (0, 0, 0))
    screen.blit(position_txt, (10, 10))
    pygame.display.flip()
    clock.tick(120)

pygame.quit()
sys.exit()