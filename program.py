from pacman import play, move_ghosts
from ui import ui_print, ui_key, ui_msg_lost, ui_msg_won
# @ -> our hero
# G -> ghosts
# P -> pills
# . -> empty spaces
# | and - -> walls
map = [
    "|--------|",
    "|G..|..G.|",
    "|...PP...|",
    "|G....|..|",
    "|.......@|",
    "|--------|"
]

game_finished = False

while not game_finished:
    ui_print(map)
    key = ui_key()
    valid_key, pacman_alive, won = play(map, key)

    pacman_was_hit = move_ghosts(map)

    if (not pacman_alive) or (pacman_was_hit):
        ui_msg_lost()
        game_finished = True
    elif won:
        ui_msg_won()
        game_finished = True

