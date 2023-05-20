from typing import Any
import pygame as pg
WIDTH = 800
HEIGHT = 650
FPS = 120

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
when_flag_clicked = pg.transform.scale(pg.image.load("res/when_flag_clicked.png"),(200,50))
run_motor_a = pg.transform.scale(pg.image.load("res/run_motor_a.png"),(200,50))
stop_motor_a = pg.transform.scale(pg.image.load("res/stop_motor_a.png"),(200,50))
run_motor_a_backward = pg.transform.scale(pg.image.load("res/run_motor_a_backward.png"),(200,50))
run_motor_b = pg.transform.scale(pg.image.load("res/run_motor_b.png"),(200,50))
stop_motor_b = pg.transform.scale(pg.image.load("res/stop_motor_b.png"),(200,50))
run_motor_b_backward = pg.transform.scale(pg.image.load("res/run_motor_b_backward.png"),(200,50))
wait = pg.transform.scale(pg.image.load("res/wait.png"),(200,50))
stop_all = pg.transform.scale(pg.image.load("res/stop_all_motors.png"),(200,50))
import tkinter as tk

def get_number_input():
    # Create a new Tkinter window
    window = tk.Tk()

    # Create a label and entry widget for the user to input a number
    label = tk.Label(window, text="Введіть значення:")
    label.pack()
    entry = tk.Entry(window)
    entry.pack()

    # Create a button that will return the user's input when clicked
    def return_input():
        global res_tmp
        input_value = entry.get()
        window.destroy()
        res_tmp = input_value
        
        return input_value

    button = tk.Button(window, text="OK", command=return_input)
    button.pack()

    # Run the window in a loop until it is closed by the user
    window.mainloop()
class Block(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = run_motor_a
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = True
        self.text = "RM"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Starter(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = when_flag_clicked
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = False
        self.text = "RN"
    def set_active(self,v):
        self.activated = False
    def update(self):
        pass
    def __str__(self) -> str:
        return self.text
class Stop_Motor(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = stop_motor_a
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = True
        self.text = "SM"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Run_motor_a_backward(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = run_motor_a_backward
        self.rect = self.image.get_rect()
        self.rect.center =cord
        self.activated = False
        self.activatable = True
        self.text = "RMB"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Run_motor_b(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = run_motor_b
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = True
        self.text = "RMA"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Run_motor_b_backward(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = run_motor_b_backward
        self.rect = self.image.get_rect()
        self.rect.center =cord
        self.activated = False
        self.activatable = True
        self.text = "RMBA"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Stop_Motor_b(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = stop_motor_b
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = True
        self.text = "SMA"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Wait(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = wait
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = True
        self.text = "WT 100"
        self.tick = 0
        self.clicks = 0
        self.act_s = 0
    def set_active(self,v):
        self.activated = v
    def clicker(self):
        self.clicks+=1
        self.tick = 60
        if self.clicks >= 2:
            self.clicks = 0
            self.pos = self.rect.center
            get_number_input()
            global res_tmp
            try:
                res_tmp=int(res_tmp)
            except:
                res_tmp=100
            self.text = "WT " + str(res_tmp)
            self.rect.center = self.pos
            self.act_s = 10
    def update(self):
        if self.act_s > 0:
            self.act_s -=1
            self.rect.center = self.pos
        if self.tick > 0:
            self.tick-=1
            if self.tick == 0 and self.clicks > 0:
                self.clicks-=1
                if self.clicks > 0:
                    self.tick=60
        if self.activated and self.act_s == 0:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text
class Stop_all_motors(pg.sprite.Sprite):
    def __init__(self,cord=(WIDTH / 2, HEIGHT / 2)):
        pg.sprite.Sprite.__init__(self)
        self.image = stop_all
        self.rect = self.image.get_rect()
        self.rect.center = cord
        self.activated = False
        self.activatable = True
        self.text = "SAM"
    def set_active(self,v):
        self.activated = v
    def update(self):
        if self.activated:
            mp = pg.mouse.get_pos()
            self.rect.center = mp
    def __str__(self) -> str:
        return self.text