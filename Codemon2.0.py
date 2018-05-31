import numpy
import pygame

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

        for character in characters_list:
            self.tiles[character.loc_y][character.loc_x] = 8

    '''Reflect the position of the board's characters in objs tile representation'''
    def update_character_positions(self):
        for character in self.characters_list:
            self.tiles[character.loc_y][character.loc_x] = 8

    '''String representation of game_board'''
    def __str__(self):
        return str(self.tiles)

class Character:
    def __init__(self, name, start_y, start_x):
        self.name = name
        self.step_x = 40
        self.step_y = 40
        self.tile_sheet = None
        self.loc_y = start_y
        self.loc_x = start_x

    def load_tile_sheet(self, tilesheet):
        self.tile_sheet = tilesheet

    # Move the character - only works on discrete directions
    def move(self, direction):
        if direction:
            if direction == "North":
                self.loc_y = self.loc_y - 1
            elif direction == "South":
                self.loc_y = self.loc_y + 1
            elif direction == "West":
                self.loc_x = self.loc_x - 1
            elif direction == "East":
                self.loc_x = self.loc_x + 1

    def get_loc(self):
        return (self.loc_x, self.loc_y)

def main():
    #Intialize game library.
    pygame.init()

    tile_width = 40
    tile_height = 40

    #Load in game sprites
    #player_sprites = pygame.image.load("sprites/player.png")
    #pygame.display.set_icon(player_sprites)
    #pygame.display.set_caption("Codemon2.0")


    board = Game_board("Test_board", 2, 2)
    test_player = Character("Paper Boy", 0, 0)
    board.load_characters([test_player])

    #Create Screen
    #screen = pygame.display.set_mode((screen_width * tile_width, screen_height * tile_height))

    # Game start stop variable
    running = True

    #Load Character tilesheet
    #player = Character("player", player_sprites);

    while running:
        board.update_character_positions()
        print board




if __name__=="__main__":
    main()