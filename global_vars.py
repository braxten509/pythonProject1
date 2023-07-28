import pygame
import objects

pygame.init()

GRID_SIZE = 32

SCREEN_X = GRID_SIZE*25
SCREEN_Y = GRID_SIZE*20

SCREEN = pygame.display.set_mode((SCREEN_X, SCREEN_Y))

FONT_1 = "chalkduster.ttf"

MUSHROOM_ICON_1 = pygame.image.load("sprites\\mushroom_1.png").convert_alpha()
FLOWER_ICON_1 = pygame.image.load("sprites\\flower_1.png").convert_alpha()
FLOWER_ICON_2 = pygame.image.load("sprites\\flower_2.png").convert_alpha()
BUSH_ICON_1 = pygame.image.load("sprites\\bush.png").convert_alpha()
GRASS_ICON_1 = pygame.image.load("sprites\\grass.png").convert_alpha()
DIRT_ICON_1 = pygame.image.load("sprites\\dirt.png").convert_alpha()
TREE_ICON_1 = pygame.image.load("sprites\\tree.png").convert_alpha()
ROCK_ICON_1 = pygame.image.load("sprites\\rock.png").convert_alpha()
COIN_ICON_1 = pygame.image.load("sprites\\coin.png").convert_alpha()
PLAYER_ICON_1 = pygame.image.load("sprites\\player.png").convert_alpha()
UTIL_BAR_ICON_1 = pygame.image.load("sprites\\util_bar.png").convert_alpha()

# Game map
object_array = [
    objects.Obstacle(2, 2, BUSH_ICON_1),
    objects.Obstacle(4, 4, MUSHROOM_ICON_1),
    objects.Coin(3, 3, 10),
    objects.Coin(5, 3, 10)
]

# x, y
player_cords = [0, 0]
previous_x = 0
previous_y = 0

player_coins = [0]
