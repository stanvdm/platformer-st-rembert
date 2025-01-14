import pygame, sys

from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.utils import load_image, load_images

class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Platformer")

        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height)) # , pygame.RESIZABLE)
        self.display = pygame.Surface((320, 180))
        self.clock = pygame.time.Clock()

        self.assets = {
            "dirt": load_images("tiles/dirt"),
            "player": load_image("entities/knight/idle/00.png")
        }

        self.tilemap = Tilemap(self)
        self.player = PhysicsEntity(self, (self.display.get_rect().width // 2, self.display.get_rect().height // 2 - 50), (10, 16))
        self.player_movement = [0, 0]
        self.scroll = pygame.Vector2(0, 0)
    
    def run(self):
        while True:
            # Render & game logic
            self.display.fill("lightblue")

            self.scroll.x += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll.x) / 60
            self.scroll.y += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll.y) / 60
            render_scroll = (int(self.scroll.x), int(self.scroll.y))

            self.tilemap.render(self.display, render_scroll)

            self.player.update(self.tilemap, (self.player_movement[1] - self.player_movement[0], 0))
            self.player.render(self.display, render_scroll)

            # Event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.VIDEORESIZE:
                    self.screen_width, self.screen_height = event.w, event.h
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = 1
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = 1
                    if event.key == pygame.K_UP:
                        self.player.vel.y = -3
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player_movement[0] = 0
                    if event.key == pygame.K_RIGHT:
                        self.player_movement[1] = 0

            pygame.transform.scale(self.display, self.screen.get_size(), self.screen)
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()