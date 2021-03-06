from constants import OUT_FSCR, OUT_QUIT
from controls import controller
import pview
import pygame as pg
import scene_manager as sm
import settings


def main():
    pg.init()
    pg.display.set_caption('Pang')
    pview.set_mode((800, 600))
    clock = pg.time.Clock()
    sm.init()
    
    while True:
        ms = clock.tick(settings.FPS) # throttle
        
        outcome = controller.poll() # get player input
        if outcome == OUT_QUIT:
            break
        elif outcome == OUT_FSCR:
            pview.toggle_fullscreen()

        outcome = sm.scene_manager.tick(ms) # update scene 
        if outcome == OUT_QUIT:
            break

if __name__ == "__main__":
    main()