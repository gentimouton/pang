""" 
If game state is lost, call game over scene.
Can also pause game and go to main menu, passing an option to resume game.
"""

from constants import CMD_NEWG, CMD_RESM
from controls import controller
import pview
import pygame as pg
from scene import SCN_MENU, Scene, SCN_OVER
import settings


class GameScene(Scene):

    def __init__(self):
        """ load images and sounds from disk here """
        self._build_new_game()
        
    def tick(self, ms):
        """ process player inputs """
        if controller.btn_event('select'):
            return SCN_MENU, {'can_resume':1}  # add "Resume Game" to menu scene
        
        pview.fill([255, 0, 0])
        pg.display.flip()
        return None, {}

    def resume(self, **kwargs):
        """ Scene callback. Called from the menu scene via scene manager. """
        if kwargs['cmd'] == CMD_NEWG:
            self._build_new_game()
        elif kwargs['cmd'] == CMD_RESM:
            pass
        

    def _build_new_game(self):
        pview.fill([255, 0, 0])

        
        
if __name__ == "__main__":
    pg.init()
    pview.set_mode((800, 600))
    clock = pg.time.Clock()
    scene = GameScene()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    done = True
                elif event.key == pg.K_F11:
                    pview.toggle_fullscreen()
        ms = clock.tick(settings.FPS)
        scene_id, kwargs = scene.tick(ms)
        pg.display.set_caption('game scene %.1f' % clock.get_fps())
