""" 
If game state is lost, call game over scene.
Can also pause game and go to main menu, passing an option to resume game.
"""

from constants import CMD_NEWG, CMD_RESM
from controls import controller
from pview import T
import pview
import pygame as pg
from scene import Scene
from constants import BTN_DOWN1, BTN_UP1, BTN_UP2, BTN_DOWN2

PADW, PADH = 10, 100
WALW, WALH = 700, 10


class GameScene(Scene):

    def __init__(self):
        """ load images and sounds from disk here """
        self._build_new_game()
        
    def tick(self, ms):
        """ process player inputs and move ball """
        # paddle 1
        p1, p2 = self.paddle1, self.paddle2
        if controller.btn_ispressed(BTN_UP1) and p1.y >= WALH:
            p1.move_ip(0, -20)
        elif controller.btn_ispressed(BTN_DOWN1) and p1.y + PADH + WALH < 600:
            p1.move_ip(0, 20)
        # paddle 2
        if controller.btn_ispressed(BTN_UP2) and p2.y >= WALH:
            p2.move_ip(0, -20)
        elif controller.btn_ispressed(BTN_DOWN2) and p2.y + PADH + WALH < 600:
            p2.move_ip(0, 20)
                
        # ball
        ball = self.ball
        ball.move_ip(self.ball_speed)
        # hit a paddle
        if ball.collidelist([p1, p2]) != -1:
            dx, dy = self.ball_speed
            self.ball_speed = [-1.1 * dx, 1.1 * dy]
            
        # goal!
        if ball.x <= 10 or ball.x >= 770:
            self._build_new_game()
            
        # bounce on walls
        if ball.collidelist(self.walls) != -1:
            dx, dy = self.ball_speed
            self.ball_speed = [dx, -dy]
            ball.move_ip(0, -dy)
        
        self._draw()
        return None, {}

    def resume(self, **kwargs):
        """ Scene callback. Called from the menu scene via scene manager. """
        if kwargs['cmd'] == CMD_NEWG:
            self._build_new_game()
        elif kwargs['cmd'] == CMD_RESM:
            pass

    def _build_new_game(self):
        self.walls = [pg.Rect(0, 0, 800, 10), pg.Rect(0, 590, 800, 600)]
        self.ball = pg.Rect(100, 100, 20, 20)
        self.ball_speed = [5, -5]  # speed in px per frame
        self.paddle1 = pg.Rect(10, 200, 20, 100)
        self.paddle2 = pg.Rect(770, 200, 20, 100)

    def _draw(self):
        pview.fill([0, 155, 155])
        # draw walls
        for wall in self.walls:
            pg.draw.rect(pview.screen, [0, 0, 0], T(wall))
        # draw ball
        pg.draw.rect(pview.screen, [0, 0, 0], T(self.ball))
        # draw paddles
        pg.draw.rect(pview.screen, [0, 0, 0], T(self.paddle1))
        pg.draw.rect(pview.screen, [0, 0, 0], T(self.paddle2))
        pg.display.flip()
        
        
if __name__ == "__main__":
    from constants import OUT_QUIT, OUT_FSCR
    pg.init()
    pview.set_mode((800, 600))
    clock = pg.time.Clock()
    scene = GameScene()
    while True:
        ms = clock.tick(20)
        outcome = controller.poll()  # get player input
        if outcome == OUT_QUIT:
            break
        elif outcome == OUT_FSCR:
            pview.toggle_fullscreen()

        next_scene_id, kwargs = scene.tick(ms) 
        pg.display.set_caption('game scene %.1f' % clock.get_fps())
