import pygame
import os
import random

# config
width = 500
height = 500
lines = 21
columns = 10
playtime = 0.0
FPS = 35
pixel = 20
init_fall_speed = 0.15
offset_x = 150
offset_y = 80

# screen blit adjustments
offset_y_2 = 40
left_dist = 120
right_dist = 30

landed =\
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
c_blue = \
    [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0], [0, 1, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 0, 0]]]
c_dblue = \
    [[[0, 0, 0, 0, 0], [0, 2, 2, 2, 0], [0, 0, 0, 2, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 2, 0, 0], [0, 0, 2, 0, 0], [0, 2, 2, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 2, 0, 0, 0], [0, 2, 2, 2, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 2, 2, 0, 0], [0, 2, 0, 0, 0], [0, 2, 0, 0, 0], [0, 0, 0, 0, 0]]]
c_green = \
    [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 3, 3, 0], [0, 3, 3, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 3, 0, 0, 0], [0, 3, 3, 0, 0], [0, 0, 3, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 3, 3, 0], [0, 3, 3, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 3, 0, 0, 0], [0, 3, 3, 0, 0], [0, 0, 3, 0, 0]]]
c_orange = [[[0, 0, 0, 0, 0], [0, 4, 4, 4, 0], [0, 4, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 4, 4, 0, 0], [0, 0, 4, 0, 0], [0, 0, 4, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 4, 0], [0, 4, 4, 4, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 4, 0, 0, 0], [0, 4, 0, 0, 0], [0, 4, 4, 0, 0], [0, 0, 0, 0, 0]]]
c_purple = \
    [[[0, 0, 0, 0, 0], [0, 0, 5, 0, 0], [0, 5, 5, 5, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 5, 0, 0], [0, 0, 5, 5, 0], [0, 0, 5, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 5, 5, 5, 0], [0, 0, 5, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 5, 0, 0], [0, 5, 5, 0, 0], [0, 0, 5, 0, 0], [0, 0, 0, 0, 0]]]
c_red = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 6, 6, 0, 0], [0, 0, 6, 6, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 6, 0, 0], [0, 6, 6, 0, 0], [0, 6, 0, 0, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 6, 6, 0, 0], [0, 0, 6, 6, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 6, 0, 0], [0, 6, 6, 0, 0], [0, 6, 0, 0, 0], [0, 0, 0, 0, 0]]]
c_yellow = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 7, 7, 0, 0], [0, 7, 7, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 7, 7, 0, 0], [0, 7, 7, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 7, 7, 0, 0], [0, 7, 7, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 7, 7, 0, 0], [0, 7, 7, 0, 0], [0, 0, 0, 0, 0]]]
c_blue2 = \
    [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [8, 8, 8, 8, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 8, 0, 0, 0], [0, 8, 0, 0, 0], [0, 8, 0, 0, 0], [0, 8, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [8, 8, 8, 8, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 8, 0, 0], [0, 0, 8, 0, 0], [0, 0, 8, 0, 0], [0, 0, 8, 0, 0]]]
c_dblue2 = \
    [[[0, 0, 0, 0, 0], [0, 9, 9, 9, 0], [0, 0, 0, 9, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 9, 0, 0], [0, 0, 9, 0, 0], [0, 9, 9, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 9, 0, 0, 0], [0, 9, 9, 9, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 9, 9, 0, 0], [0, 9, 0, 0, 0], [0, 9, 0, 0, 0], [0, 0, 0, 0, 0]]]
c_green2 = \
    [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 10, 10, 0], [0, 10, 10, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 10, 0, 0, 0], [0, 10, 10, 0, 0], [0, 0, 10, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 10, 10, 0], [0, 10, 10, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 10, 0, 0, 0], [0, 10, 10, 0, 0], [0, 0, 10, 0, 0]]]
