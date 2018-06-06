import numpy
import pygame
from pygame.locals import *

from copy import copy, deepcopy

DEBUG = False

screen_width = 18
screen_height = 18

tile_width = 32
tile_height = 32

FPS = 10
fpsClock=pygame.time.Clock()

'''
Class that renders the board into graphical format. 
It is the controller that build the view from the models that is the Board class

Board contains references to that needs to be represented in it, so only board
'''
class Renderer:
    def __init__(self):
        board = None
        tile_set = None

    def load_board(self, board):
        self.board = board
        return self

    def load_tileset(self, tiles):
        self.tile_set = tiles
        return self

    def render_board(self, screen):
        for y in range(0, self.board.get_width()):
            for x in range(0, self.board.get_height()):
                curr_tile = self.board.get_tile((x,y))
                #Check that the tile is valid
                if self.tile_set.is_tile_in_set(curr_tile):
                    #render the tile
                    screen.blit(self.tile_set.get_tileset(), (x*32, y*32), self.tile_set.get_tile_rect(curr_tile))

'''Class that holds all tiles and mapping data for a specific tileset'''
class Tileset:
    __name = ""
    __tiles = None
    __tiles_map = {}
    __int_tile_map = None

    def __init__(self, name):
        self.__name = name

    def get_tileset(self):
        return self.__tiles


    def load_tileset(self, path):
        self.__tiles = pygame.image.load(path)
        self.__tiles_map.update({0:(0, 1*tile_width, 1*tile_width, 1*tile_width)})
        self.__tiles_map.update({1:(2*tile_width, 2*tile_width, 1*tile_width, 1*tile_width)})

        return self

    '''Boolean. Check whether numeric tile is in thing'''
    def is_tile_in_set(self, tile):
        return tile in self.__tiles_map

    '''Returns rectangular tuple of the graphical tile'''
    def get_tile_rect(self, tile):
        return self.__tiles_map[tile]

'''Game board Class
    Model for all information of the current gameboard. References set of 
    characters loaded onto the board for use in a seperate renderer class'''
class Game_board:
    __characters_refs = []     #List of characters on the game board,
                               #scanned through for location at render time
    __map = None               #Integer tile representation array
    __image = None             #Game_board render buffer
    __width = 0
    __height = 0
    __tileset = None

    '''Create game board'''
    def __init__(self, board_name, width, height):
        self.__width        = width
        self.__height       = height
        self.__board_name   = board_name
        self.__tileset      = Tileset("Forest").load_tileset("sprites/Forest.png")
        self.__map = numpy.zeros(shape=(width, height), dtype=numpy.int8)
        self.__map[3][3] = 1

    '''Load list of characters into game map'''
    def load_characters(self, characters_list):
        for character in characters_list:
            self.__characters_refs.append(character)
            character.set_board(self)

    def get_tile(self, tile_loc):
        return self.__map[tile_loc[1]][tile_loc[0]]

    '''Returns the height in tiles of the game map'''
    def get_height(self):
        return self.__height

    '''Returns the width in tiles of the game map'''
    def get_width(self):
        return self.__width

    '''Sets and Creates tile set object'''
    def set_tileset(self, path):
        self.__tileset = Tileset().load_tileset(path)
        return self

    '''Load in integer representation of the game board from file'''
    def load_board_from_file(self, path):
        pass

    '''String representation of game_board'''
    def __str__(self):
        character_map_copy = deepcopy(self.__map)
        for character in self.__characters_refs:
            character_map_copy[character.loc_x][character.loc_y] = 1

        return str(character_map_copy)

    '''Check wether a location tuple is within bounds'''
    def check_bounds(self, loc):
        if (loc[0] >= 0 and loc[0] < self.__width):
            if (loc[1] >= 0 and loc[1] < self.__height):
                if DEBUG: print "CHECKBOUNDS? Pass bounds"
                return True
        if DEBUG: print "CHECKBOUNDS? Fail bounds"
        return False

    '''Checks wether a location tuple is colliding with a map entity'''
    def check_collision(self, loc):
        pass

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

    def set_board(self, board):
        self.__board_ref = board

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
            if direction == "NORTH" and \
                    self.__board_ref.check_bounds((self.loc_x, self.loc_y - 1)):
                if DEBUG: print "PASS BOUNDS"
                self.loc_y = self.loc_y - 1
            elif direction == "SOUTH" and \
                    self.__board_ref.check_bounds((self.loc_x, self.loc_y + 1)):
                if DEBUG: print "PASS BOUNDS"
                self.loc_y = self.loc_y + 1
            elif direction == "WEST" and \
                    self.__board_ref.check_bounds((self.loc_x - 1, self.loc_y)):
                if DEBUG: print "PASS BOUNDS"
                self.loc_x = self.loc_x - 1
            elif direction == "EAST" and \
                    self.__board_ref.check_bounds((self.loc_x + 1, self.loc_y)):
                if DEBUG: print "PASS BOUNDS"
                self.loc_x = self.loc_x + 1

    def get_loc(self):
        return (self.loc_x, self.loc_y)

def main():
    #Intialize game library.
    pygame.init()


    #Load Game objects
    board = Game_board("Test_board", screen_width, screen_height)
    test_player = Character("Paper Boy", (screen_width//2, screen_height//2))
    #Create Screen
    screen = pygame.display.set_mode(
        (board.get_width() * tile_width,
         board.get_height() * tile_height)
    )

    #Load in game sprites and title
    player_sprites = pygame.image.load("sprites/player.png").convert()
    player_sprites.set_colorkey((255,0,255))
    pygame.display.set_icon(player_sprites)
    pygame.display.set_caption("Codemon2.0")


    board.load_characters([test_player])
    test_player.set_sprite_sheet(player_sprites)



    # Game start stop variable
    running = True

    test_tiles = Tileset("Forest").load_tileset("sprites/complete_tileset.png")
    render_engine = Renderer()
    render_engine.load_board(board).load_tileset(test_tiles)

    while running:
        #Clock timing
        fpsClock.tick(FPS)

        #EVENT PROCESSING
        event = pygame.event.poll()
        if event.type == QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if DEBUG: print "KEYDOWN"
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_UP:
                if DEBUG: print "UP"
                test_player.move("NORTH")
            elif event.key == pygame.K_DOWN:
                if DEBUG: print "DOWN"
                test_player.move("SOUTH")
            elif event.key == K_RIGHT:
                if DEBUG: print "RIGHT"
                test_player.move("EAST")
            elif event.key == K_LEFT:
                if DEBUG: print "LEFT"
                test_player.move("WEST")
        pygame.event.clear()  #Flush event queue; deals with ghost action problems


        #TODO Add more tiles to tileset rendere
        #TODO add dirty rectangle blit so that only player old pos and new player pos or animated
        #TODO Add Clock timer

        screen.fill((0,0,0))
        #Blit sprite
        render_engine.render_board(screen)
        screen.blit(test_player.get_sprite_sheet(),
                    (test_player.get_loc()[0] * 32, test_player.get_loc()[1] * 32)
        )
        #Update screen
        pygame.display.update()
    pygame.quit()



if __name__=="__main__":
    main()