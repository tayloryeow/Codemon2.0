from Constants import *

#TODO add event listener bounds checking
class Character:
    __name = ""
    __loc_y = 0
    __loc_x = 0
    __board_ref = None #Sets what board the character is loaded into
    __sprite_sheet = None

    __up_sprite =    [(32, 96, 32, 32), (0, 96, 32, 32), (64, 96, 32, 32)]
    __down_sprite =  [(32,  0, 32, 32), (0, 0,  32, 32), (64,  0, 32, 32)]
    __left_sprite =  [(32, 32, 32, 32), (0, 32, 32, 32), (64, 32, 32, 32)]
    __right_sprite = [(32, 64, 32, 32), (0, 64, 32, 32), (64, 64, 32, 32)]

    __sprite_locs = [__up_sprite, __right_sprite, __down_sprite, __left_sprite ]

    __curr_sprite = __down_sprite

    face_dir = SOUTH
    __prev_face_dir = ""
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

    def get_next_sprite(self):
        #Sets next character sprite based on current facing direction
        #Sprite locs are hardcoded in class header
        self.__curr_sprite = self.__sprite_locs[self.face_dir]

        return self.__curr_sprite[self.anim_num]

    # Move the character - only works on discrete directions
    def move(self, direction):
        self.__prev_face_dir = self.face_dir

        new_x = self.loc_x
        new_y = self.loc_y
        if direction:
            if direction == "NORTH":
                self.face_dir =  NORTH
                new_y = new_y - 1
            elif direction == "SOUTH":
                self.face_dir = SOUTH
                new_y = new_y + 1
            elif direction == "WEST":
                self.face_dir = WEST
                new_x = new_x - 1
            elif direction == "EAST":
                self.face_dir = EAST
                new_x = new_x + 1
        if self.__board_ref.check_bounds((new_x, new_y)) and not self.__board_ref.collides((new_x, new_y)):
            self.loc_x = new_x
            self.loc_y = new_y

        # Keep track of movement animation number. Reset number if face_dur is different.
        if self.__prev_face_dir == self.face_dir:
            self.anim_num = (self.anim_num + 1) % 3
        else:
            self.anim_num = 0

    def get_loc(self):
        return (self.loc_x, self.loc_y)