from constants import BTN_SLCT, BTN_DOWN1, BTN_DOWN2, BTN_UP1, BTN_UP2
import pygame as pg


FPS = 30
DEBUG = True

# map button to keys
bmap = {
    BTN_SLCT: [pg.K_SPACE, pg.K_RETURN],
    BTN_UP1: [pg.K_w],
    BTN_DOWN1: [pg.K_s],
    BTN_UP2: [pg.K_UP],
    BTN_DOWN2: [pg.K_DOWN]
    }

# map keys to button, eg K_d -> 'right'
kmap = {e: btn for (btn, v) in bmap.items() for e in v}
