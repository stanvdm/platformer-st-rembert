import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

class Tile:
    def __init__(self, tiletype, variant, pos):
        self.type = tiletype
        self.variant = variant
        self.x = pos[0]
        self.y = pos[1]
        
    def pos(self):
        return [self.x, self.y]

class Tilemap:
    def __init__(self, game, tile_size = 16):
        self.game = game
        self.tile_size = tile_size
        self.tilemap = {
            "7;4": Tile("dirt", 0, [7, 4]),
            "8;4": Tile("dirt", 0, [8, 4]),
            "7;5": Tile("dirt", 1, [7, 5]),
            "7;6": Tile("dirt", 1, [7, 6]),
            "7;7": Tile("dirt", 1, [7, 7]),
            "8;7": Tile("dirt", 0, [8, 7]),
            "9;7": Tile("dirt", 0, [9, 7]),
            "10;7": Tile("dirt", 0, [10, 7]),
            "8;8": Tile("dirt", 1, [8, 8]),
            "9;8": Tile("dirt", 1, [9, 8])
        }

    def physics_rects_around(self, pos):
        neighbors = []
        tile_pos = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            tile_key = f"{tile_pos[0] + offset[0]};{tile_pos[1] + offset[1]}"
            if tile_key in self.tilemap:
                rect = pygame.Rect(self.tilemap[tile_key].x * self.tile_size, self.tilemap[tile_key].y * self.tile_size, self.tile_size, self.tile_size)
                neighbors.append(rect)
        return neighbors

    def render(self, surf: pygame.Surface, offset = (0, 0)):
        for _, tile in self.tilemap.items():
            surf.blit(self.game.assets[tile.type][tile.variant], (tile.x * self.tile_size - offset[0], tile.y * self.tile_size - offset[1]))