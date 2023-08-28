import random
import curses

# Initialiser curses-vinduet
stdscr = curses.initscr()
curses.start_color()  # Aktiver fargemodus

# Definer Tetrominoene og deres former
tetrominoer = [
    [[1, 1, 1, 1]],              # I-formet Tetromino
    [[1, 1, 0], [0, 1, 1]],      # S-formet Tetromino
    [[0, 1, 1], [1, 1, 0]],      # Z-formet Tetromino
    [[1, 0, 0], [1, 1, 1]],      # J-formet Tetromino
    [[0, 0, 1], [1, 1, 1]],      # L-formet Tetromino
    [[1, 1], [1, 1]],            # O-formet Tetromino
    [[1, 1, 1], [0, 1, 0]],      # T-formet Tetromino
]

# Spilllogikk
def main(stdscr):
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)       # Definerer fargepar
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    vinduhøyde = 20
    vindubredden = 10
    win = curses.newwin(vinduhøyde, vindubredden, 0, 0)
    win.border(0)
    win.nodelay(1)

    gjeldende_tetromino = random.choice(tetrominoer)
    gjeldende_tetromino_x = vindubredden // 2 - len(gjeldende_tetromino[0]) // 2
    gjeldende_tetromino_y = 0

    while True:
        win.clear()
        for y, rad in enumerate(gjeldende_tetromino):
            for x, celle in enumerate(rad):
                if celle:
                    # Vis fargede tetromino-celler basert på radnummeret
                    fargepar = y % 7 + 1
                    win.addch(gjeldende_tetromino_y + y, gjeldende_tetromino_x + x, "#", curses.color_pair(fargepar))
        
        win.refresh()

        tast = win.getch()
        if tast == ord("q"):
            break
        elif tast == curses.KEY_RIGHT:
            gjeldende_tetromino_x += 1
        elif tast == curses.KEY_LEFT:
            gjeldende_tetromino_x -= 1
        elif tast == curses.KEY_DOWN:
            gjeldende_tetromino_y += 1

# Kjør spillet ved hjelp av curses.wrapper() for å sikre riktig opprydding
curses.wrapper(main)
