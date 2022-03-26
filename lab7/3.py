import pygame
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
working=True
x,y=200,200
red=(225,0,0)
step=20
while working:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        working = False
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: 
        if y>=40:
            y -= step
    elif pressed[pygame.K_DOWN]:
        if y<=360: 
            y += step
    elif pressed[pygame.K_LEFT]: 
        if x>=40:
            x -= step
    elif pressed[pygame.K_RIGHT]: 
        if x<=360:
            x += step

    screen.fill((0,0,0)) 
    pygame.draw.circle(screen,red,(x, y),25)
    
    pygame.display.flip()
    clock.tick(60)

pygame.exit()
