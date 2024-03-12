import sys
import pyautogui as pg
import keyboard as kb
from PIL import ImageGrab


if __name__ == '__main__':
    rows, cols = int(sys.argv[1]), int(sys.argv[2])
    print(rows, cols)
    pg.PAUSE = 0

    print('Click top left corner of the grid')
    kb.wait('enter')
    left, top = pg.position()

    print('Click bottom right corner of the grid')
    kb.wait('enter')
    right, bottom = pg.position()

    pieceWidth, pieceHeight = (right - left) // cols, (bottom - top) // rows

    
