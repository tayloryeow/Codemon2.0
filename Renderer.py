'''
Class that renders the board into graphical format.
It is the controller that build the view from the models that is the Board class

Board contains references to that needs to be represented in it, so only board
'''

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
        for y in range(0, self.board.get_height()):
            for x in range(0, self.board.get_width()):
                curr_int_tile = self.board.get_tile((x,y))

                #Check that the tile is valid
                if self.tile_set.is_tile_in_set(curr_int_tile):
                    #render the tile - cut the approparite tile from the tileset and past that there
                    screen.blit(self.tile_set.get_tileset(), (x*32, y*32), self.tile_set.get_tile_rect(curr_int_tile))