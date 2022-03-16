import pygame
from random import randint

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Reaction Time')
clock = pygame.time.Clock()
off = False
start = False
show = False
wait = 99999999999
font = pygame.font.SysFont('Arial', 24)

while not off:

    time = pygame.time.get_ticks()

    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,0,0),(400,300),30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            off = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if not start:
                start = True
                wait = randint(3000,8000) + time
            if show:
                start = False
                timer = time - wait
                show = False
                wait = 9999999999
                print(timer)

    if time >= wait:
        show = True

    if show:
        pygame.draw.circle(screen,(255,255,255),(400,300),100)

    fps = font.render(str(int(clock.get_fps())),False,(255,255,255))
    screen.blit(fps,(0,0))

    clock.tick(300)
    pygame.display.update()

pygame.quit()
