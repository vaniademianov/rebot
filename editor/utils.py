import pygame
import math
import os
def get_sprites_at_point(group, point):
    sprites_at_point = []
    for sprite in group:
        rect = sprite.rect
        if rect.collidepoint(point):
            sprites_at_point.append(sprite)
    return sprites_at_point
def calc_dist(x1,y1,x2,y2):
   return pygame.math.Vector2(x1, y1).distance_to((x2, y2))
def calc_dist_rect(r1,r2):
   return pygame.math.Vector2(r1.x, r1.y).distance_to((r2.x, r2.y))

def get_nearest_sprite(group, sprite):
    closest_sprite = None
    closest_distance = float('inf')
    sprite_x, sprite_y = sprite.rect.center
    for other_sprite in group:
        if other_sprite != sprite:
            other_sprite_x, other_sprite_y = other_sprite.rect.center
            distance = math.sqrt((sprite_x - other_sprite_x)**2 + (sprite_y - other_sprite_y)**2)
            if distance < closest_distance:
                closest_sprite = other_sprite
                closest_distance = distance
    return closest_sprite
def get_nearest_sprite_by_dist(group, sprite, dist):
    closest_sprite = None
    closest_distance = float('inf')
    sprite_x, sprite_y = sprite.rect.center
    for other_sprite in group:
        if other_sprite != sprite:
            other_sprite_x, other_sprite_y = other_sprite.rect.center
            distance = math.sqrt((sprite_x - other_sprite_x)**2 + (sprite_y - other_sprite_y)**2)
            if distance < closest_distance and distance <= dist:
                closest_sprite = other_sprite
                closest_distance = distance
    return closest_sprite
def get_nearest_sprite_by_dist_(group, sprite, dist,checked):
    closest_sprite = None
    closest_distance = float('inf')
    sprite_x, sprite_y = sprite.rect.center
    for other_sprite in group:
        if other_sprite != sprite and other_sprite not in checked:
            other_sprite_x, other_sprite_y = other_sprite.rect.center
            distance = math.sqrt((sprite_x - other_sprite_x)**2 + (sprite_y - other_sprite_y)**2)
            if distance < closest_distance and distance <= dist:
                closest_sprite = other_sprite
                closest_distance = distance
    return closest_sprite
