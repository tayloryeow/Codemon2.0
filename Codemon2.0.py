`import numpy
import pygame

screen_width = 1280
screen_height = 640

tile_width = 40
tile_height = 40

FPS = 30
fpsClock=pygame.time.Clock()


class Character:
    loc_y = 0
    loc_x = 0

    def __init__(self, name, tilesheet):
        self.name = name
        self.tilesheet = tilesheet
        self.step_x = 40
        self.step_y = 40

    # Move the character - only works on discrete directions
    def move(self, direction):
        if direction:
            if direction == "North":
                self.loc_y = self.loc_y - 1 * self.step_y
            elif direction == "South":
                self.loc_y = self.loc_y + 1 * self.step_y
            elif direction == "West":
                self.loc_x = self.loc_x - 1
            elif direction == "East":
                self.loc_x = self.loc_x + 1

    def get_loc(self):
        return (self.loc_x, self.loc_y)



def main():
    #Intialize game library.
    pygame.init()

    screen_width = 10
    screen_height = 10

    tile_width = 40
    tile_height = 40

    #Create a zero gameboard
    game_board = numpy.zeros(shape=(screen_width, screen_height))

    #Load in game sprites
    #player_sprites = pygame.image.load("sprites/player.png")
    #pygame.display.set_icon(player_sprites)
    #pygame.display.set_caption("Codemon2.0")

    print (game_board)

    #Create Screen
    screen = pygame.display.set_mode((screen_width * tile_width, screen_height * tile_height))

    # Game start stop variable
    running = True

    #Load Character tilesheet
    #player = Character("player", player_sprites);

    while running:
        print game_board
    



if __name__=="__main__":
    main()