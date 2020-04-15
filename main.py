import pygame

pygame.init()

window = pygame.display.set_mode((1500,1000))
pygame.display.set_caption("Caption")

x,y,w,h = 10, 10, 20, 20
v = 1
run = True

while run:
    
    pygame.time.delay(1)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y-=v
    if keys[pygame.K_DOWN]:
        y+=v
    if keys[pygame.K_RIGHT]:
        x+=v
    if keys[pygame.K_LEFT]:
        x-=v
    
    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0 ,0 ), (x,y,w,h))
    pygame.display.update()

pygame.quit()