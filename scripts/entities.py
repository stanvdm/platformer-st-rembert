import pygame
from pygame import Vector2

from scripts.tilemap import Tilemap

class PhysicsEntity:
    def __init__(self, game, pos, size):
        self.game = game
        self.pos = Vector2(pos)
        self.size = size

        self.flip = False
        self.vel = Vector2(0, 0)
        self.collisions = {"up": False, "down": False, "left": False, "right": False}

    def rect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.size[0], self.size[1])

    def render(self, surf, offset=(0, 0)):
        img = pygame.transform.flip(self.game.assets["player"], self.flip, False)
        image_rect = img.get_rect()
        image_rect.center = self.rect().center
        surf.blit(img, (image_rect.x - offset[0], image_rect.y - offset[1]))

    def update(self, tilemap: Tilemap, movement = (0, 0)):
        self.collisions = {"up": False, "down": False, "left": False, "right": False}

        self.vel.y = min(5, self.vel.y + 0.1)

        frame_movement = (self.vel.x + movement[0], self.vel.y + movement[1])

        self.pos.x += frame_movement[0]
        entity_rect = self.rect()
        for tile_rect in tilemap.physics_rects_around(entity_rect.center):
            if entity_rect.colliderect(tile_rect):
                if frame_movement[0] > 0:
                    entity_rect.right = tile_rect.left
                    self.collisions["right"] = True
                if frame_movement[0] < 0:
                    entity_rect.left = tile_rect.right
                    self.collisions["left"] = True
                self.pos.x = entity_rect.x

        self.pos.y += frame_movement[1]
        entity_rect = self.rect()
        for tile_rect in tilemap.physics_rects_around(entity_rect.center):
            if entity_rect.colliderect(tile_rect):
                if frame_movement[1] > 0:
                    entity_rect.bottom = tile_rect.top
                    self.collisions["down"] = True
                if frame_movement[1] < 0:
                    entity_rect.top = tile_rect.bottom
                    self.collisions["up"] = True
                self.pos.y = entity_rect.y

        if movement[0] > 0:
            self.flip = False
        if movement[0] < 0:
            self.flip = True

        if self.collisions["up"] or self.collisions["down"]:
            self.vel.y = 0