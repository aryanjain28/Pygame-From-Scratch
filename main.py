import pygame

pygame.init()

window = pygame.display.set_mode((2000,2000))
pygame.display.set_caption("Caption")

x,y,w,h = 0, 0, 20, 20
v = 5
run = True

isJump = False
jumpCount = 10

while run:
    
    pygame.time.delay(50)

    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x<500-w:
        x+=v
    if keys[pygame.K_LEFT] and  x>v:
        x-=v
    
    if not isJump:
        if keys[pygame.K_UP] and y>v :
            y-=v
        if keys[pygame.K_DOWN] and y<500-h:
            y+=v
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y-=(jumpCount**2) * 0.5 * neg
            jumpCount-=1
        else:
            isJump = False
            jumpCount = 10


    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0 ,0 ), (x,y,w,h))
    pygame.display.update()

pygame.quit()