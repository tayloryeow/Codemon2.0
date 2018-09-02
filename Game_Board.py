import pygame
import Codemon2
import numpy

from constants import *

'''Class that holds all tiles and mapping data for a specific tileset'''
class Tileset:
    __name = ""                 #Name of this tileset
    __tiles = None              #Graphical Tileset image

    #Mapping of tile's int representations to graphical tile_set locations
    __tiles_map = {
        GRASS:(0,32,32,32),
        SIGN:(64,0,98,32),
        TALL_GRASS:(64,32,98,64)
    }

    def __init__(self, name):
        self.__name = name

    def get_tileset(self):
        return self.__tiles


    def load_tileset(self, path):
        self.__tiles = pygame.image.load(path)
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


