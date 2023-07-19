import pygame
import random
import sys

pygame.init()

pygame.font.init()

grid_size = 32

screen_x = grid_size*25
screen_y = grid_size*20

screen = pygame.display.set_mode((screen_x, screen_y))

pygame.display.set_caption('Heroes Game')

font_1 = "chalkduster.ttf"

# Player stats


# x, y
player_cords = [0, 0]
previous_x = 0
previous_y = 0

player_coins = [0]

# Image paths
tree_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\tree.png").convert()
rock_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\rock.png").convert()
coin_image_1 = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\coin.png").convert_alpha()
player_image = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\player.png").convert()
util_bar_image = pygame.image.load("C:\\Users\\braxt\\Desktop\\Desktop\\Coding\\python_game_1\\sprites\\util_bar.png").convert()


def draw_rect(cord_x, cord_y, length, width, color):
    pygame.draw.rect(screen, color, [cord_x*grid_size, cord_y*grid_size, length, width], 100)
    # pygame.draw.rect(screen, (0, random.randint(102, 204), random.randint(34, 68)), [x, y, length, width], 100)


def draw_image(cord_x, cord_y, image_path):
    screen.blit(image_path, (cord_x * grid_size, cord_y * grid_size))


def draw_text(font, font_size, text, color, cord_x, cord_y):
    text_font = pygame.font.SysFont(font, font_size)

    text_description = text_font.render(text, True, color)

    text_rect = text_description.get_rect()

    text_rect.bottomleft = (cord_x*grid_size, cord_y*grid_size)

    screen.blit(text_description, text_rect)


def draw_coin(cord_x, cord_y, value, used):

    if used != True:

        screen.blit(coin_image_1, (cord_x*grid_size, cord_y*grid_size))

        if player_cords[0] == cord_x and player_cords[1] == cord_y:

            player_coins[0] += value

            used = True


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


# Object maps
coin_map = [draw_coin(4, 4, 10, False)]


running = True

while running:

    # Background color
    screen.fill((0, 0, 0))

    # Draw grid
    for cord_x in range(0, int(screen_x / grid_size + 1)):
        for cord_y in range(0, int(screen_y / grid_size) + 1):
            draw_rect(cord_x, cord_y, grid_size, grid_size, (0, 153, 51))

    # Draw utils
    draw_image(0, 18, util_bar_image)
    draw_coin(4, 4, 10, False)

    # Text
    draw_text(font_1, 60, str(player_coins[0]), (255, 255, 255), 1.8, 19.7)

    # Draw player
    draw_image(player_cords[0], player_cords[1], player_image)

    # Draw obstacles
    draw_obstacle(1, 1, tree_image_1)
    draw_obstacle(4, 3, tree_image_1)
    draw_obstacle(7, 2, rock_image_1)

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
