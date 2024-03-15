import pygame
from settings import *
from tile import Tile

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        #sprite groups
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
    
        #sprite setup
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(WORLD_MAP):
                x = col_index * TITELSIZE
                y = row_index * TITELSIZE  
                if col == "x":
                    Title((x,y),[self.visible_sprites])
                    
    def run(self):
        
        #run the game
        pass