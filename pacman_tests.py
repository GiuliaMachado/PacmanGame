#teste pra encontrar o pacman no mapa
#x, y = find_pacman(map)
#print(x)
#print(y)

import unittest

from pacman import find_pacman, move_pacman


class PacmanTest(unittest.TestCase):

    def test_find_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        x, y = find_pacman(map)

        self.assertEqual(x, 3)
        self.assertEqual(y, 5)

    def test_find_pacman_when_pacman_doesnt_exist(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G.....|.|",
            "|........|",
            "|--------|"
        ]

        x, y = find_pacman(map)

        self.assertEqual(x, -1)
        self.assertEqual(y, -1)

    def test_move_pacman(self):
        map = [
            "|--------|",
            "|G..|..G.|",
            "|...PP...|",
            "|G...@.|.|",
            "|........|",
            "|--------|"
        ]

        move_pacman(map, 4, 1)

        new_x, new_y = find_pacman(map)

        self.assertEqual(new_x, 4)
        self.assertEqual(new_y, 1)

