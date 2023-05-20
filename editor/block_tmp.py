from typing import Any
import pygame as pg
WIDTH = 800
HEIGHT = 650
FPS = 120
import block
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
class Block(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.run_motor_a
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.activated = False
        self.parent = block.Block
        self.activatable = True
class Starter(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.when_flag_clicked
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.activated = False
        self.parent = block.Starter
        self.activatable = False
class Stop_Motor(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.stop_motor_a
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.activated = False
        self.parent = block.Stop_Motor
        self.activatable = True
class Run_motor_a_backward(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.run_motor_a_backward
        self.rect = self.image.get_rect()
        self.parent = block.Run_motor_a_backward
        self.rect.center = pos
        self.activated = False
        self.activatable = True
class Run_motor_b(pg.sprite.Sprite):
    def __init__(self, pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.run_motor_b
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.activated = False
        self.parent = block.Run_motor_b
        self.activatable = True
class Stop_Motor_b(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.stop_motor_b
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.activated = False
        self.parent = block.Stop_Motor_b
        self.activatable = True
class Run_motor_b_backward(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.run_motor_b_backward
        self.rect = self.image.get_rect()
        self.parent = block.Run_motor_b_backward
        self.rect.center = pos
        self.activated = False
        self.activatable = True
class Wait(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.wait
        self.rect = self.image.get_rect()
        self.parent = block.Wait
        self.rect.center = pos
        self.activated = False
        self.activatable = True
class Stop_all_motors(pg.sprite.Sprite):
    def __init__(self,pos):
        pg.sprite.Sprite.__init__(self)
        self.image = block.stop_all
        self.rect = self.image.get_rect()
        self.parent = block.Stop_all_motors
        self.rect.center = pos
        self.activated = False
        self.activatable = True