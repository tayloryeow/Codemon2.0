from Renderer import Renderer
from character import *
from pygame.locals import *
from Game_Board import *




FPS = 60
fpsClock=pygame.time.Clock()

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
    player_sprites = pygame.image.load("sprites/player.png")
    player_sprites.convert()
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


        screen.fill((0,0,0))

        #Render the Game board to the screen buffer
        render_engine.render_board(screenbuff)

        #Temporary location variables
        player_x = test_player.get_loc()[0]
        player_y = test_player.get_loc()[1]

        #Draw the player on the screen
        screenbuff.blit(test_player.get_sprite_sheet(),
                    (player_x * 32, player_y * 32), test_player.get_next_sprite()
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