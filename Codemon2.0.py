import pygame
import sys

def main():
    pygame.init()

    player = pygame.image.load("player.png")
    pygame.display.set_icon(player)
    pygame.display.set_caption("minimal program")

    #Create surface
    screen = pygame.display.set_mode((640, 640))

    # Game start stop variable
    running = True

    #Draw player sprite onto buffer
    screen.blit(player, (50, 50))

    #Draw buffer to screen
    pygame.display.flip()

    player.set_colorkey((255, 0, 255))
    screen.fill((0,0,0))
    #Game Loop
    while running:
        #Event handling,
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__=="__main__":
    main()