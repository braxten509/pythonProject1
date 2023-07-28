import pygame
import random
import sys

# ADD MAP EDITOR BUTTONS NEXT AND SAVE TO FILE - THEN READ FROM FILE

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

discovered = bool

# x, y
player_cords = [0, 0]
previous_x = 0
previous_y = 0

player_coins = [0]

object_array = []


# Image paths
mushroom_image_1 = pygame.image.load("sprites\\mushroom_1.png").convert_alpha()
flower_image_1 = pygame.image.load("sprites\\flower_1.png").convert_alpha()
flower_image_2 = pygame.image.load("sprites\\flower_2.png").convert_alpha()
bush_image_1 = pygame.image.load("sprites\\bush.png").convert_alpha()
grass_image_1 = pygame.image.load("sprites\\grass.png").convert_alpha()
dirt_image_1 = pygame.image.load("sprites\\dirt.png").convert_alpha()
tree_image_1 = pygame.image.load("sprites\\tree.png").convert_alpha()
rock_image_1 = pygame.image.load("sprites\\rock.png").convert_alpha()
coin_image_1 = pygame.image.load("sprites\\coin.png").convert_alpha()
player_image = pygame.image.load("sprites\\player.png").convert_alpha()
util_bar_image = pygame.image.load("sprites\\util_bar.png").convert_alpha()


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


class Coin:

    def __init__(self, cord_x, cord_y, value):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.value = value

    # The __eq__ method will return true when compared with anything if this AND that AND that are all true.
    # For example if compared with another "Coin" it will NOT compare if they're the same object ID (like default),
    # but will compare if cord_x, cord_y, and value in both objects are the same. If yes, then it returns true.
    def __eq__(self, other):
        return self.cord_x == other.cord_x and self.cord_y == other.cord_y and self.value == other.value

    # When printed, it will output "(1, 3, 10)" instead of "<__main__.Coin object at 0x000001F51B3313A0>"
    def __repr__(self):
        return f"`{self.cord_x, self.cord_y, self.value}`"

    def draw(self):

        screen.blit(coin_image_1, (self.cord_x*grid_size, self.cord_y*grid_size))

        if player_cords[0] == self.cord_x and player_cords[1] == self.cord_y:

            player_coins[0] += self.value

            # So now this is removing an object with this string value in an array INSTEAD of an actual object!
            object_array.remove(self)


class Obstacle:

    def __init__(self, cord_x, cord_y, image_path):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.image_path = image_path

    def draw(self):
        screen.blit(self.image_path, (self.cord_x*grid_size, self.cord_y*grid_size))

        if player_cords[0] == self.cord_x and player_cords[1] == self.cord_y and previous_x == self.cord_x and previous_y == self.cord_y + 1:

            player_cords[1] += 1

        elif player_cords[0] == self.cord_x and player_cords[1] == self.cord_y and previous_x == self.cord_x and previous_y == self.cord_y - 1:

            player_cords[1] -= 1

        elif player_cords[0] == self.cord_x and player_cords[1] == self.cord_y and previous_x == self.cord_x + 1 and previous_y == self.cord_y:

            player_cords[0] += 1

        elif player_cords[0] == self.cord_x and player_cords[1] == self.cord_y and previous_x == self.cord_x - 1 and previous_y == self.cord_y:

            player_cords[0] -= 1


class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clicked = False
        self.rect = pygame.draw.rect(screen, self.color, [self.x*grid_size, self.y*grid_size,
                                                          self.width, self.height], 300)

    def draw(self):
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        pygame.draw.rect(screen, self.color, [self.x * grid_size, self.y * grid_size,
                                              self.width, self.height], 300)

        return action


object_array = [
    Obstacle(2, 2, bush_image_1),
    Obstacle(4, 4, mushroom_image_1),
    Coin(3, 3, 10),
    Coin(5, 3, 10)
]

mixer.music.load("C:\\Users\\braxt\\Desktop\\Desktop\\Music Catalog\\My Music\\DIRT.mp3")

mixer.music.set_volume(0.5)

mixer.music.play()

running = True

while running:

    # Background color
    screen.fill((0, 0, 0))

    # Draw grid
    for cord_x_grid in range(0, int(screen_x / grid_size + 1)):
        for cord_y_grid in range(0, int(screen_y / grid_size) + 1):
            draw_image(cord_x_grid, cord_y_grid, grass_image_1)

    # Draw utils
    draw_image(0, 18, util_bar_image)

    # Draw Objects (iterating from last to first. len(object_array) has a "- 1" because there is no
    # object_array[5] in an array with 5 values. And the ending value is -1 as it is not included
    # in what ends up being printed)
    for each in range(len(object_array) - 1, -1, -1):
        object_array[each].draw()

    # Text
    draw_text(font_1, 60, str(player_coins[0]), (255, 255, 255), 1.8, 19.7)

    # Draw player
    draw_image(player_cords[0], player_cords[1], player_image)

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
