import numpy
import pygame
from character import *
from Game_Board import *
from pygame.locals import *

from copy import copy, deepcopy

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

    def load_player(self, player):
        self.player = player
        return player

    def load_tileset(self, tiles):
        self.tile_set = tiles
        return self

    '''Loop through every index of the bitmap and resolve it into its graphical tile'''
    def render_board(self, screen):
        # create a new Surface
        for y in range(0, self.board.get_width()):
            for x in range(0, self.board.get_height()):
                curr_int_tile = self.board.get_tile((x,y))

                #Check that the tile is valid
                if self.tile_set.is_tile_in_set(curr_int_tile):
                    #render the tile - cut the approparite tile from the tileset and past that there
                    screen.blit(self.tile_set.get_tileset(), (x*32, y*32), self.tile_set.get_tile_rect(curr_int_tile))


def main():
    #Intialize game library.
    pygame.init()

    #Load Game objects
    board = Game_board("Test_board", screen_width, screen_height)
    test_player = Character("Paper Boy", (screen_width // 2, screen_height // 2))
    #Create Screen
    screen = pygame.display.set_mode(
        (board.get_width() * tile_width,
         board.get_height() * tile_height)
    )

    #Create Screen Buffer
    screenbuff = pygame.Surface(
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

    #Add a buffer
    #todo make render render out to a buffer then to screen

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


        screen.fill((0,0,0))

        #Render the Game board to the screen buffer
        render_engine.render_board(screenbuff)

        #Temporary location variables
        player_x = test_player.get_loc()[0]
        player_y = test_player.get_loc()[1]

        #Draw the player on the screen
        screenbuff.blit(test_player.get_sprite_sheet(),
                    (player_x * 32, player_y * 32)

        )
        #Update screen, write screen buffer to screen
        screen.blit(screenbuff,
                    ((screen_width / 2 - player_x) * 32,
                     (screen_height / 2-player_y) * 32)
        )
        pygame.display.update()
    pygame.quit()

if __name__=="__main__":
    main()