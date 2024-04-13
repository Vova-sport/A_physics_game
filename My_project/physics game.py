import arcade
import os
from functions import fill_sprite_list

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Обучающая игра по кинематике"

BG_COSTUMES_PATH = 'img/bg'
BG_M_COSTUMES_PATH = 'audio/bg_m'
LEVEL_1_ANSWERS_COSTUMES_PATH = 'img/level_1/answers_level_1'
FORMULAS_LEVEL_1_COSTUMES_PATH = 'img/level_1/formulas_level_1'
LEVEL_2_ANSWERS_COSTUMES_PATH = 'img/level_2/answers_level_2'
FORMULAS_LEVEL_2_COSTUMES_PATH = 'img/level_2/formulas_level_2'
LEVEL_3_ANSWERS_COSTUMES_PATH = 'img/level_3/answers_level_3'
ILLUSTRATION_LEVEL_3_COSTUMES_PATH = 'img/level_3/illustration_level_3'
TASKS_CONDITIONS_LEVEL_4_COSTUMES_PATH = 'img/level_4/tasks_conditions_level_4'
TASKS_F_AND_A_LEVEL_4_COSTUMES_PATH = 'img/level_4/f_and_a_level_4'
TASKS_CONDITIONS_LEVEL_5_COSTUMES_PATH = 'img/level_5/tasks_conditions_level_5'
TASKS_F_AND_A_LEVEL_5_COSTUMES_PATH = 'img/level_5/f_and_a_level_5'
TASKS_CONDITIONS_LEVEL_6_COSTUMES_PATH = 'img/level_6/tasks_conditions_level_6'
TASKS_F_AND_A_LEVEL_6_COSTUMES_PATH = 'img/level_6/f_and_a_level_6'
TASKS_CONDITIONS_LEVEL_7_COSTUMES_PATH = 'img/level_7/tasks_conditions_level_7'
TASKS_F_AND_A_LEVEL_7_COSTUMES_PATH = 'img/level_7/f_and_a_level_7'
TASKS_CONDITIONS_LEVEL_8_COSTUMES_PATH = 'img/level_8/tasks_conditions_level_8'
TASKS_F_AND_A_LEVEL_8_COSTUMES_PATH = 'img/level_8/f_and_a_level_8'


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.start_img = arcade.load_texture('img/other/start.jpg')
        self.select_img = arcade.load_texture('img/other/select.jpg')
        self.exit_img = arcade.load_texture('img/other/exit.jpg')
        self.wall = arcade.load_texture('img/other/wall.jpg')
        self.wrong = arcade.load_texture('img/other/wrong.jpg')
        self.correctly = arcade.load_texture('img/other/correctly.jpg')
        self.box_answer = arcade.load_texture('img/other/box_answer.jpg')
        self.box_formula = arcade.load_texture('img/other/box_formula.jpg')
        self.graph_level_4 = arcade.load_texture('img/other/g_level_4.jpg')
        self.clik = arcade.load_sound('audio/effects/clik.mp3')
        self.lose = arcade.load_sound('audio/effects/lose.mp3')
        self.win = arcade.load_sound('audio/effects/win.mp3')
        self.mov = arcade.load_sound('audio/effects/mov.mp3')
        self.exit_m = arcade.load_sound('audio/effects/exit.mp3')
        self.back = arcade.load_sound('audio/effects/back.mp3')
        self.escape = arcade.load_sound('audio/effects/escape.mp3')
        self.start = arcade.load_sound('audio/effects/start.mp3')
        self.bg_l_imgs = []
        self.bg_l_ms = []
        self.game = 'start'
        self.exit = 'off'
        self.check = ''
        self.end = 'off'
        self.music = 'on'

        self.current_bg_music = ''
        self.all_bg_sounds = []

        self.selected_formula_level_1 = None
        self.selected_formula_level_2 = None
        self.selected_answers_level_3 = None
        self.selected_f_and_a_level_4 = None
        self.selected_f_and_a_level_5 = None
        self.selected_f_and_a_level_6 = None
        self.selected_f_and_a_level_7 = None
        self.selected_f_and_a_level_8 = None

        self.sprite_list_formuls_l1 = arcade.SpriteList()
        self.sprite_list_answers_l1 = arcade.SpriteList()

        self.sprite_list_formuls_l2 = arcade.SpriteList()
        self.sprite_list_answers_l2 = arcade.SpriteList()

        self.sprite_list_answers_l3 = arcade.SpriteList()
        self.sprite_list_illustration_l3 = arcade.SpriteList()

        self.sprite_list_conditions_l4 = arcade.SpriteList()
        self.sprite_list_f_and_a_l4 = arcade.SpriteList()

        self.sprite_list_conditions_l5 = arcade.SpriteList()
        self.sprite_list_f_and_a_l5 = arcade.SpriteList()

        self.sprite_list_conditions_l6 = arcade.SpriteList()
        self.sprite_list_f_and_a_l6 = arcade.SpriteList()

        self.sprite_list_conditions_l7 = arcade.SpriteList()
        self.sprite_list_f_and_a_l7 = arcade.SpriteList()

        self.sprite_list_conditions_l8 = arcade.SpriteList()
        self.sprite_list_f_and_a_l8 = arcade.SpriteList()

        self.setup()

        if self.game == 'start':
            self.current_bg_music = arcade.play_sound(self.bg_l_ms[8], 0.4)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == 1 and self.game != 'select_level' and self.game != 'start' and self.music == 'on':
            arcade.play_sound(self.mov, 0.4)

    def on_mouse_drag(self, x: int, y: int, dx: int, dy: int, buttons: int, modifiers: int):
        if buttons == 1 and self.game == 'level_1':
            for formula_l1 in self.sprite_list_formuls_l1:
                if x - 60 <= formula_l1.center_x <= x + 60 and y - 40 <= formula_l1.center_y <= y + 40:
                    self.selected_formula_level_1 = formula_l1
                    break
            if (self.selected_formula_level_1
                    and self.selected_formula_level_1.left > 0
                    and self.selected_formula_level_1.right < SCREEN_WIDTH
                    and self.selected_formula_level_1.top < SCREEN_HEIGHT
                    and self.selected_formula_level_1.bottom > 0):
                self.selected_formula_level_1.center_x = x
                self.selected_formula_level_1.center_y = y
            if self.selected_formula_level_1.left <= 0:
                self.selected_formula_level_1.left = 1
            if self.selected_formula_level_1.right >= SCREEN_WIDTH:
                self.selected_formula_level_1.right = SCREEN_WIDTH - 1
            if self.selected_formula_level_1.top >= SCREEN_HEIGHT:
                self.selected_formula_level_1.top = SCREEN_HEIGHT - 1
            if self.selected_formula_level_1.bottom <= 0:
                self.selected_formula_level_1.bottom = 1

        if buttons == 1 and self.game == 'level_2':
            for formula_l2 in self.sprite_list_formuls_l2:
                if x - 60 <= formula_l2.center_x <= x + 60 and y - 40 <= formula_l2.center_y <= y + 40:
                    self.selected_formula_level_2 = formula_l2
                    break
            if (self.selected_formula_level_2
                    and self.selected_formula_level_2.left > 0
                    and self.selected_formula_level_2.right < SCREEN_WIDTH
                    and self.selected_formula_level_2.top < SCREEN_HEIGHT
                    and self.selected_formula_level_2.bottom > 0):
                self.selected_formula_level_2.center_x = x
                self.selected_formula_level_2.center_y = y
            if self.selected_formula_level_2.left <= 0:
                self.selected_formula_level_2.left = 1
            if self.selected_formula_level_2.right >= SCREEN_WIDTH:
                self.selected_formula_level_2.right = SCREEN_WIDTH - 1
            if self.selected_formula_level_2.top >= SCREEN_HEIGHT:
                self.selected_formula_level_2.top = SCREEN_HEIGHT - 1
            if self.selected_formula_level_2.bottom <= 0:
                self.selected_formula_level_2.bottom = 1

        if buttons == 1 and self.game == 'level_3':
            for answer in self.sprite_list_answers_l3:
                if x - 60 <= answer.center_x <= x + 60 and y - 40 <= answer.center_y <= y + 40:
                    self.selected_answers_level_3 = answer
                    break
            if (self.selected_answers_level_3
                    and self.selected_answers_level_3.left > 0
                    and self.selected_answers_level_3.right < SCREEN_WIDTH
                    and self.selected_answers_level_3.top < SCREEN_HEIGHT
                    and self.selected_answers_level_3.bottom > 0):
                self.selected_answers_level_3.center_x = x
                self.selected_answers_level_3.center_y = y
            if self.selected_answers_level_3.left <= 0:
                self.selected_answers_level_3.left = 1
            if self.selected_answers_level_3.right >= SCREEN_WIDTH:
                self.selected_answers_level_3.right = SCREEN_WIDTH - 1
            if self.selected_answers_level_3.top >= SCREEN_HEIGHT:
                self.selected_answers_level_3.top = SCREEN_HEIGHT - 1
            if self.selected_answers_level_3.bottom <= 0:
                self.selected_answers_level_3.bottom = 1

        if buttons == 1 and self.game == 'level_4':
            for f_and_a in self.sprite_list_f_and_a_l4:
                if x - 60 <= f_and_a.center_x <= x + 60 and y - 40 <= f_and_a.center_y <= y + 40:
                    self.selected_f_and_a_level_4 = f_and_a
                    break
            if (self.selected_f_and_a_level_4
                    and self.selected_f_and_a_level_4.left > 0
                    and self.selected_f_and_a_level_4.right < SCREEN_WIDTH
                    and self.selected_f_and_a_level_4.top < SCREEN_HEIGHT
                    and self.selected_f_and_a_level_4.bottom > 0):
                self.selected_f_and_a_level_4.center_x = x
                self.selected_f_and_a_level_4.center_y = y
            if self.selected_f_and_a_level_4.left <= 0:
                self.selected_f_and_a_level_4.left = 1
            if self.selected_f_and_a_level_4.right >= SCREEN_WIDTH:
                self.selected_f_and_a_level_4.right = SCREEN_WIDTH - 1
            if self.selected_f_and_a_level_4.top >= SCREEN_HEIGHT:
                self.selected_f_and_a_level_4.top = SCREEN_HEIGHT - 1
            if self.selected_f_and_a_level_4.bottom <= 0:
                self.selected_f_and_a_level_4.bottom = 1

        if buttons == 1 and self.game == 'level_5':
            for f_and_a in self.sprite_list_f_and_a_l5:
                if x - 60 <= f_and_a.center_x <= x + 60 and y - 40 <= f_and_a.center_y <= y + 40:
                    self.selected_f_and_a_level_5 = f_and_a
                    break
            if (self.selected_f_and_a_level_5
                    and self.selected_f_and_a_level_5.left > 0
                    and self.selected_f_and_a_level_5.right < SCREEN_WIDTH
                    and self.selected_f_and_a_level_5.top < SCREEN_HEIGHT
                    and self.selected_f_and_a_level_5.bottom > 0):
                self.selected_f_and_a_level_5.center_x = x
                self.selected_f_and_a_level_5.center_y = y
            if self.selected_f_and_a_level_5.left <= 0:
                self.selected_f_and_a_level_5.left = 1
            if self.selected_f_and_a_level_5.right >= SCREEN_WIDTH:
                self.selected_f_and_a_level_5.right = SCREEN_WIDTH - 1
            if self.selected_f_and_a_level_5.top >= SCREEN_HEIGHT:
                self.selected_f_and_a_level_5.top = SCREEN_HEIGHT - 1
            if self.selected_f_and_a_level_5.bottom <= 0:
                self.selected_f_and_a_level_5.bottom = 1

        if buttons == 1 and self.game == 'level_6':
            for f_and_a in self.sprite_list_f_and_a_l6:
                if x - 60 <= f_and_a.center_x <= x + 60 and y - 40 <= f_and_a.center_y <= y + 40:
                    self.selected_f_and_a_level_6 = f_and_a
                    break
            if (self.selected_f_and_a_level_6
                    and self.selected_f_and_a_level_6.left > 0
                    and self.selected_f_and_a_level_6.right < SCREEN_WIDTH
                    and self.selected_f_and_a_level_6.top < SCREEN_HEIGHT
                    and self.selected_f_and_a_level_6.bottom > 0):
                self.selected_f_and_a_level_6.center_x = x
                self.selected_f_and_a_level_6.center_y = y
            if self.selected_f_and_a_level_6.left <= 0:
                self.selected_f_and_a_level_6.left = 1
            if self.selected_f_and_a_level_6.right >= SCREEN_WIDTH:
                self.selected_f_and_a_level_6.right = SCREEN_WIDTH - 1
            if self.selected_f_and_a_level_6.top >= SCREEN_HEIGHT:
                self.selected_f_and_a_level_6.top = SCREEN_HEIGHT - 1
            if self.selected_f_and_a_level_6.bottom <= 0:
                self.selected_f_and_a_level_6.bottom = 1

        if buttons == 1 and self.game == 'level_7':
            for f_and_a in self.sprite_list_f_and_a_l7:

                if x - 60 <= f_and_a.center_x <= x + 60 and y - 40 <= f_and_a.center_y <= y + 40:
                    self.selected_f_and_a_level_7 = f_and_a
                    break
            if (self.selected_f_and_a_level_7
                    and self.selected_f_and_a_level_7.left > 0
                    and self.selected_f_and_a_level_7.right < SCREEN_WIDTH
                    and self.selected_f_and_a_level_7.top < SCREEN_HEIGHT
                    and self.selected_f_and_a_level_7.bottom > 0):
                self.selected_f_and_a_level_7.center_x = x
                self.selected_f_and_a_level_7.center_y = y
            if self.selected_f_and_a_level_7.left <= 0:
                self.selected_f_and_a_level_7.left = 1
            if self.selected_f_and_a_level_7.right >= SCREEN_WIDTH:
                self.selected_f_and_a_level_7.right = SCREEN_WIDTH - 1
            if self.selected_f_and_a_level_7.top >= SCREEN_HEIGHT:
                self.selected_f_and_a_level_7.top = SCREEN_HEIGHT - 1
            if self.selected_f_and_a_level_7.bottom <= 0:
                self.selected_f_and_a_level_7.bottom = 1

        if buttons == 1 and self.game == 'level_8':
            for f_and_a in self.sprite_list_f_and_a_l8:

                if x - 60 <= f_and_a.center_x <= x + 60 and y - 40 <= f_and_a.center_y <= y + 40:
                    self.selected_f_and_a_level_8 = f_and_a
                    break
            if (self.selected_f_and_a_level_8
                    and self.selected_f_and_a_level_8.left > 0
                    and self.selected_f_and_a_level_8.right < SCREEN_WIDTH
                    and self.selected_f_and_a_level_8.top < SCREEN_HEIGHT
                    and self.selected_f_and_a_level_8.bottom > 0):
                self.selected_f_and_a_level_8.center_x = x
                self.selected_f_and_a_level_8.center_y = y
            if self.selected_f_and_a_level_8.left <= 0:
                self.selected_f_and_a_level_8.left = 1
            if self.selected_f_and_a_level_8.right >= SCREEN_WIDTH:
                self.selected_f_and_a_level_8.right = SCREEN_WIDTH - 1
            if self.selected_f_and_a_level_8.top >= SCREEN_HEIGHT:
                self.selected_f_and_a_level_8.top = SCREEN_HEIGHT - 1
            if self.selected_f_and_a_level_8.bottom <= 0:
                self.selected_f_and_a_level_8.bottom = 1

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.ENTER and self.game == 'start':
            self.game = 'select_level'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.start)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[9])

        if symbol == arcade.key.ESCAPE and self.game != 'select_level' and self.game != 'start':
            self.exit = 'on'
            if self.music == 'on':
                arcade.play_sound(self.escape)

        if symbol == arcade.key.Y and self.exit == 'on':
            self.game = 'select_level'
            self.exit = 'off'
            self.check = ''
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.exit_m)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[9], 0.4)
            self.sprite_list_answers_l1 = arcade.SpriteList()
            self.sprite_list_formuls_l1 = arcade.SpriteList()
            self.sprite_list_answers_l2 = arcade.SpriteList()
            self.sprite_list_formuls_l2 = arcade.SpriteList()
            self.sprite_list_illustration_l3 = arcade.SpriteList()
            self.sprite_list_answers_l3 = arcade.SpriteList()
            self.sprite_list_conditions_l4 = arcade.SpriteList()
            self.sprite_list_f_and_a_l4 = arcade.SpriteList()
            self.sprite_list_conditions_l5 = arcade.SpriteList()
            self.sprite_list_f_and_a_l5 = arcade.SpriteList()
            self.sprite_list_conditions_l6 = arcade.SpriteList()
            self.sprite_list_f_and_a_l6 = arcade.SpriteList()
            self.sprite_list_conditions_l7 = arcade.SpriteList()
            self.sprite_list_f_and_a_l7 = arcade.SpriteList()
            self.sprite_list_conditions_l8 = arcade.SpriteList()
            self.sprite_list_f_and_a_l8 = arcade.SpriteList()

        if symbol == arcade.key.N and self.exit == 'on':
            self.exit = 'off'
            if self.music == 'on':
                arcade.play_sound(self.back)

        if symbol == arcade.key.E and self.end == 'correctly':
            self.game = 'select_level'
            self.end = 'off'
            self.check = ''
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[9], 0.4)
            self.sprite_list_answers_l1 = arcade.SpriteList()
            self.sprite_list_formuls_l1 = arcade.SpriteList()
            self.sprite_list_answers_l2 = arcade.SpriteList()
            self.sprite_list_formuls_l2 = arcade.SpriteList()
            self.sprite_list_illustration_l3 = arcade.SpriteList()
            self.sprite_list_answers_l3 = arcade.SpriteList()
            self.sprite_list_conditions_l4 = arcade.SpriteList()
            self.sprite_list_f_and_a_l4 = arcade.SpriteList()
            self.sprite_list_conditions_l5 = arcade.SpriteList()
            self.sprite_list_f_and_a_l5 = arcade.SpriteList()
            self.sprite_list_conditions_l6 = arcade.SpriteList()
            self.sprite_list_f_and_a_l6 = arcade.SpriteList()
            self.sprite_list_conditions_l7 = arcade.SpriteList()
            self.sprite_list_f_and_a_l7 = arcade.SpriteList()
            self.sprite_list_conditions_l8 = arcade.SpriteList()
            self.sprite_list_f_and_a_l8 = arcade.SpriteList()

        if symbol == arcade.key.O and self.end == 'wrong':
            self.end = 'off'
            if self.music == 'on':
                arcade.play_sound(self.clik)

        if symbol == arcade.key.KEY_1 and self.game == 'select_level':
            self.game = 'level_1'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
            if self.music == 'on':
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[0], 0.4)

            self.formulas_coords_l1 = [540, 450, 370, 290, 200, 115]
            self.formula_level_1_textures_name = os.listdir(FORMULAS_LEVEL_1_COSTUMES_PATH)
            fill_sprite_list(
                self.formula_level_1_textures_name,
                Movable,
                FORMULAS_LEVEL_1_COSTUMES_PATH,
                0.8,
                [self.formulas_coords_l1],
                self.sprite_list_formuls_l1,
                fill_random='random y',
                center_x=SCREEN_WIDTH / 2
            )

            self.answer_coords_l1 = [
                [95, 505],
                [95, 325],
                [95, 155],
                [700, 505],
                [700, 325],
                [700, 155]
            ]
            self.answers_level_1_textures_name = os.listdir(LEVEL_1_ANSWERS_COSTUMES_PATH)
            fill_sprite_list(
                self.answers_level_1_textures_name,
                Static,
                LEVEL_1_ANSWERS_COSTUMES_PATH,
                0.8,
                [self.answer_coords_l1],
                self.sprite_list_answers_l1
            )

        if symbol == arcade.key.KEY_2 and self.game == 'select_level':
            self.game = 'level_2'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[1], 0.4)
            self.answer_coords_l2 = [
                [95, 505],
                [95, 325],
                [95, 155],
                [450, 505],
                [450, 325],
                [450, 155]
            ]
            self.answers_level_2_textures_name = os.listdir(LEVEL_2_ANSWERS_COSTUMES_PATH)
            fill_sprite_list(
                self.answers_level_2_textures_name,
                Static,
                LEVEL_2_ANSWERS_COSTUMES_PATH,
                1.3,
                [self.answer_coords_l2],
                self.sprite_list_answers_l2
            )

            self.formulas_coords_l2 = [540, 450, 370, 290, 200, 115]
            self.formula_level_2_textures_name = os.listdir(FORMULAS_LEVEL_2_COSTUMES_PATH)
            fill_sprite_list(
                self.formula_level_2_textures_name,
                Movable,
                FORMULAS_LEVEL_2_COSTUMES_PATH,
                0.8,
                [self.formulas_coords_l2],
                self.sprite_list_formuls_l2,
                fill_random='random y',
                center_x=700
            )

        if symbol == arcade.key.KEY_3 and self.game == 'select_level':
            self.game = 'level_3'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[2], 0.4)
            self.illustration_level_3_coords = [
                [110, 505],
                [110, 155],
                [550, 155],
                [550, 505]
            ]
            self.illustration_level_3_textures_name = os.listdir(ILLUSTRATION_LEVEL_3_COSTUMES_PATH)
            fill_sprite_list(
                self.illustration_level_3_textures_name,
                Static,
                ILLUSTRATION_LEVEL_3_COSTUMES_PATH,
                0.5,
                [self.illustration_level_3_coords],
                self.sprite_list_illustration_l3
            )

            self.answers_coords_l3 = [700, 500, 300, 100]
            self.answer_level_3_textures_name = os.listdir(LEVEL_3_ANSWERS_COSTUMES_PATH)
            fill_sprite_list(
                self.answer_level_3_textures_name,
                Movable,
                LEVEL_3_ANSWERS_COSTUMES_PATH,
                1,
                [self.answers_coords_l3],
                self.sprite_list_answers_l3,
                fill_random='random x',
                center_y=300
            )

        if symbol == arcade.key.KEY_4 and self.game == 'select_level':
            self.game = 'level_4'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[3], 0.4)
            self.сonditions_level_4_coords = [
                [150, 505],
                [725, 505]
            ]
            self.сonditions_level_4_textures_name = os.listdir(TASKS_CONDITIONS_LEVEL_4_COSTUMES_PATH)
            fill_sprite_list(
                self.сonditions_level_4_textures_name,
                Static,
                TASKS_CONDITIONS_LEVEL_4_COSTUMES_PATH,
                0.55,
                [self.сonditions_level_4_coords],
                self.sprite_list_conditions_l4
            )

            self.f_and_a_coords_l4 = [540, 450, 370, 290, 200, 115]
            self.f_and_a_level_4_textures_name = os.listdir(TASKS_F_AND_A_LEVEL_4_COSTUMES_PATH)
            fill_sprite_list(
                self.f_and_a_level_4_textures_name,
                Movable,
                TASKS_F_AND_A_LEVEL_4_COSTUMES_PATH,
                1,
                [self.f_and_a_coords_l4],
                self.sprite_list_f_and_a_l4,
                fill_random='random y',
                center_x=443
            )

        if symbol == arcade.key.KEY_5 and self.game == 'select_level':
            self.game = 'level_5'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[4], 0.4)
            self.сonditions_level_5_coords = [
                [150, 505],
                [660, 505]
            ]
            self.сonditions_level_5_textures_name = os.listdir(TASKS_CONDITIONS_LEVEL_5_COSTUMES_PATH)
            fill_sprite_list(
                self.сonditions_level_5_textures_name,
                Static,
                TASKS_CONDITIONS_LEVEL_5_COSTUMES_PATH,
                1,
                [self.сonditions_level_5_coords],
                self.sprite_list_conditions_l5
            )

            self.f_and_a_coords_l5 = [540, 450, 370, 290, 200, 115]
            self.f_and_a_level_5_textures_name = os.listdir(TASKS_F_AND_A_LEVEL_5_COSTUMES_PATH)
            fill_sprite_list(
                self.f_and_a_level_5_textures_name,
                Movable,
                TASKS_F_AND_A_LEVEL_5_COSTUMES_PATH,
                1,
                [self.f_and_a_coords_l5],
                self.sprite_list_f_and_a_l5,
                fill_random='random y',
                center_x=410
            )

        if symbol == arcade.key.KEY_6 and self.game == 'select_level':
            self.game = 'level_6'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[5], 0.4)
            self.сonditions_level_6_coords = [
                [170, 505],
                [680, 505]
            ]
            self.сonditions_level_6_textures_name = os.listdir(TASKS_CONDITIONS_LEVEL_6_COSTUMES_PATH)
            fill_sprite_list(
                self.сonditions_level_6_textures_name,
                Static,
                TASKS_CONDITIONS_LEVEL_6_COSTUMES_PATH,
                1,
                [self.сonditions_level_6_coords],
                self.sprite_list_conditions_l6
            )

            self.f_and_a_coords_l6 = [540, 450, 370, 290, 200, 115]
            self.f_and_a_level_6_textures_name = os.listdir(TASKS_F_AND_A_LEVEL_6_COSTUMES_PATH)
            fill_sprite_list(
                self.f_and_a_level_6_textures_name,
                Movable,
                TASKS_F_AND_A_LEVEL_6_COSTUMES_PATH,
                1,
                [self.f_and_a_coords_l6],
                self.sprite_list_f_and_a_l6,
                fill_random='random y',
                center_x=450
            )

        if symbol == arcade.key.KEY_7 and self.game == 'select_level':
            self.game = 'level_7'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[6], 0.4)
            self.сonditions_level_7_coords = [
                [400, 505]
            ]
            self.сonditions_level_7_textures_name = os.listdir(TASKS_CONDITIONS_LEVEL_7_COSTUMES_PATH)
            fill_sprite_list(
                self.сonditions_level_7_textures_name,
                Static,
                TASKS_CONDITIONS_LEVEL_7_COSTUMES_PATH,
                0.75,
                [self.сonditions_level_7_coords],
                self.sprite_list_conditions_l7
            )

            self.formulas_coords_level_7 = [
                [715, 260],
                [715, 170],
                [715, 85],
                [540, 260],
                [540, 170],
                [540, 85],
                [305, 260],
                [305, 170],
                [305, 85],
                [80, 260],
                [80, 170],
                [80, 85],
            ]
            self.formulas_coords_l7_textures_name = os.listdir(TASKS_F_AND_A_LEVEL_7_COSTUMES_PATH)

            fill_sprite_list(
                self.formulas_coords_l7_textures_name,
                Movable,
                TASKS_F_AND_A_LEVEL_7_COSTUMES_PATH,
                1,
                [self.formulas_coords_level_7],
                self.sprite_list_f_and_a_l7
            )

        if symbol == arcade.key.KEY_8 and self.game == 'select_level':
            self.game = 'level_8'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''
            if self.music == 'on':
                arcade.play_sound(self.clik)
                self.current_bg_music = arcade.play_sound(self.bg_l_ms[7], 0.4)
            self.сonditions_level_8_coords = [
                [400, 505]
            ]
            self.сonditions_level_8_textures_name = os.listdir(TASKS_CONDITIONS_LEVEL_8_COSTUMES_PATH)
            fill_sprite_list(
                self.сonditions_level_8_textures_name,
                Static,
                TASKS_CONDITIONS_LEVEL_8_COSTUMES_PATH,
                0.75,
                [self.сonditions_level_8_coords],
                self.sprite_list_conditions_l8
            )

            self.formulas_coords_level_8 = [
                [715, 260],
                [715, 170],
                [715, 85],
                [540, 260],
                [540, 170],
                [540, 85],
                [305, 260],
                [305, 170],
                [305, 85],
                [80, 260],
                [80, 170],
                [80, 85],
            ]
            self.formulas_coords_l8_textures_name = os.listdir(TASKS_F_AND_A_LEVEL_8_COSTUMES_PATH)

            fill_sprite_list(
                self.formulas_coords_l8_textures_name,
                Movable,
                TASKS_F_AND_A_LEVEL_8_COSTUMES_PATH,
                1,
                [self.formulas_coords_level_8],
                self.sprite_list_f_and_a_l8
            )

        if symbol == arcade.key.C and self.game == 'level_1':
            for i, answer in enumerate(self.sprite_list_answers_l1):
                if '00' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l1:
                        if (
                                '00' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l1_c'
                if '01' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l1:
                        if (
                                '01' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l2_c'
                if '02' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l1:
                        if (
                                '02' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l3_c'
                if '03' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l1:
                        if (
                                '03' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l4_c'
                if '04' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l1:
                        if (
                                '04' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l5_c'
                if '05' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l1:
                        if (
                                '05' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l6_c'
                if ('l1_c' in self.check and 'l2_c' in self.check and 'l3_c' in self.check and 'l4_c' in self.check
                        and 'l5_c' in self.check and 'l6_c' in self.check):
                    self.end = 'correctly'
                    if self.music == 'on':
                        arcade.play_sound(self.win)
                else:
                    self.end = 'wrong'
                    if self.music == 'on':
                        arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_2':
            print(self.check)
            for i, answer in enumerate(self.sprite_list_answers_l2):
                if '00' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l2:
                        if (
                                '00' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l1_c'
                if '01' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l2:
                        if (
                                '01' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l2_c'
                if '02' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l2:
                        if (
                                '02' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l3_c'
                if '03' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l2:
                        if (
                                '03' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l4_c'
                if '04' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l2:
                        if (
                                '04' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l5_c'
                if '05' in answer.texture.name:
                    for formula in self.sprite_list_formuls_l2:
                        if (
                                '05' in formula.texture.name and answer.center_y - 40 <= formula.center_y <= answer.center_y + 40
                                and answer.center_x - 40 <= formula.center_x <= answer.center_x + 40):
                            self.check += 'l6_c'
                if ('l1_c' in self.check and 'l2_c' in self.check and 'l3_c' in self.check and 'l4_c' in self.check
                        and 'l5_c' in self.check and 'l6_c' in self.check):
                    self.end = 'correctly'
                    if self.music == 'on':
                        arcade.play_sound(self.win)
                else:
                    self.end = 'wrong'
                    if self.music == 'on':
                        arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_3':
            for i, illustration in enumerate(self.sprite_list_illustration_l3):
                if '00' in illustration.texture.name:
                    for answer in self.sprite_list_answers_l3:
                        if ('00' in answer.texture.name and illustration.bottom - 40 <= answer.top):
                            self.check += 'l1_c'
                if '01' in illustration.texture.name:
                    for answer in self.sprite_list_answers_l3:
                        if (
                                '01' in answer.texture.name and illustration.bottom - 40 <= answer.top):
                            self.check += 'l2_c'
                if '02' in illustration.texture.name:
                    for answer in self.sprite_list_answers_l3:
                        if (
                                '02' in answer.texture.name and illustration.bottom - 40 <= answer.top):
                            self.check += 'l3_c'
                if '03' in illustration.texture.name:
                    for answer in self.sprite_list_answers_l3:
                        if (
                                '03' in answer.texture.name and illustration.bottom - 40 <= answer.top):
                            self.check += 'l4_c'
                if 'l1_c' in self.check and 'l2_c' in self.check and 'l3_c' in self.check and 'l4_c':
                    self.end = 'correctly'
                    if self.music == 'on':
                        arcade.play_sound(self.win)
                else:
                    self.end = 'wrong'
                    if self.music == 'on':
                        arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_4':
            for i, f_and_a in enumerate(self.sprite_list_f_and_a_l4):
                if '00' in f_and_a.texture.name and 110 <= f_and_a.center_x <= 190 and 160 <= f_and_a.center_y <= 240:
                    self.check += 'l1_c'
            for f_and_a in self.sprite_list_f_and_a_l4:
                if '03' in f_and_a.texture.name and 685 <= f_and_a.center_x <= 765 and 160 <= f_and_a.center_y <= 240:
                    self.check += 'l2_c'
                if 'l1_c' in self.check and 'l2_c' in self.check:
                    self.end = 'correctly'
                    if self.music == 'on':
                        arcade.play_sound(self.win)
                else:
                    self.end = 'wrong'
                    if self.music == 'on':
                        arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_5':
            for i, f_and_a in enumerate(self.sprite_list_f_and_a_l5):
                if '00' in f_and_a.texture.name and 110 <= f_and_a.center_x <= 190 and 160 <= f_and_a.center_y <= 240:
                    self.check += 'l1_c'
            for f_and_a in self.sprite_list_f_and_a_l5:
                if '05' in f_and_a.texture.name and 620 <= f_and_a.center_x <= 700 and 160 <= f_and_a.center_y <= 240:
                    self.check += 'l2_c'
                if 'l1_c' in self.check and 'l2_c' in self.check:
                    self.end = 'correctly'
                    if self.music == 'on':
                        arcade.play_sound(self.win)
                else:
                    self.end = 'wrong'
                    if self.music == 'on':
                        arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_6':
            for i, f_and_a in enumerate(self.sprite_list_f_and_a_l6):
                if '00' in f_and_a.texture.name and 145 <= f_and_a.center_x <= 225 and 160 <= f_and_a.center_y <= 240:
                    self.check += 'l1_c'
            for f_and_a in self.sprite_list_f_and_a_l6:
                if '01' in f_and_a.texture.name and 660 <= f_and_a.center_x <= 740 and 160 <= f_and_a.center_y <= 240:
                    self.check += 'l2_c'
                if 'l1_c' in self.check and 'l2_c' in self.check:
                    self.end = 'correctly'
                    if self.music == 'on':
                        arcade.play_sound(self.win)
                else:
                    self.end = 'wrong'
                    if self.music == 'on':
                        arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_7':
            for i, f_and_a in enumerate(self.sprite_list_f_and_a_l7):
                if '11' in f_and_a.texture.name and 700 <= f_and_a.center_x <= 730 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'a_c'
            for f_and_a in self.sprite_list_f_and_a_l7:
                if '07' in f_and_a.texture.name and 70 <= f_and_a.center_x <= 100 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'f1_c'
            for f_and_a in self.sprite_list_f_and_a_l7:
                if '06' in f_and_a.texture.name and 285 <= f_and_a.center_x <= 315 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'f2_c'
            for f_and_a in self.sprite_list_f_and_a_l7:
                if '08' in f_and_a.texture.name and 500 <= f_and_a.center_x <= 530 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'f3_c'
            if 'a_c' in self.check and 'f1_c' in self.check and 'f2_c' in self.check and 'f3_c' in self.check:
                self.end = 'correctly'
                if self.music == 'on':
                    arcade.play_sound(self.win)
            else:
                self.end = 'wrong'
                if self.music == 'on':
                    arcade.play_sound(self.lose)

        if symbol == arcade.key.C and self.game == 'level_8':
            for i, f_and_a in enumerate(self.sprite_list_f_and_a_l8):
                if '11' in f_and_a.texture.name and 700 <= f_and_a.center_x <= 730 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'a_c'
            for f_and_a in self.sprite_list_f_and_a_l8:
                if '03' in f_and_a.texture.name and 70 <= f_and_a.center_x <= 100 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'f1_c'
            for f_and_a in self.sprite_list_f_and_a_l8:
                if '08' in f_and_a.texture.name and 385 <= f_and_a.center_x <= 415 and 385 <= f_and_a.center_y <= 415:
                    self.check += 'f2_c'
            if 'a_c' in self.check and 'f1_c' in self.check and 'f2_c' in self.check:
                self.end = 'correctly'
                if self.music == 'on':
                    arcade.play_sound(self.win)
            else:
                self.end = 'wrong'
                if self.music == 'on':
                    arcade.play_sound(self.lose)

        if symbol == arcade.key.D and self.music == 'on':
            self.music = 'off'
            if self.current_bg_music != '':
                self.current_bg_music.delete()
                self.current_bg_music = ''

        if symbol == arcade.key.A and self.music == 'off':
            self.music = 'on'

    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.start_img)

        if self.game == 'select_level':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.select_img)
            arcade.draw_text('V', SCREEN_WIDTH - 445, SCREEN_HEIGHT - 565,
                             arcade.color.BABY_BLUE, 30)
        if self.game == 'level_1':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[1])
            arcade.draw_text(' Соедини формулы с правильным названием', SCREEN_WIDTH - 650, SCREEN_HEIGHT - 50,
                             arcade.color.DARK_BLUE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 40, arcade.color.WHITE, 20)
            self.sprite_list_answers_l1.draw()
            self.sprite_list_formuls_l1.draw()

        if self.game == 'level_2':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[2])
            arcade.draw_text('Соедини две части формулы', 230, 600,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 40, arcade.color.WHITE, 20)
            self.sprite_list_answers_l2.draw()
            self.sprite_list_formuls_l2.draw()

        if self.game == 'level_3':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[3])
            arcade.draw_text('Соедините физическую величину и рисунок', SCREEN_WIDTH - 700, SCREEN_HEIGHT - 50,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 40, arcade.color.WHITE, 20)
            self.sprite_list_illustration_l3.draw()
            self.sprite_list_answers_l3.draw()

        if self.game == 'level_4':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[4])
            arcade.draw_text('Решите задачи', 300, 600,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 20, arcade.color.WHITE, 20)
            arcade.draw_texture_rectangle(305, 310, 10, 520,
                                          self.wall)
            arcade.draw_texture_rectangle(570, 310, 10, 520,
                                          self.wall)
            arcade.draw_texture_rectangle(225, 390, 150, 150,
                                          self.graph_level_4)
            arcade.draw_texture_rectangle(150, 200, 300, 150,
                                          self.box_answer)
            arcade.draw_texture_rectangle(725, 200, 300, 150,
                                          self.box_answer)
            self.sprite_list_conditions_l4.draw()
            self.sprite_list_f_and_a_l4.draw()

        if self.game == 'level_5':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[5])
            arcade.draw_text('Решите задачи', 300, 600,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 20, arcade.color.WHITE, 20)
            arcade.draw_texture_rectangle(305, 310, 10, 520,
                                          self.wall)
            arcade.draw_texture_rectangle(510, 310, 10, 520,
                                          self.wall)
            arcade.draw_texture_rectangle(130, 200, 300, 150,
                                          self.box_answer)
            arcade.draw_texture_rectangle(670, 200, 300, 150,
                                          self.box_answer)
            self.sprite_list_conditions_l5.draw()
            self.sprite_list_f_and_a_l5.draw()

        if self.game == 'level_6':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[6])
            arcade.draw_text('Решите задачи', 300, 600,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 20, arcade.color.WHITE, 20)
            arcade.draw_texture_rectangle(340, 310, 10, 520,
                                          self.wall)
            arcade.draw_texture_rectangle(545, 310, 10, 520,
                                          self.wall)
            arcade.draw_texture_rectangle(185, 200, 300, 150,
                                          self.box_answer)
            arcade.draw_texture_rectangle(700, 200, 300, 150,
                                          self.box_answer)
            self.sprite_list_conditions_l6.draw()
            self.sprite_list_f_and_a_l6.draw()

        if self.game == 'level_7':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[7])
            arcade.draw_text('Решите задачу', 300, 600,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 20, arcade.color.WHITE, 20)
            arcade.draw_texture_rectangle(85, 400, 150, 100,
                                          self.box_formula)
            arcade.draw_texture_rectangle(300, 400, 150, 100,
                                          self.box_formula)
            arcade.draw_texture_rectangle(515, 400, 150, 100,
                                          self.box_formula)
            arcade.draw_texture_rectangle(715, 400, 150, 100,
                                          self.box_answer)
            arcade.draw_texture_rectangle(0, 310, 10, 2000,
                                          self.wall, 90)
            self.sprite_list_conditions_l7.draw()
            self.sprite_list_f_and_a_l7.draw()

        if self.game == 'level_8':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.bg_l_imgs[7])
            arcade.draw_text('Решите задачу', 300, 600,
                             arcade.color.WHITE, 20)
            arcade.draw_text('Чтобы проверить ответ нажмите "C"', 150, 20, arcade.color.WHITE, 20)
            arcade.draw_texture_rectangle(85, 400, 150, 100,
                                          self.box_formula)
            arcade.draw_texture_rectangle(400, 400, 150, 100,
                                          self.box_formula)
            arcade.draw_texture_rectangle(715, 400, 150, 100,
                                          self.box_answer)
            arcade.draw_texture_rectangle(0, 310, 10, 2000,
                                          self.wall, 90)
            self.sprite_list_conditions_l8.draw()
            self.sprite_list_f_and_a_l8.draw()

        if self.exit == 'on':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 400, 150, self.exit_img)

        if self.exit == 'guide_form':
            self.game = 'select_level'
            self.exit = 'off'

        if self.end == 'wrong' and self.game != 'select_level' and self.game != 'start':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 400, 150, self.wrong)
        if self.end == 'correctly' and self.game != 'select_level' and self.game != 'start':
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 400, 150, self.correctly)

    def update(self, delta_time: float):
        pass

    def setup(self):

        self.bg_l_imgs_dir = os.listdir(BG_COSTUMES_PATH)
        for bg in self.bg_l_imgs_dir:
            self.bg_l_imgs.append(arcade.load_texture(BG_COSTUMES_PATH + '/' + bg))

        self.bg_l_ms_dir = os.listdir(BG_M_COSTUMES_PATH)
        for bg_m in self.bg_l_ms_dir:
            self.bg_l_ms.append(arcade.load_sound(BG_M_COSTUMES_PATH + '/' + bg_m))


class Static(arcade.Sprite):
    def __init__(self, texture, size):
        super().__init__(texture, size)


class Movable(arcade.Sprite):
    def __init__(self, texture, size):
        super().__init__()
        self.texture = arcade.load_texture(texture)
        self.moved = True


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
