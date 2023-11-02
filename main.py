import pygame


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0 # delta time

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() /2)

# game loop
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #this will whip away the last frame's state    
    screen.fill("purple")

    pygame.draw.circle(screen, "black", player_pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        player_pos.y += 300 * dt
    if keys[pygame.K_LEFT]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        player_pos.x += 300 * dt

    #shows on screen and dows some good display things 
    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()