c_orange2 = [[[0, 0, 0, 0, 0], [0, 11, 11, 11, 0], [0, 11, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 11, 11, 0, 0], [0, 0, 11, 0, 0], [0, 0, 11, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 11, 0], [0, 11, 11, 11, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 11, 0, 0, 0], [0, 11, 0, 0, 0], [0, 11, 11, 0, 0], [0, 0, 0, 0, 0]]]
c_purple2 = \
    [[[0, 0, 0, 0, 0], [0, 0, 12, 0, 0], [0, 12, 12, 12, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 12, 0, 0], [0, 0, 12, 12, 0], [0, 0, 12, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 12, 12, 12, 0], [0, 0, 12, 0, 0], [0, 0, 0, 0, 0]],
     [[0, 0, 0, 0, 0], [0, 0, 12, 0, 0], [0, 12, 12, 0, 0], [0, 0, 12, 0, 0], [0, 0, 0, 0, 0]]]
c_red2 = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 13, 13, 0, 0], [0, 0, 13, 13, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 13, 0, 0], [0, 13, 13, 0, 0], [0, 13, 0, 0, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 13, 13, 0, 0], [0, 0, 13, 13, 0], [0, 0, 0, 0, 0]],
         [[0, 0, 0, 0, 0], [0, 0, 13, 0, 0], [0, 13, 13, 0, 0], [0, 13, 0, 0, 0], [0, 0, 0, 0, 0]]]
c_yellow2 = [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 14, 14, 0, 0], [0, 14, 14, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 14, 14, 0, 0], [0, 14, 14, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 14, 14, 0, 0], [0, 14, 14, 0, 0], [0, 0, 0, 0, 0]],
            [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 14, 14, 0, 0], [0, 14, 14, 0, 0], [0, 0, 0, 0, 0]]]

# converts the 2D array to list of positions
# eliminates 0s for no interruptions
def convert_block(block, bLeft, bTop):
    converted = []
    for i, row in enumerate(block):
        for j, column in enumerate(row):
            if column > 0:
                converted.append((j + bLeft, i + bTop))
    for i, pos in enumerate(converted):
        converted[i] = (pos[0] - 2, pos[1] - 4)
    return converted


def check_lost(block_pos):
    for pos in block_pos:
        if pos[1] <= 1:
            return True
        else:
            return False


def new_block():
    num = random.randrange(1, 8)
    if num == 1:
        return c_blue
    elif num == 2:
        return c_dblue
    elif num == 3:
        return c_green
    elif num == 4:
        return c_orange
    elif num == 5:
        return c_purple
    elif num == 6:
        return c_red
    elif num == 7:
        return c_yellow

def new_block2():
    num = random.randrange(8, 15)
    if num == 8:
        return c_blue2
    elif num == 9:
        return c_dblue2
    elif num == 10:
        return c_green2
    elif num == 11:
        return c_orange2
    elif num == 12:
        return c_purple2
    elif num == 13:
        return c_red2
    elif num == 14:
        return c_yellow2


def rotate(block_type, rotate_val):
    if rotate_val >= len(block_type):
        rotate_val = 0
    return block_type[rotate_val], rotate_val


