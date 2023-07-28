import pygame
import global_vars

from pygame import mixer

pygame.init()
pygame.font.init()
mixer.init()


def play_music(path, volume):
    mixer.music.load(path)

    mixer.music.set_volume(volume)

    mixer.music.play()


def draw_rect(cord_x, cord_y, length, width, color):
    pygame.draw.rect(global_vars.SCREEN, color, [cord_x*global_vars.GRID_SIZE, cord_y*global_vars.GRID_SIZE, length, width], 300)
    # pygame.draw.rect(screen, (0, random.randint(102, 204), random.randint(34, 68)), [x, y, length, width], 100)


def draw_image(cord_x, cord_y, image_path):
    global_vars.SCREEN.blit(image_path, (cord_x * global_vars.GRID_SIZE, cord_y * global_vars.GRID_SIZE))


def draw_text(font, font_size, text, color, cord_x, cord_y):
    text_font = pygame.font.SysFont(font, font_size)

    text_description = text_font.render(text, True, color)

    text_rect = text_description.get_rect()

    text_rect.bottomleft = (cord_x*global_vars.GRID_SIZE, cord_y*global_vars.GRID_SIZE)

    global_vars.SCREEN.blit(text_description, text_rect)


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

        global_vars.SCREEN.blit(global_vars.COIN_ICON_1, (self.cord_x*global_vars.GRID_SIZE, self.cord_y*global_vars.GRID_SIZE))

        if global_vars.player_cords[0] == self.cord_x and global_vars.player_cords[1] == self.cord_y:

            global_vars.player_coins[0] += self.value

            # So now this is removing an object with this string value in an array INSTEAD of an actual object!
            global_vars.object_array.remove(self)


class Obstacle:

    def __init__(self, cord_x, cord_y, image_path):
        self.cord_x = cord_x
        self.cord_y = cord_y
        self.image_path = image_path

    def draw(self):
        global_vars.SCREEN.blit(self.image_path, (self.cord_x*global_vars.GRID_SIZE, self.cord_y*global_vars.GRID_SIZE))

        if global_vars.player_cords[0] == self.cord_x and global_vars.player_cords[1] == self.cord_y and global_vars.previous_x == self.cord_x\
                and global_vars.previous_y == self.cord_y + 1:

            global_vars.player_cords[1] += 1

        elif global_vars.player_cords[0] == self.cord_x and global_vars.player_cords[1] == self.cord_y and global_vars.previous_x == self.cord_x\
                and global_vars.previous_y == self.cord_y - 1:

            global_vars.player_cords[1] -= 1

        elif global_vars.player_cords[0] == self.cord_x and global_vars.player_cords[1] == self.cord_y and global_vars.previous_x == self.cord_x\
                + 1 and global_vars.previous_y == self.cord_y:

            global_vars.player_cords[0] += 1

        elif global_vars.player_cords[0] == self.cord_x and global_vars.player_cords[1] == self.cord_y and global_vars.previous_x == self.cord_x\
                - 1 and global_vars.previous_y == self.cord_y:

            global_vars.player_cords[0] -= 1


class Button:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.clicked = False
        self.rect = pygame.draw.rect(global_vars.SCREEN, self.color, [self.x*global_vars.GRID_SIZE, self.y*global_vars.GRID_SIZE,
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

        pygame.draw.rect(global_vars.SCREEN, self.color, [self.x * global_vars.GRID_SIZE, self.y * global_vars.GRID_SIZE,
                                              self.width, self.height], 300)

        return action
