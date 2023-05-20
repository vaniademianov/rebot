from typing import Any
import pygame
import random


import utils as u
from block import *
WIDTH = 800
HEIGHT = 650
FPS = 120
import bluetooth
import os
address = "00:22:09:01:29:5c"
import block_tmp
# create a Bluetooth socket and connect to the Arduino
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((address, 1))
runn = pg.transform.scale(pg.image.load("res/runn.png"),(200,50))
def send(text):
    sock.send(text+"*")
send("ST")
print("sent")
def receive():
    response = ""
    data = sock.recv(1024)
    response += data.decode()
    return response.strip()
# print the response from the Arduino
response = receive()
print("Received: " + response)
if response == "ST":
    print("P.R.O.J.E.C.T.O.R. is running")

# close the Bluetooth socket
def txt(obj):
    # os.system("cls")
    string = ""
    for a in obj:
        string+=str(a)+";"
        print(str(a)+";")
    send(string)
class Button(pygame.sprite.Sprite):
    def __init__(self,coords):
        super().__init__()
        
        self.image = runn
        self.rect = self.image.get_rect()
        self.rect.center = coords
    def onclick(self):
        send("ACT")
    def update(self) -> None:
        pass

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def rebuild(sprite):
    nearst = u.get_nearest_sprite_by_dist_(all_sprites,sprite,100,[])
    lst = [sprite]
    while nearst != None:
        lst.append(nearst)
        nearst = u.get_nearest_sprite_by_dist_(all_sprites,nearst,100,lst)
    return lst

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("By RemoteAccess01 <3")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
blocks_tmp = pygame.sprite.Group()
toper = Starter()
all_sprites.add(toper)
# player = Block()
# all_sprites.add(player)
# player = Stop_Motor()
# all_sprites.add(player)
# player = Run_motor_a_backward()
# all_sprites.add(player)
bl = block_tmp.Block((110,50))
blocks_tmp.add(bl)
bl = block_tmp.Stop_Motor((110,120))
blocks_tmp.add(bl)
bl = block_tmp.Run_motor_a_backward((110,190))
blocks_tmp.add(bl)
bl = block_tmp.Run_motor_b((110,260))
blocks_tmp.add(bl)
bl = block_tmp.Stop_Motor_b((110,330))
blocks_tmp.add(bl)
bl = block_tmp.Run_motor_b_backward((110,400))
blocks_tmp.add(bl)


bl = block_tmp.Wait((110,470))
blocks_tmp.add(bl)
bl = block_tmp.Stop_all_motors((110,540))
blocks_tmp.add(bl)
buttons = pygame.sprite.Group()
btn = Button((WIDTH-100,50))
buttons.add(btn)
clicked = False
# Цикл игры
act = None

code = []
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            
            obj = u.get_sprites_at_point(all_sprites,pos)
            if len(obj) > 0 and not clicked:
                for obj in obj:
                    if obj.activatable:
                        if type(obj) == Wait:
                            obj.clicker()
                        obj.set_active(True)
                        act = obj
                        clicked = True
                        break
                
            obj = u.get_sprites_at_point(blocks_tmp,pos)
            if len(obj) > 0:
                obj = obj[0]
                new = obj.parent(pos)
                all_sprites.add(new)
                if new.activatable:
                    new.set_active(True)
                    act = new
                    clicked = True

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            # get a list of all sprites that are under the mouse cursor
            if clicked:
                if act.rect.x < 170:
                    act.kill()
                act.set_active(False)
                nearst = u.get_nearest_sprite(all_sprites,act)

                if u.calc_dist_rect(nearst.rect,act.rect) < 110:
    
                    act.rect.topright = (nearst.rect.bottomright[0], nearst.rect.bottom)
                code = rebuild(toper)
                txt(code)
                clicked = False
                act = None
            else:
                obj = u.get_sprites_at_point(buttons,pos)
                if len(obj) > 0:
                    obj= obj[0]
                    obj.onclick()
    # Обновление
    all_sprites.update()
    buttons.update()
    # Рендеринг
    screen.fill(BLACK)
    pygame.draw.line(screen, RED, (170,0), (175,HEIGHT), 2)
    all_sprites.draw(screen)
    blocks_tmp.draw(screen)
    buttons.draw(screen)
    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
sock.close()
pygame.quit()