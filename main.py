import pygame
import random
import sys

from pygame import mixer

pygame.init()

pygame.font.init()

mixer.init()

grid_size = 32

screen_x = grid_size*25
screen_y = grid_size*20

screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption('Heroes Game')

font_1 = "chalkduster.ttf"

# Player stats
pickedUp = []
discovered = [bool]

# x, y
player_cords = [0, 0]
previous_x = 0
previous_y = 0

player_coins = [0]

obj_coins = []



# Image paths
mushroom_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\mushroom_1.png").convert_alpha()
flower_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\flower_1.png").convert_alpha()
flower_image_2 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\flower_2.png").convert_alpha()
bush_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\bush.png").convert()
grass_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\grass.png").convert()
dirt_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\dirt.png").convert()
tree_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\tree.png").convert()
rock_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\rock.png").convert()
coin_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\coin.png").convert_alpha()
player_image = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\player.png").convert()
util_bar_image = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\util_bar.png").convert()


class GenericObject:

    def __init__(self, cord_x, cord_y, value, image):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.value = value
        self.image = image

    def draw(self):
        screen.blit(self.image, (self.cord_x * grid_size, self.cord_y * grid_size))

    def collision(self):
        if player_cords[0] == self.cord_x and player_cords[1] == self.cord_y:

            player_coins[0] += self.value

    def remove(self):
        del self




def draw_rect(cord_x, cord_y, length, width, color):
    pygame.draw.rect(screen, color, [cord_x*grid_size, cord_y*grid_size, length, width], 300)
    # pygame.draw.rect(screen, (0, random.randint(102, 204), random.randint(34, 68)), [x, y, length, width], 100)


def draw_image(cord_x, cord_y, image_path):
    screen.blit(image_path, (cord_x * grid_size, cord_y * grid_size))


def draw_text(font, font_size, text, color, cord_x, cord_y):
    text_font = pygame.font.SysFont(font, font_size)

    text_description = text_font.render(text, True, color)

    text_rect = text_description.get_rect()

    text_rect.bottomleft = (cord_x*grid_size, cord_y*grid_size)

    screen.blit(text_description, text_rect)


def draw_coin(self, cord_x, cord_y, value, obj_num):

    appended = bool

    if appended != True:
        pickedUp.append(bool)

    if pickedUp[obj_num] != True:

        screen.blit(coin_image_1, (cord_x*grid_size, cord_y*grid_size))

        if player_cords[0] == cord_x and player_cords[1] == cord_y:

            player_coins[0] += value



def draw_obstacle(cord_x, cord_y, image_path):
    screen.blit(image_path, (cord_x*grid_size, cord_y*grid_size))

    if player_cords[0] == cord_x and player_cords[1] == cord_y and previous_x == cord_x and previous_y == cord_y + 1:

        player_cords[1] += 1

    elif player_cords[0] == cord_x and player_cords[1] == cord_y and previous_x == cord_x and previous_y == cord_y - 1:

        player_cords[1] -= 1

    elif player_cords[0] == cord_x and player_cords[1] == cord_y and previous_x == cord_x + 1 and previous_y == cord_y:

        player_cords[0] += 1

    elif player_cords[0] == cord_x and player_cords[1] == cord_y and previous_x == cord_x - 1 and previous_y == cord_y:

        player_cords[0] -= 1


obj_coins.append(
    GenericObject(2, 2, 10, coin_image_1)
)


# Object maps
# coin_map = [draw_coin(4, 4, 10)]

mixer.music.load("C:\\Users\\braxt\\Desktop\\Desktop\\Music Catalog\\My Music\\DIRT.mp3")

mixer.music.set_volume(0.5)

mixer.music.play()

running = True

while running:

    # Background color
    screen.fill((0, 0, 0))

    # Draw grid
    for cord_x in range(0, int(screen_x / grid_size + 1)):
        for cord_y in range(0, int(screen_y / grid_size) + 1):
            draw_image(cord_x, cord_y, grass_image_1)
            # draw_rect(cord_x, cord_y, grid_size, grid_size, (0, 153, 51))

    # Draw utils
    draw_image(0, 18, util_bar_image)
    # draw_coin(4, 4, 10, 0)
    # draw_coin(7, 8, 20, 1)

    for each in range(0, len(obj_coins)):
        obj_coins[each].draw()
        obj_coins[each].collision()
        obj_coins[each].remove()

    # Text
    draw_text(font_1, 60, str(player_coins[0]), (255, 255, 255), 1.8, 19.7)

    # Draw player
    draw_image(player_cords[0], player_cords[1], player_image)

    # Draw obstacles
    draw_obstacle(1, 1, bush_image_1)
    draw_obstacle(4, 3, bush_image_1)
    draw_obstacle(7, 2, bush_image_1)
    draw_obstacle(1, 8, flower_image_1)
    draw_obstacle(3, 6, flower_image_2)
    draw_obstacle(8, 8, mushroom_image_1)

    # Fog of war
    if discovered[0] != True:
        draw_rect(0, 10, 10 * grid_size, 8 * grid_size, (0, 0, 0))

    if 0 <= player_cords[0] <= 10 <= player_cords[1] <= 18:
        discovered[0] = True

    # Game Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and player_cords[0] > 0:
                previous_x = player_cords[0]
                previous_y = player_cords[1]
                player_cords[0] -= 1
            elif event.key == pygame.K_RIGHT and player_cords[0] < (screen_x/grid_size)-1:
                previous_x = player_cords[0]
                previous_y = player_cords[1]
                player_cords[0] += 1
            elif event.key == pygame.K_UP and player_cords[1] > 0:
                previous_x = player_cords[0]
                previous_y = player_cords[1]
                player_cords[1] -= 1
            elif event.key == pygame.K_DOWN and player_cords[1] < (screen_y/grid_size)-3:
                previous_x = player_cords[0]
                previous_y = player_cords[1]
                player_cords[1] += 1

    pygame.display.update()
