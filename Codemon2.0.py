import numpy
import pygame
from pygame.locals import *
import sys
from copy import copy, deepcopy

screen_width = 1280
screen_height = 640

tile_width = 40
tile_height = 40

FPS = 30
fpsClock=pygame.time.Clock()




class Game_board:
    characters_list = None

    '''Create game board'''
    def __init__(self, board_name, width, height):
        self.width = width
        self.height = height
        self.board_name = board_name
        self.tiles = numpy.zeros(shape=(width, height))

    '''Load list of characters into game map'''
    def load_characters(self, characters_list):
        self.characters_list = characters_list

    '''String representation of game_board'''
    def __str__(self):

        character_map_copy = deepcopy(self.tiles)

        for character in self.characters_list:
            character_map_copy[character.loc_x][character.loc_y] = 8

        return str(character_map_copy)

class Character:
    __name = ""
    __loc_y = 0
    __loc_x = 0
    __board_ref = None #Sets what board the character is loaded into
    __sprite_sheet = None

    def __init__(self, name, location):
        self.name = name
        self.loc_y = location[0]
        self.loc_x = location[1]

    def set_loc(self, location):
        loc_x = location[0]
        loc_y = location[1]

    def set_name(self, name):
        self.name = name

    def set_sprite_sheet(self, sprite):
        self.sprite = sprite

    def get_loc(self):
        return (self.loc_x, self.loc_y)

    def get_name(self):
        return self.name

    def get_sprite_sheet(self):
        return self.sprite


    # Move the character - only works on discrete directions
    def move(self, direction):
        if direction:
            if direction == "NORTH":
                self.loc_y = self.loc_y - 1
            elif direction == "SOUTH":
                self.loc_y = self.loc_y + 1
            elif direction == "WEST":
                self.loc_x = self.loc_x - 1
            elif direction == "EAST":
                self.loc_x = self.loc_x + 1

    def get_loc(self):
        return (self.loc_x, self.loc_y)

def main():
    #Intialize game library.
    pygame.init()

    tile_width = 40
    tile_height = 40

    #Load in game sprites and title
    player_sprites = pygame.image.load("sprites/player.png")
    pygame.display.set_icon(player_sprites)
    pygame.display.set_caption("Codemon2.0")


    board = Game_board("Test_board", 2, 2)
    test_player = Character("Paper Boy", (0, 0))
    board.load_characters([test_player])
    test_player.set_sprite_sheet(player_sprites)

    #Create Screen
    screen = pygame.display.set_mode((board.width * tile_width*10, board.height * tile_height*10))


    # Game start stop variable
    running = True

    #Load Character tilesheet
    #player = Character("player", player_sprites);

    while running:
        #EVENT PROCESSING
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.K_DOWN:
                print ("down")
                test_player.move("SOUTH")
            elif event.type == pygame.K_UP:
                print("up")
                test_player.move("NORTH")

        #TODO Write renderer that creates a bitmap from board repr
        #TODO add dirty rectangle blit so that only player old pos and new player pos or animated
        #TODO fix key event handling
        #TODO add 4 dimensional movement to thing
        #TODO Add Clock timer

        #Blit sprite
        screen.blit(test_player.get_sprite_sheet(), test_player.get_loc())
        #Update screen
        pygame.display.flip()
        screen.fill((255, 255, 255))    #Clear the screen
        pygame.time.delay(500)


        #print board




if __name__=="__main__":
    main()