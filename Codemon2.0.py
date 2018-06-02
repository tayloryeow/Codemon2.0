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
    __characters_refs = None
    __map = None
    __image = None
    __width = 0
    __height = 0


    '''Create game board'''
    def __init__(self, board_name, width, height):
        self.__width = width
        self.__height = height
        self.__board_name = board_name
        self.__map = numpy.zeros(shape=(width, height))
        #self.__image = pygame.display.

    '''def render_board(self):
        for y in range(0, self.__width):
            for x in range(0, self.__height):
    '''

    '''Load list of characters into game map'''
    def load_characters(self, characters_list):
        self.__characters_refs = characters_list

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    '''String representation of game_board'''
    def __str__(self):
        character_map_copy = deepcopy(self.__map)
        for character in self.__characters_refs:
            character_map_copy[character.loc_x][character.loc_y] = 8

        return str(character_map_copy)

#TODO add event listener bounds checking
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
                self.loc_y = self.loc_y - 1 * 40
            elif direction == "SOUTH":
                self.loc_y = self.loc_y + 1 * 40
            elif direction == "WEST":
                self.loc_x = self.loc_x - 1 * 40
            elif direction == "EAST":
                self.loc_x = self.loc_x + 1 * 40

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


    board = Game_board("Test_board", 10, 10)
    test_player = Character("Paper Boy", (0, 0))
    board.load_characters([test_player])
    test_player.set_sprite_sheet(player_sprites)

    #Create Screen
    screen = pygame.display.set_mode((board.get_width() * tile_width, board.get_height() * tile_height))


    # Game start stop variable
    running = True

    #Load Character tilesheet
    #player = Character("player", player_sprites);

    while running:
        #EVENT PROCESSING
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                test_player.move("NORTH")
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                test_player.move("SOUTH")
            elif event.type == pygame.KEYDOWN and event.key == K_RIGHT:
                test_player.move("EAST")
            elif event.type == pygame.KEYDOWN and event.key == K_LEFT:
                test_player.move("WEST")

        #TODO Write renderer that creates a bitmap from board repr
        #TODO add dirty rectangle blit so that only player old pos and new player pos or animated
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