from constants import BTN_SLCT, BTN_DOWN, BTN_UP
import pygame as pg


FPS = 30
DEBUG = True

# map button to keys
bmap = {
    BTN_SLCT: [pg.K_SPACE, pg.K_RETURN],
    BTN_UP: [pg.K_UP, pg.K_w],
    BTN_DOWN: [pg.K_DOWN, pg.K_s]
    }

# map keys to button, eg K_d -> 'right'
kmap = {e: btn for (btn, v) in bmap.items() for e in v}
