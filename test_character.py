import unittest
from Codemon2 import character_src


class TestCharacter(unittest.TestCase):
    def test_set_loc(self):

        test_loc = (10,10)
        testCharacter = character_src("test", (0, 0))
        testCharacter.set_loc(test_loc)

    def test_set_name(self):
        test_name = "name!"
        testCharacter = character_src("test", (0, 0))
        testCharacter.set_name(test_name)

        assert(testCharacter.get_name() == test_name)

    def test_get_loc(self):
        test_name = "name!"
        testCharacter = character_src("test", (0, 0))
        testCharacter.set_name(test_name)

        assert(testCharacter.get_name() == test_name)

    def test_get_name(self):
        test_name = "name!"
        testCharacter = character_src("test", (0, 0))
        testCharacter.set_name(test_name)

        assert(testCharacter.get_name() == test_name)

    def test_get_sprite_sheet(self):
        test_sheet = "complete_tileset.png"

        test_char = character_src("test", (0, 0))
        test_char.set_sprite_sheet(test_sheet)

        test_char.get_sprite_sheet() == test_sheet



if __name__ == "__main__":
    unittest.main()