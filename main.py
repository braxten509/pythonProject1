import pygame
import global_vars
import objects

# ADD MAP EDITOR BUTTONS NEXT AND SAVE TO FILE - THEN READ FROM FILE

from pygame import mixer

pygame.init()

pygame.font.init()

mixer.init()

pygame.display.set_caption('Heroes Game')

objects.play_music("sounds\\music\\DIRT.mp3", 0.5)

running = True

while running:

    # Background color
    global_vars.SCREEN.fill((0, 0, 0))

    # Draw grid
    for cord_x_grid in range(0, int(global_vars.SCREEN_X / global_vars.GRID_SIZE + 1)):
        for cord_y_grid in range(0, int(global_vars.SCREEN_Y / global_vars.GRID_SIZE) + 1):
            objects.draw_image(cord_x_grid, cord_y_grid, global_vars.GRASS_ICON_1)

    # Draw utils
    objects.draw_image(0, 18, global_vars.UTIL_BAR_ICON_1)

    # Draw Objects (iterating from last to first. len(object_array) has a "- 1" because there is no
    # object_array[5] in an array with 5 values. And the ending value is -1 as it is not included
    # in what ends up being printed)
    for each in range(len(global_vars.object_array) - 1, -1, -1):
        global_vars.object_array[each].draw()

    # Text
    objects.draw_text(global_vars.FONT_1, 60, str(global_vars.player_coins[0]), (255, 255, 255), 1.8, 19.7)

    # Draw player
    objects.draw_image(global_vars.player_cords[0], global_vars.player_cords[1], global_vars.PLAYER_ICON_1)

    # Game Events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and global_vars.player_cords[0] > 0:
                global_vars.previous_x = global_vars.player_cords[0]
                global_vars.previous_y = global_vars.player_cords[1]
                global_vars.player_cords[0] -= 1
            elif event.key == pygame.K_RIGHT and global_vars.player_cords[0] < (global_vars.SCREEN_X / global_vars.GRID_SIZE)-1:
                global_vars.previous_x = global_vars.player_cords[0]
                global_vars.previous_y = global_vars.player_cords[1]
                global_vars.player_cords[0] += 1
            elif event.key == pygame.K_UP and global_vars.player_cords[1] > 0:
                global_vars.previous_x = global_vars.player_cords[0]
                global_vars.previous_y = global_vars.player_cords[1]
                global_vars.player_cords[1] -= 1
            elif event.key == pygame.K_DOWN and global_vars.player_cords[1] < (global_vars.SCREEN_Y / global_vars.GRID_SIZE)-3:
                global_vars.previous_x = global_vars.player_cords[0]
                global_vars.previous_y = global_vars.player_cords[1]
                global_vars.player_cords[1] += 1

    pygame.display.update()