class Game(object):

    def __init__(self):
        # setup python objects, load images, declare surfaces
        pygame.init()
        folder = "data"
        pygame.mixer.music.load(os.path.join(folder, "theme.ogg"))
        pygame.mixer.music.play(-1, 0.0)
        self.clock = pygame.time.Clock()
        self.blue = pygame.image.load(os.path.join(folder, "b.png"))
        self.dblue = pygame.image.load(os.path.join(folder, "d.png"))
        self.green = pygame.image.load(os.path.join(folder, "g.png"))
        self.orange = pygame.image.load(os.path.join(folder, "o.png"))
        self.purple = pygame.image.load(os.path.join(folder, "p.png"))
        self.red = pygame.image.load(os.path.join(folder, "r.png"))
        self.yellow = pygame.image.load(os.path.join(folder, "y.png"))
        self.blue2 = pygame.image.load(os.path.join(folder, "b2.png"))
        self.dblue2 = pygame.image.load(os.path.join(folder, "d2.png"))
        self.green2 = pygame.image.load(os.path.join(folder, "g2.png"))
        self.orange2 = pygame.image.load(os.path.join(folder, "o2.png"))
        self.purple2 = pygame.image.load(os.path.join(folder, "p2.png"))
        self.red2 = pygame.image.load(os.path.join(folder, "r2.png"))
        self.yellow2 = pygame.image.load(os.path.join(folder, "y2.png"))
        self.grid_block = pygame.image.load(os.path.join(folder, "gridpiece.png"))  # 20 x 20
        self.background = pygame.image.load(os.path.join(folder, "grid.png"))  # columns * pixel, lines * pixel
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

        # setup surfaces for refreshing
        self.block_cover = pygame.Surface((80, 80))  # refresh next block
        self.pause_cover = pygame.Surface((120, 30))
        self.wipe_text = pygame.Surface((90, 50))  # refresh score
        self.wipe_surf = pygame.Surface((self.screen.get_size()))  # wipe_surf = pausing, wipe_surf_complete erases entire screen
        self.wipe_surf_complete = pygame.Surface((self.screen.get_size()))  # wipe_surf = pausing, wipe_surf_complete erases entire screen
        self.end_screen = pygame.Surface((self.background.get_size()))

        # fill Surfaces
        self.block_cover.fill((20, 0, 0))
        self.pause_cover.fill((0, 0, 0))
        self.wipe_text.fill((0, 0, 0))
        self.wipe_surf.fill((0, 0, 0))
        self.wipe_surf_complete.fill((0, 0, 0))
        self.end_screen.fill((0, 0, 0))

        # colorkey / alpha
        self.wipe_surf.set_alpha(100)
        self.end_screen.set_alpha(100)

        # converting Surfaces
        self.blue = self.blue.convert()
        self.dblue = self.dblue.convert()
        self.green = self.green.convert()
        self.orange = self.orange.convert()
        self.purple = self.purple.convert()
        self.red = self.red.convert()
        self.yellow = self.yellow.convert()
        self.grid_block = self.grid_block.convert()
        self.block_cover = self.block_cover.convert()
        self.pause_cover = self.pause_cover.convert()
        self.background = self.background.convert()
        self.wipe_text = self.wipe_text.convert()
        self.wipe_surf.convert_alpha()
        self.wipe_surf_complete = self.wipe_surf_complete.convert()
        self.end_screen = self.end_screen.convert_alpha()


        # num lines, num cols
        self.lines = len(landed)
        self.col = len(landed[0])

        # title of window
        pygame.display.set_caption("Tetris!")

    def run(self):
        #holding
        font = pygame.font.SysFont(None, 25)
        hold_block_type = None
        can_hold = True
        hold_font = font.render("HOLD", True, (255, 255, 255))
        # pause
        pause_font = font.render("PAUSED", True, (255, 255, 255))
        paused = False
        # score
        score = 0
        score_diff = 0
        #level
        level = 1
        level_font = font.render("LEVEL: %d" % level, True, (255, 255, 255))

        #intervals
        last_pressed_down = 0
        last_pressed_side = 0
        last_fall = 0
        last_pressed_down2 = 0
        last_pressed_side2 = 0
        last_fall2 = 0
        long_interval = 600
        interval = 65
        down_interval = 90

        #block data
        movable = False
        movable2 = False
        clear = False
        change_piece = False
        change_piece2 = False
        next_block_type = new_block()
        block_type = new_block()
        next_block_type2 = new_block2()
        block_type2 = new_block2()
        speed_x = 0
        speed_y = 0
        rotate_val = 0
        speed_x2 = 0
        speed_y2 = 0
        rotate_val2 = 0
        block, rotate_val = rotate(block_type, rotate_val)
        block2, rotate_val2 = rotate(block_type2, rotate_val2)
        temp_left = 5
        temp_top = 2
        b_left = 5
        b_top = 2
        temp_left2 = 5
        temp_top2 = 2
        b_left2 = 5
        b_top2 = 2

        # level data
        mainloop = 1
        fall_time = 0
        fall_speed = init_fall_speed - (level * 0.02)
        fall_time2 = 0
        no_down = False  # stops going down thru blocks when landed
        no_down2 = False

        #main loop
        while mainloop:
            score_font = font.render("SCORE: %d" % score, True, (255, 255, 255))
            last_pressed_down += self.clock.get_time()
            last_pressed_side += self.clock.get_time()
            fall_time += self.clock.get_time()
            last_pressed_down2 += self.clock.get_time()
            last_pressed_side2 += self.clock.get_time()
            fall_time2 += self.clock.get_time()
            self.clock.tick_busy_loop(FPS)

            # level up
            if score_diff >= 50:
                level += 1
                score_diff = score
                level_font = font.render("LEVEL: %d" % level, True, (255, 255, 255))

            # let block fall with interval
            if fall_time / 1000.0 > fall_speed and not paused:
                fall_time = 0
                b_top += 1
                if not self.can_move(block, b_left, b_top):
                    last_fall += self.clock.get_time()
                    no_down = True
                    if last_fall >= down_interval:
                        last_fall = 0
                        change_piece = True
                    b_top -= 1
                elif self.can_move(block, b_left, b_top):
                    no_down = False
                    last_fall = 0

            if fall_time2 / 1000.0 > fall_speed and not paused:
                fall_time2 = 0
                b_top2 += 1
                if not self.can_move(block2, b_left2, b_top2):
                    last_fall2 += self.clock.get_time()
                    no_down2 = True
                    if last_fall2 >= down_interval:
                        last_fall2 = 0
                        change_piece2 = True
                    b_top2 -= 1
                elif self.can_move(block2, b_left2, b_top2):
                    no_down2 = False
                    last_fall2 = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame window closed by user
                    mainloop = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False
                    elif event.key == pygame.K_DOWN:
                        speed_y = 1
                    elif event.key == pygame.K_LEFT:
                        speed_x = -1
                    elif event.key == pygame.K_RIGHT:
                        speed_x = 1
                    elif event.key == pygame.K_UP:
                        block, rotate_val, b_left = self.can_rotate(block, block_type, b_left, b_top, rotate_val)
                    elif event.key == pygame.K_SPACE:
                        change_piece, b_left, b_top, speed_x, speed_y = self.drop(block, b_left, b_top)
                    elif event.key == pygame.K_s:
                        speed_y2 = 1
                    elif event.key == pygame.K_a:
                        speed_x2 = -1
                    elif event.key == pygame.K_d:
                        speed_x2 = 1
                    elif event.key == pygame.K_w:
                        block2, rotate_val2, b_left2 = self.can_rotate(block2, block_type2, b_left2, b_top2, rotate_val2)
                    elif event.key == pygame.K_SPACE:
                        change_piece2, b_left2, b_top2, speed_x2, speed_y2 = self.drop(block2, b_left2, b_top2)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_p:
                        if not paused:
                            pygame.mixer.music.stop()
                            self.screen.blit(self.wipe_surf, (0, 0))
                            speed_x = 0
                            speed_y = 0
                            last_pressed_down = 0
                            last_pressed_side = 0
                            speed_x2 = 0
                            speed_y2 = 0
                            last_pressed_down2 = 0
                            last_pressed_side2 = 0
                            paused = True
                            self.screen.blit(pause_font, (offset_x + 60, 30))
                        else:
                            pygame.mixer.music.play(-1, 0.0)
                            paused = False
                            self.screen.blit(self.background, (offset_x, offset_y))
                            self.screen.blit(score_font, (offset_x + columns*pixel + right_dist, offset_y))
                            self.screen.blit(level_font, (offset_x + columns*pixel + right_dist, offset_y + offset_y_2))
                            self.draw_landed()
                            self.draw_block(block, b_left, b_top)
                            self.draw_block2(block, b_left2, b_top2)
                            self.screen.blit(self.pause_cover, (offset_x + 60, 30))
                            pygame.display.flip()
                    elif event.key == pygame.K_c:
                        speed_x = 0
                        speed_y = 0
                        if can_hold:
                            if hold_block_type:
                                temp_block_type = block_type
                                block_type = hold_block_type
                                hold_block_type = temp_block_type
                                rotate_val = 0
                                block, rotate_val = rotate(block_type, rotate_val)
                                b_left = 5
                                b_top = 2
                                temp_top = 2
                                temp_left = 5
                                change_piece = False
                            else:
                                hold_block_type = block_type
                                block_type = new_block()
                                rotate_val = 0
                                block, rotate_val = rotate(block_type, rotate_val)
                                b_left = 5
                                b_top = 2
                                temp_top = 2
                                temp_left = 5
                                change_piece = False
                        can_hold = False
                    # elif event.key == pygame.K_c:
                    #     speed_x2 = 0
                    #     speed_y2 = 0
                    #     if can_hold:
                    #         if hold_block_type:
                    #             temp_block_type = block_type
                    #             block_type = hold_block_type
                    #             hold_block_type = temp_block_type
                    #             rotate_val = 0
                    #             block, rotate_val = rotate(block_type, rotate_val)
                    #             b_left = 5
                    #             b_top = 2
                    #             temp_top = 2
                    #             temp_left = 5
                    #             change_piece = False
                    #         else:
                    #             hold_block_type = block_type
                    #             block_type = new_block()
                    #             rotate_val = 0
                    #             block, rotate_val = rotate(block_type, rotate_val)
                    #             b_left = 5
                    #             b_top = 2
                    #             temp_top = 2
                    #             temp_left = 5
                    #             change_piece = False
                    #     can_hold = False
                    elif event.key == pygame.K_DOWN:
                        speed_y = 0
                    elif event.key == pygame.K_LEFT:
                        speed_x = 0
                    elif event.key == pygame.K_RIGHT:
                        speed_x = 0
                    elif event.key == pygame.K_s:
                        speed_y2 = 0
                    elif event.key == pygame.K_a:
                        speed_x2 = 0
                    elif event.key == pygame.K_d:
                        speed_x2 = 0
                # elif event.type == pygame.VIDEORESIZE:
                    # self.screen.blit(pygame.transform.scale(self.background, event.dict['size']), (0, 0))
                    # pygame.display.update()

            # controlled movement (not too fast)
            if last_pressed_side >= interval:
                last_pressed_side = 0
                temp_left = b_left + speed_x
            if last_pressed_down >= interval and not no_down:
                last_pressed_down = 0
                temp_top = b_top + speed_y
            if last_pressed_side2 >= interval:
                last_pressed_side2 = 0
                temp_left2 = b_left2 + speed_x2
            if last_pressed_down2 >= interval and not no_down2:
                last_pressed_down2 = 0
                temp_top2 = b_top2 + speed_y2

            block_pos = convert_block(block, b_left, b_top)
            block_pos2 = convert_block(block2, b_left2, b_top2)

            if self.can_move(block, temp_left, temp_top):
                b_left = temp_left
                b_top = temp_top
            else:
                #update temptop, templeft
                temp_left = b_left
                temp_top = b_top
            if self.can_move(block2, temp_left2, temp_top2):
                b_left2 = temp_left2
                b_top2 = temp_top2
            else:
                #update temptop, templeft
                temp_left2 = b_left2
                temp_top2 = b_top2

            if change_piece:
                fall_speed = init_fall_speed - (level * 0.02)
                color = 0
                no_down = False
                #recharge hold
                can_hold = True
                # find color
                for row in block:
                    for col in row:
                        if col > 0:
                            color = col
                            break
                for i in range(len(block_pos)):
                    x, y = block_pos[i]
                    landed[y][x] = color
                if check_lost(block_pos):
                    self.draw_landed()
                    mainloop, fall_speed, score, hold_block_type, level = self.lose_screen(fall_speed, score, hold_block_type, level)
                    if not mainloop:
                        break
                block_type = next_block_type
                next_block_type = new_block()
                rotate_val = 0
                block, rotate_val = rotate(block_type, rotate_val)
                b_left = 5
                b_top = 2
                temp_top = 2
                temp_left = 5
                change_piece = False

            if change_piece2:
                fall_speed2 = init_fall_speed - (level * 0.02)
                color = 0
                no_down2 = False
                #recharge hold
                can_hold2 = True
                # find color
                for row in block2:
                    for col in row:
                        if col > 0:
                            color = col
                            break
                for i in range(len(block_pos2)):
                    x, y = block_pos2[i]
                    landed[y][x] = color
                if check_lost(block_pos2):
                    self.draw_landed()
                    mainloop, fall_speed, score, hold_block_type2, level = self.lose_screen(fall_speed, score, hold_block_type2, level)
                    if not mainloop:
                        break
                block_type2 = next_block_type2
                next_block_type2 = new_block2()
                rotate_val2 = 0
                block2, rotate_val2 = rotate(block_type2, rotate_val2)
                b_left2 = 5
                b_top2 = 2
                temp_top2 = 2
                temp_left2 = 5
                change_piece2 = False

            # check for cleared lines
            clear = True
            for row in range(self.lines - 1, -1, -1):
                for col in range(10):
                    if landed[row][col] == 0:
                        clear = False
                        break
                if clear:
                    score += 10
                    self.clear_line(row)
                else:
                    clear = True

            # blit all
            self.screen.blit(self.wipe_text, (offset_x + columns*pixel + right_dist, offset_y))
            self.screen.blit(self.wipe_text, (offset_x + columns*pixel + right_dist, offset_y + offset_y_2))
            self.screen.blit(self.wipe_text, (offset_x - left_dist, offset_y))
            if not paused:
                self.screen.blit(self.background, (offset_x, offset_y))
                self.draw_hold_block(hold_block_type)
                self.draw_next_block(next_block_type)
                self.draw_landed()
                self.draw_block(block, b_left, b_top)
                self.draw_block2(block2, b_left2, b_top2)
            self.screen.blit(level_font, (offset_x + columns*pixel + right_dist, offset_y + offset_y_2))
            self.screen.blit(score_font, (offset_x + columns*pixel + right_dist, offset_y))
            self.screen.blit(hold_font, ((offset_x - left_dist), offset_y))
            pygame.display.flip()

    def draw_landed(self):
        for row in range(self.lines):
            for col in range(self.col):
                self.draw_color(landed, row, col)

    def draw_block(self, block, b_left, b_top):
        pos = convert_block(block, b_left, b_top)
        color = 0
        #find color
        for row in block:
            for col in row:
                if col > 0:
                    color = col
                    break
        for i in range(len(pos)):
            x, y = pos[i]
            if y >= 0:
                if color == 1:
                    self.screen.blit(self.blue, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 2:
                    self.screen.blit(self.dblue, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 3:
                    self.screen.blit(self.green, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 4:
                    self.screen.blit(self.orange, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 5:
                    self.screen.blit(self.purple, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 6:
                    self.screen.blit(self.red, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 7:
                    self.screen.blit(self.yellow, (x * pixel + offset_x, y * pixel + offset_y))

    def draw_block2(self, block2, b_left2, b_top2):
        pos = convert_block(block2, b_left2, b_top2)
        color = 0
        #find color
        for row in block2:
            for col in row:
                if col > 0:
                    color = col
                    break
        for i in range(len(pos)):
            x, y = pos[i]
            if y >= 0:
                if color == 8:
                    self.screen.blit(self.blue2, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 9:
                    self.screen.blit(self.dblue2, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 10:
                    self.screen.blit(self.green2, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 11:
                    self.screen.blit(self.orange2, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 12:
                    self.screen.blit(self.purple2, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 13:
                    self.screen.blit(self.red2, (x * pixel + offset_x, y * pixel + offset_y))
                elif color == 14:
                    self.screen.blit(self.yellow2, (x * pixel + offset_x, y * pixel + offset_y))

    def draw_hold_block(self, hold_block_type):
        if not hold_block_type:
            hold_block = [[0 for i in range(5)] for j in range(5)]
        else:
            hold_block = hold_block_type[0]
        self.screen.blit(self.block_cover, (offset_x - left_dist, offset_y + offset_y_2))
        for row in range(len(hold_block)):
            for col in range(len(hold_block[0])):
                if hold_block[row][col] == 0:
                    self.screen.blit(self.grid_block, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 1:
                    self.screen.blit(self.blue, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 2:
                    self.screen.blit(self.dblue, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 3:
                    self.screen.blit(self.green, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 4:
                    self.screen.blit(self.orange, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 5:
                    self.screen.blit(self.purple, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 6:
                    self.screen.blit(self.red, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))
                elif hold_block[row][col] == 7:
                    self.screen.blit(self.yellow, ((col * pixel) + offset_x - left_dist, (row * pixel) + offset_y + offset_y_2))

    def draw_next_block(self, next_block_type):
        next_block = next_block_type[0]
        self.screen.blit(self.block_cover, (offset_x + columns * pixel + right_dist, offset_y + 2 * offset_y_2))
        for row in range(len(next_block)):
            for col in range(len(next_block[0])):
                if next_block[row][col] == 0:
                    self.screen.blit(self.grid_block, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 1:
                    self.screen.blit(self.blue, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 2:
                    self.screen.blit(self.dblue, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 3:
                    self.screen.blit(self.green, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 4:
                    self.screen.blit(self.orange, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 5:
                    self.screen.blit(self.purple, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 6:
                    self.screen.blit(self.red, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))
                elif next_block[row][col] == 7:
                    self.screen.blit(self.yellow, (col*pixel + offset_x + columns*pixel + right_dist, row*pixel + offset_y + 2*offset_y_2))

    def draw_color(self, co_list, row, col, left=0, top=0):
        if co_list[row][col] == 1:
            self.screen.blit(self.blue, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 2:
            self.screen.blit(self.dblue, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 3:
            self.screen.blit(self.green, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 4:
            self.screen.blit(self.orange, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 5:
            self.screen.blit(self.purple, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 6:
            self.screen.blit(self.red, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 7:
            self.screen.blit(self.yellow, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 8:
            self.screen.blit(self.blue2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 9:
            self.screen.blit(self.dblue2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 10:
            self.screen.blit(self.green2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 11:
            self.screen.blit(self.orange2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 12:
            self.screen.blit(self.purple2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 13:
            self.screen.blit(self.red2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))
        elif co_list[row][col] == 14:
            self.screen.blit(self.yellow2, ((col + left) * pixel + offset_x, (row + top) * pixel + offset_y))

    def lose_screen(self, fall_speed, score, hold_block_type, level):
        pygame.mixer.music.stop()
        hold_block_type = None
        hold_block_type2 = None
        level = 1
        score = 0
        fall_speed = init_fall_speed - (level * 0.02)
        font = pygame.font.SysFont(None, 25, True, False)
        text = font.render("GAME OVER", True, (255, 255, 255))
        text2 = font.render("PRESS \'R\' TO RESTART", True, (250, 250, 250))
        end_loop = True
        mainLoop = True
        self.screen.blit(self.end_screen, (offset_x, offset_y))
        self.screen.blit(text, (offset_x + 50, 30))
        self.screen.blit(text2, (offset_x, 60))
        pygame.display.flip()
        while end_loop:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # pygame window closed by user
                    mainloop = False
                    end_loop = False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        # pygame.mixer.music.load("theme.ogg")
                        pygame.mixer.music.play(-1, 0.0)
                        mainloop = True
                        end_loop = False
                        self.screen.blit(self.wipe_surf_complete, (0, 0))
                        self.restart_landed()
        return mainloop, fall_speed, score, hold_block_type, level

    def restart_landed(self):
        for x in range(self.lines):
            for y in range(self.col):
                landed[x][y] = 0

    def clear_line(self, num):
        if num != len(landed) - 1:
            for row in range(num, 0, -1):
                landed[row] = landed[row - 1]
            else:
                landed[0] = [i * 0 for i in range(self.col)]
        else:
            for row in range(len(landed) - 1, 0, -1):
                landed[row] = landed[row-1]
            else:
                landed[0] = [i * 0 for i in range(self.col)]

    def can_move(self, block, b_left, b_top):
        accepted_pos = [[(x, y) for x in range(self.col) if landed[y][x] == 0] for y in range(self.lines)]
        accepted_pos = [x for item in accepted_pos for x in item]

        formatted = convert_block(block, b_left, b_top)

        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] >= 0:
                    return False
        return True

    def can_rotate(self, block, block_type, b_left, b_top, rotate_vol):
        rotatable = True
        rotate_vol += 1
        pot_block, rotate_vol = rotate(block_type, rotate_vol)
        if self.can_move(pot_block, b_left, b_top):
            return pot_block, rotate_vol, b_left
        else:
            if self.can_move(pot_block, b_left - 1, b_top):
                return pot_block, rotate_vol, b_left - 1
            elif self.can_move(pot_block, b_left + 1, b_top):
                return pot_block, rotate_vol, b_left + 1
            else:
                if self.can_move(pot_block, b_left - 2, b_top):
                    return pot_block, rotate_vol, b_left - 2
                elif self.can_move(pot_block, b_left + 2, b_top):
                    return pot_block, rotate_vol, b_left + 2
                else:
                    rotate_vol -= 1
                    return block, rotate_vol, b_left

    def drop(self, block, b_left, b_top):
        temp_top = b_top + 1
        while self.can_move(block, b_left, temp_top):
            temp_top += 1
        temp_top -= 1
        return True, b_left, temp_top, 0, 0

if __name__ == "__main__":
    Game().run()
    pygame.quit()