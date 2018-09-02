from constants import *

#TODO add event listener bounds checking
class Character:
    __name = ""
    __loc_y = 0
    __loc_x = 0
    __board_ref = None #Sets what board the character is loaded into
    __sprite_sheet = None

    face_dir = None
    anim_num = 0

    def __init__(self, name, location):
        self.name = name
        self.loc_y = location[0]
        self.loc_x = location[1]

    def get_face_dir(self):
        return self.face_dir

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
            if direction == "NORTH":
                self.face_dir =  NORTH
                if self.__board_ref.check_bounds((self.loc_x, self.loc_y - 1)):
                    if DEBUG: print "PASS BOUNDS"
                    self.loc_y = self.loc_y - 1
            elif direction == "SOUTH":
                self.face_dir = SOUTH
                if self.__board_ref.check_bounds((self.loc_x, self.loc_y + 1)):
                    if DEBUG: print "PASS BOUNDS"
                    self.loc_y = self.loc_y + 1
            elif direction == "WEST":
                self.face_dir = WEST
                if self.__board_ref.check_bounds((self.loc_x - 1, self.loc_y)):
                    if DEBUG: print "PASS BOUNDS"
                    self.loc_x = self.loc_x - 1
            elif direction == "EAST":
                self.face_dir = EAST
                if self.__board_ref.check_bounds((self.loc_x + 1, self.loc_y)):
                    if DEBUG: print "PASS BOUNDS"
                    self.loc_x = self.loc_x + 1

    def get_loc(self):
        return (self.loc_x, self.loc_y)