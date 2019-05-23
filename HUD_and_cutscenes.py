import  pygame as pg
from Settings import *

class HUD(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 2
        self.groups = game.heads_up_display
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.load_images()
        self.surface = self.draw_HUD()
        self.rect = (3, 6, 115, 95)


    def load_images(self):
        self.hud = self.game.spritesheet_hud.get_image(1, 18, 112, 79).convert()
        self.hud_underlay = self.game.spritesheet_hud.get_image(12, 104, 64, 56)
        self.hud_underlay2 = self.game.spritesheet_hud.get_image(6, 164, 79, 3)
        self.hud_underlay3 = self.game.spritesheet_hud.get_image(2, 170, 108, 4)
        self.ingame_portrait = self.game.spritesheet_hud.get_image(133, 32, 62, 55)
        self.green_hp = self.game.spritesheet_hud.get_image(131, 2, 110, 6)
        self.yellow_hp = self.game.spritesheet_hud.get_image(131, 9, 79, 6)
        self.red_hp = self.game.spritesheet_hud.get_image(131, 16, 31, 6)

    def draw_HUD(self):
        self.hud.set_colorkey(BLUE)
        self.green_hp.set_colorkey(BLUE)
        self.yellow_hp.set_colorkey(BLUE)
        self.red_hp.set_colorkey(BLUE)
        self.surface = pg.Surface((0, 0))
        self.surface.set_alpha(255)

        return self.surface

class Get_ready_screen(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 2
        self.groups = game.get_ready
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.load_images()
        self.surface = pg.Surface((0,0))
        #Backdrop
        self.darkness_ok = True
        self.darkness_update = 0
        self.darkness_alpha = 0
        #Bars
        self.bars_ok = False
        self.bars_pos_x = -500
        self.bars_pos_y = 70
        self.bars_update = 0
        self.surface = self.draw_backlayer()
        #Portrait
        self.portrait_ok = False
        self.portrait_pos_x = -290
        self.portrait_update = 0
        self.rect = (3, 6, 400, 400)
        #LightFlash
        self.flash_up_ok = False
        self.flash_down_ok = False
        self.flash_surface = pg.Surface((480,360))
        self.flash_surface.fill(WHITE)
        self.flash_real = pg.Surface((480,360))
        self.flash_real.set_alpha(0)
        self.flash_surface_alpha = 0
        self.flash_surface_update = 0
        #Get Ready...
        self.get_ready_ok = False
        self.get_ready_pos_x = 480
        self.get_ready_pos_y = 200
        self.get_ready_alpha = 0
        self.get_ready_update = 0
        self.get_ready.set_alpha(self.get_ready_alpha)
        #Survive!
        self.survive_ok = False
        self.survive_pos_x = 480
        self.survive_pos_y = 200
        self.survive_alpha = 0
        self.survive_update = 0
        self.survive.set_alpha(self.survive_alpha)
        #Final Flash
        self.final_flash_ok = False
        self.final_flash_fade = False
        self.final_flash_surface = pg.Surface((480, 360))
        self.final_flash_surface.fill(WHITE)
        self.final_flash_real = pg.Surface((480, 360))
        self.final_flash_real.set_alpha(0)
        self.final_flash_surface_alpha = 0
        self.final_flash_surface_update = 0
        #Sound effects
        self.snd_update = 0
        self.snd_whoosh = False
        self.snd_whoosh1 = True
        self.snd_tick = False
        self.snd_tick1 = True

    def load_images(self):
        self.bars = self.game.spritesheet_Game_start.get_image(5, 471, 490, 112)
        self.green_bar = self.game.spritesheet_Game_start.get_image(4, 367, 481, 99)
        self.darkness = self.game.spritesheet_Game_start.get_image(3, 2, 481, 362)
        self.portrait = self.game.spritesheet_Game_start.get_image(492, 10, 290, 110)
        self.get_ready = self.game.spritesheet_Game_start.get_image(489, 137, 144, 20).convert()
        self.get_ready.set_colorkey(BROWN)
        self.survive = self.game.spritesheet_Game_start.get_image(489, 164, 103, 20)

    def update(self):
        self.sound_effects()
        self.draw_backlayer()
        self.draw_bars()
        self.draw_portrait()
        self.flash()
        self.draw_get_ready()
        self.draw_survive()
        self.final_flash()
        self.blit_start_screen()

    def sound_effects(self):
        if self.snd_whoosh == True and self.snd_whoosh1 == True:
            self.game.snd_effects['woosh'].play()
            self.snd_whoosh1 = False
        if self.snd_tick == True and self.snd_tick1 == True:
            self.game.snd_effects['tick'].play()
            self.snd_tick1 = False

    def draw_backlayer(self):
        if self.darkness_ok == True:
            now = pg.time.get_ticks()
            self.darkness.set_alpha(self.darkness_alpha)
            if self.darkness_alpha < 215:
                self.snd_whoosh = True

                if now - self.darkness_update > 8:
                    self.darkness_update = pg.time.get_ticks()
                    self.darkness_alpha = self.darkness_alpha + 10
            else:
                self.bars_ok = True

    def draw_bars(self):
        if self.bars_ok == True:
            now = pg.time.get_ticks()
            if self.bars_pos_x < 0:
                if now - self.bars_update > 0.2:
                    self.bars_update = pg.time.get_ticks()
                    self.bars_pos_x = self.bars_pos_x + 50
            else:
                self.portrait_ok = True

    def draw_portrait(self):
        if self.portrait_ok == True:
            now = pg.time.get_ticks()
            if self.portrait_pos_x < 100:
                if now - self.portrait_update > 2:
                    self.portrait_update = pg.time.get_ticks()
                    self.portrait_pos_x = self.portrait_pos_x + 30
            if self.portrait_pos_x >= 100 and self.portrait_pos_x < 110:
                self.snd_tick = True

                if now - self.portrait_update > 80:
                    self.portrait_update = pg.time.get_ticks()
                    self.portrait_pos_x = self.portrait_pos_x + 1
                    if self.portrait_pos_x == 103:

                        self.flash_up_ok = True

    def flash(self):
        if self.flash_up_ok == True:
            now = pg.time.get_ticks()
            self.flash_real.blit(self.flash_surface, (0, 0))
            self.flash_real.set_alpha(self.flash_surface_alpha)
            if self.flash_surface_alpha < 255:
                if now - self.flash_surface_update > 20:
                    self.flash_surface_update = pg.time.get_ticks()
                    self.flash_surface_alpha = self.flash_surface_alpha + 55
                    if self.flash_surface_alpha >= 255:
                        self.flash_up_ok = False
                        self.get_ready_ok = True
                        self.flash_down_ok = True

        if self.flash_down_ok == True:
            now = pg.time.get_ticks()
            self.flash_real.blit(self.flash_surface, (0, 0))
            self.flash_real.set_alpha(self.flash_surface_alpha)
            if self.flash_surface_alpha > 0:
                if now - self.flash_surface_update > 20:
                    self.flash_surface_update = pg.time.get_ticks()
                    self.flash_surface_alpha = self.flash_surface_alpha - 55
                    if self.flash_surface_alpha <= -50:
                        self.flash_down_ok = False

    def draw_get_ready(self):
        if self.get_ready_ok == True:
            now = pg.time.get_ticks()
            self.get_ready.set_alpha(self.get_ready_alpha)
            if self.get_ready_pos_x > 220:
                if now - self.get_ready_update > 4:
                    self.get_ready_update = pg.time.get_ticks()
                    self.get_ready_pos_x = self.get_ready_pos_x - 24
            if self.get_ready_pos_x >= 180 and self.get_ready_pos_x <= 220:
                if now - self.get_ready_update > 20:
                    self.get_ready_update = pg.time.get_ticks()
                    self.get_ready_pos_x = self.get_ready_pos_x - 1
                    self.get_ready_alpha = self.get_ready_alpha + 20
            if self.get_ready_pos_x == 179:
                if now - self.get_ready_update > 800:
                    self.survive_ok = True

    def draw_survive(self):
        if self.survive_ok == True:
            now = pg.time.get_ticks()
            self.survive.set_alpha(self.survive_alpha)
            if self.survive_pos_x > 220:
                if now - self.survive_update > 4:
                    self.get_ready.set_alpha(self.get_ready_alpha)
                    self.survive_update = pg.time.get_ticks()
                    self.get_ready_pos_x = self.get_ready_pos_x - 10
                    self.survive_pos_x = self.survive_pos_x - 12
                    self.get_ready_alpha = self.get_ready_alpha - 1400
            if self.survive_pos_x >= 200 and self.survive_pos_x <= 220:
                if now - self.get_ready_update > 20:
                    self.survive_update = pg.time.get_ticks()
                    self.survive_pos_x = self.survive_pos_x - 1
                    self.get_ready.set_alpha(self.get_ready_alpha)
                    self.get_ready_pos_x = self.get_ready_pos_x - 24
                    self.get_ready_alpha = self.get_ready_alpha - 20
                    self.survive_alpha = self.survive_alpha + 20
            if self.survive_pos_x == 199:
                if now - self.survive_update > 800:
                    self.final_flash_ok = True

    def final_flash(self):
        if self.final_flash_ok == True:
            self.game.background_music = True
            now = pg.time.get_ticks()
            self.final_flash_real.blit(self.final_flash_surface, (0, 0))
            self.final_flash_real.set_alpha(self.final_flash_surface_alpha)
            if self.final_flash_surface_alpha < 255:
                if now - self.final_flash_surface_update > 30:
                    self.final_flash_surface_update = pg.time.get_ticks()
                    self.final_flash_surface_alpha = self.final_flash_surface_alpha + 10
                    if self.final_flash_surface_alpha >= 255:
                        self.final_flash_fade = True
                        self.final_flash_ok = False
                        self.survive_ok = False
                        self.get_ready_ok = False
                        self.portrait_ok = False
                        self.bars_ok = False
                        self.darkness_ok = False
        if self.final_flash_fade == True:
            now = pg.time.get_ticks()
            self.final_flash_real.blit(self.final_flash_surface, (0, 0))
            self.final_flash_real.set_alpha(self.final_flash_surface_alpha)
            if self.final_flash_surface_alpha > 0:
                if now - self.final_flash_surface_update > 20:
                    self.final_flash_surface_update = pg.time.get_ticks()
                    self.final_flash_surface_alpha = self.final_flash_surface_alpha - 20
                    if self.final_flash_surface_alpha <= 0:
                        self.kill()

    def blit_start_screen(self):
        if self.darkness_ok == True:
            self.game.screen.blit(self.darkness, (0, 0))
        if self.bars_ok == True:
            self.game.screen.blit(self.bars, (self.bars_pos_x, self.bars_pos_y))
            self.game.screen.blit(self.green_bar, (self.bars_pos_x, 77), special_flags=pg.BLEND_RGBA_SUB)
        if self.portrait_ok == True:
            self.game.screen.blit(self.portrait, (self.portrait_pos_x, 80), special_flags=pg.BLEND_RGB_MAX)
        if self.flash_up_ok == True or self.flash_down_ok == True:
            self.game.screen.blit(self.flash_real, (0, 0))
        if self.get_ready_ok == True:
            self.game.screen.blit(self.get_ready.convert_alpha(), (self.get_ready_pos_x, self.get_ready_pos_y))
        if self.survive_ok == True:
            self.game.screen.blit(self.survive.convert_alpha(), (self.survive_pos_x, self.survive_pos_y))
        if self.final_flash_ok == True or self.final_flash_fade == True:
            self.game.screen.blit(self.final_flash_real, (0, 0))

class Game_start_cutscene(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 2
        self.groups = game.intro
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.load_images()
        self.intro = True # Turns off when the entire intro cutscene is over.
        self.music_ok = False
        self.time_aid = 0 # Value to be used to time certain things better!
        self.trigger_update = 0
        self.trigger_count = 0
        # Sweat-drop scene
        self.sweat_scene_surface = pg.Surface((480, 360))
        self.sweat_scene_surface2 = pg.Surface((480, 360))
        self.sweat_scene_surface2.set_colorkey(BLACK)
        self.sweat_scene_ok = False  # Turns off when the sweat-drop scene is over.
        self.sweat_scene_overlay_ok = False # Obscures unwanted elements in de sweat_scene.
        self.sweat_scene_update = 0 # Keeps track of the time the sweat-drop scene is last updated.
        self.sweat_scene_current_frame = 0 # Keeps track of the current frame in the sweat-drop scene.
        # First text and dark figure
        self.dark_figure_ok = False
        self.dark_figure_alpha = 0
        self.dark_figure_update = 0
        self.goback = False
        # First flash transition into main background
        self.flash_ok = False
        self.flash_up_ok = True
        self.flash_down_ok =False
        self.flash_fade = False
        self.flash_surface = pg.Surface((480, 360))
        self.flash_surface.fill(WHITE)
        self.flash_real = pg.Surface((480, 360))
        self.flash_real.set_alpha(0)
        self.flash_surface_alpha = 0
        self.flash_surface_update = 0
        # Main Scrolling background
        self.scrolling_background = False
        self.clouds_pos = vec(0, -426)
        self.clouds_update = 0
        # Menu background
        self.menu_ok = False
        self.menu_left_pos = vec(-240, 0)
        self.menu_right_pos = vec(480, 0)
        self.menu_update = 0
        # Texts
        self.text_alpha = 0
        self.timeofbetrayal_pos = vec(140, 300)
        self.timeofbetrayal_update = 0
        self.timeofbetrayal_ok = False
        self.betrayal_alpha = 0
        self.blackscreen = pg.Surface((480, 360))  # To blit the texts on a black screen.
        self.blackscreen.fill(BLACK)
        self.theswordisall_ok = False
        self.theswordisall_update = 0
        self.straightthrough_ok = False
        self.straighthrough_update = 0
        self.finalchapter_ok = False
        self.finalchapter_update = 0
        self.goforbroke_ok = False
        self.goforbroke_update = 0
        self.getready_ok = False
        self.getready_update = 0
        # Artworks
        self.artwork_update = 0
        self.chrom_ok = False
        self.chrom_pos = vec(-232, 10)
        self.girl_ok = False
        self.girl_pos = vec(-232, 2)
        self.old_man_ok = False
        self.old_man_pos = vec(-232, 10)
        self.old_man_update = 0
        self.adol_1_ok = False
        self.adol_1_pos = vec(-540, 30)
        self.move_away = False # If true, the first 4 artworks move away from the screen
        self.adol_2_ok = False
        self.adol_2_pos = vec(820, 700)
        self.adol_2_movequick = False
        self.adol_2_moveslow = False
        self.adol_2_alpha = 255
        self.adol_3_ok = False
        self.fact_ok = False
        self.adol_3_pos = vec(-10, 360)
        self.fact_pos = vec(10, -370)
        self.eyeturn_ok = False
        self.eyeturn_surface = pg.Surface((480, 360))
        self.eyeturn_animation = False
        self.eyeturn_update = 0
        self.eyeturn_current_frame = 0
        self.eyeturn_start_animation = 0
        self.endtime = 0

    def load_images(self):
        self.sweat_drop_images = [self.game.spritesheet_adol_sweat_drop.get_image(0, 0, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 0, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(0, 375, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 375, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 0, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 375, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 0, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 375, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(0, 750, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(0, 1125, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 750, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(0, 1500, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 1125, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 750, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 1500, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 1125, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 750, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 1500, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 1125, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 1500, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 0, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 375, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 750, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 1125, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 1500, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(0, 1875, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(0, 2250, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 1875, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(501, 2250, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 1875, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1002, 2250, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 1875, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(1503, 2250, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 1875, 499, 373),
                                  self.game.spritesheet_adol_sweat_drop.get_image(2004, 1875, 499, 373),
                                  ]
        for frame in self.sweat_drop_images:
            pg.transform.scale(frame, (480, 360))

        self.sweat_overlay_image_raw = self.game.spritesheet_adol_sweat_drop.get_image(2004, 2250, 499, 373)
        self.sweat_overlay_image = pg.transform.scale(self.sweat_overlay_image_raw, (480, 360))
        self.sweat_overlay_image.set_colorkey(WHITE)

        # Dark figure image

        self.dark_figure_image = pg.image.load("intro_enemy.png").convert()

        # Main scrolling backgorund

        self.clouds = pg.image.load("Intro_clouds.png")

        # Text images

        self.text_thetimeofbetrayal = self.game.intro_texts.get_image(0, 0, 316, 24).convert()
        self.text_thetimeofbetrayal.set_colorkey(BLACK)
        self.text_getready = self.game.intro_texts.get_image(0, 25, 278, 22)
        self.text_goforbroke = self.game.intro_texts.get_image(0, 49 , 200, 20)
        self.text_finalchapter = self.game.intro_texts.get_image(0, 73, 440, 22)
        self.text_straightthrough = self.game.intro_texts.get_image(0, 97, 466, 22)
        self.text_yourswordisall = self.game.intro_texts.get_image(0, 121, 410, 22)

        #Character artwork
        self.chrom = pg.image.load("Intro_chrom.png")
        self.girl = pg.image.load("Intro_girl.png")
        self.oldman = pg.image.load("Intro_old_man.png")
        self.adol_1 = pg.image.load("intro_adol_1.png")
        self.adol_2 = pg.image.load("intro_adol_2.png").convert()
        self.adol_2.set_colorkey(BLACK)
        self.adol_3 = pg.image.load("intro_adol_3.png")
        self.fact = pg.image.load("intro_fact.png")

        #Eyeturn

        self.eye_turn_images = [self.game.spritesheet_adol_eyeturn.get_image(0, 0, 499, 373),
                                self.game.spritesheet_adol_eyeturn.get_image(501, 0, 499, 373),
                                self.game.spritesheet_adol_eyeturn.get_image(1002, 0, 499, 373),
                                self.game.spritesheet_adol_eyeturn.get_image(1503, 0, 499, 373)
                                ]
        for frame in self.eye_turn_images:
            pg.transform.scale(frame, (480, 360))

        # Final menu background
        self.menu_left = pg.image.load("Intro_menu_background_left.png")
        self.menu_right = pg.image.load("Intro_menu_background_right.png")

    def trigger(self):
        now = pg.time.get_ticks()
        if now - self.trigger_update > 80:
            self.trigger_update = pg.time.get_ticks()
            self.trigger_count += 1
            if self.trigger_count == 1:
                self.music()
            if self.trigger_count == 6:
                self.sweat_scene_ok = True
                self.sweat_scene_overlay_ok = True

    def music(self):
            self.game.soundtrack['intro'].play()

    def sweat_drop(self):

        if self.intro == True and self.sweat_scene_ok == True:
            now = pg.time.get_ticks()
            if now - self.sweat_scene_update > 80 and self.sweat_scene_current_frame != len(self.sweat_drop_images):
                self.current_image = self.sweat_drop_images[self.sweat_scene_current_frame]
                self.sweat_scene_surface.blit(self.current_image, (0, 0))
                self.sweat_scene_current_frame += 1

                self.sweat_scene_update = pg.time.get_ticks()

                self.sweat_scene_surface2.blit(self.sweat_overlay_image, (0,0))

                if self.sweat_scene_current_frame == len(self.sweat_drop_images):
                    self.sweat_scene_current_frame = 34
                    self.timeofbetrayal_ok = True

    def eyeturn(self):
        if self.eyeturn_ok == True and self.eyeturn_animation == False:
            now = pg.time.get_ticks()
            self.current_eyeturn_image = self.eye_turn_images[self.eyeturn_current_frame]
            self.eyeturn_surface.blit(self.current_eyeturn_image, (0, 0))
            if now - self.eyeturn_update > 600 and self.eyeturn_animation == False:
                self.eyeturn_update = pg.time.get_ticks()
                self.eyeturn_current_frame += 1
                self.eyeturn_start_animation = pg.time.get_ticks()
                self.eyeturn_animation = True

        if self.eyeturn_ok == True and self.eyeturn_animation == True:
            now = pg.time.get_ticks()
            self.current_eyeturn_image = self.eye_turn_images[self.eyeturn_current_frame]
            self.eyeturn_surface.blit(self.current_eyeturn_image, (0, 0))
            if now - self.eyeturn_start_animation > 100 and self.eyeturn_current_frame == 1:
                self.eyeturn_start_animation = pg.time.get_ticks()
                self.eyeturn_current_frame += 1
                self.endtime = pg.time.get_ticks()
            if now - self.eyeturn_start_animation > 130 and self.eyeturn_current_frame == 2:
                    print("ending")
                    self.eyeturn_current_frame = 3
                    self.current_eyeturn_image = self.eye_turn_images[self.eyeturn_current_frame]
                    self.endtime = pg.time.get_ticks()

                    self.eyeturn_surface.blit(self.current_eyeturn_image, (0, 0))
            if self.eyeturn_current_frame == 3 and now - self.endtime > 600:
                self.eyeturn_ok = False
                self.adol_3_ok = True
                self.fact_ok = True

    def text_placement(self):
        now = pg.time.get_ticks()
        if self.timeofbetrayal_ok == True:
            self.text_thetimeofbetrayal.set_alpha(self.betrayal_alpha)
            if now - self.timeofbetrayal_update > 20:
                self.timeofbetrayal_update = pg.time.get_ticks()
                if self.timeofbetrayal_pos[0] <= 170:
                    self.timeofbetrayal_pos[0] += 0.25
                if self.betrayal_alpha < 255:
                    self.betrayal_alpha += 5
                if self.timeofbetrayal_pos[0] > 154:
                    self.dark_figure_ok = True
        if self.theswordisall_ok == True:
            self.blackscreen.blit(self.text_yourswordisall, (40, 360/2))
            if now - self.theswordisall_update > 600:
                self.theswordisall_ok = False
                self.blackscreen.fill(BLACK)
                self.adol_1_ok = True
                self.flash_ok = True
        if self.straightthrough_ok == True:
            self.blackscreen.blit(self.text_straightthrough, (10, 360/2))
            if now - self.straighthrough_update > 600:
                self.straightthrough_ok = False
                self.blackscreen.fill(BLACK)
                self.flash_ok = True
                self.move_away = True
        if self.finalchapter_ok == True:
            self.blackscreen.blit(self.text_finalchapter, (10, 360/2))
            if now - self.finalchapter_update > 600:
                self.finalchapter_ok = False
                self.adol_2_ok = True
                self.adol_2_movequick = True
                self.blackscreen.fill(BLACK)
                self.flash_ok = True
        if self.goforbroke_ok == True:
            self.blackscreen.blit(self.text_goforbroke, (160, 360/2))
            if now - self.goforbroke_update > 600:
                self.goforbroke_ok = False
                self.blackscreen.fill(BLACK)
                self.adol_2_moveslow = True
                self.flash_ok = True
        if self.getready_ok == True:
            self.blackscreen.blit(self.text_getready, (130, 360/2))
            if now - self.getready_update > 600:
                self.getready_ok = False
                self.adol_2_ok = False
                self.blackscreen.fill(BLACK)
                self.eyeturn_ok = True
                self.eyeturn_update = pg.time.get_ticks()

    def artwork_placement(self):
        now = pg.time.get_ticks()
        if now - self.artwork_update > 10:
            self.artwork_update = pg.time.get_ticks()
            if self.move_away == False:
                if self.chrom_ok == True:
                    if self.chrom_pos[0] < 290:
                        self.chrom_pos[0] += 10
                    if self.chrom_pos[0] > 90:
                        self.girl_ok = True
                if self.girl_ok == True:
                    if self.girl_pos[0] < 90:
                        self.girl_pos[0] += 7
                    if self.girl_pos[0] > 40:
                        self.old_man_ok = True
                if self.old_man_ok == True:
                    if self.old_man_pos[0] < -50:
                        self.old_man_update = pg.time.get_ticks()
                        self.old_man_pos[0] += 7
                    if self.old_man_pos[0] == -50:
                        if now - self.old_man_update > 400:
                            self.theswordisall_ok = True
                            self.theswordisall_update = pg.time.get_ticks()
                            self.flash_ok = True
                            self.old_man_pos[0] = -51
                if self.adol_1_ok == True:
                    if self.adol_1_pos[0] < -150:
                        self.adol_1_pos[0] += 10
                    if self.adol_1_pos[0] == -150:
                        self.straighthrough_update = pg.time.get_ticks()
                        self.flash_ok = True
                        self.straightthrough_ok = True
                        self.adol_1_pos[0] = -151
            if self.move_away == True:
                self.adol_1_pos[1] += 4
                self.old_man_pos[0] -= 4
                self.chrom_pos[0] += 4
                self.girl_pos[1] -= 4
                if self.adol_1_pos[1] >= 320:
                    self.adol_1_ok = False
                    self.girl_ok = False
                    self.old_man_ok = False
                    self.chrom_ok = False
                    self.finalchapter_update = pg.time.get_ticks()
                    self.flash_ok = True
                    self.finalchapter_ok = True
                    self.move_away = False
            if self.adol_2_ok == True:
                self.adol_2.set_alpha(self.adol_2_alpha)
                if self.adol_2_movequick == True:
                    self.adol_2_pos[0] -= 10
                    self.adol_2_pos[1] -= 10
                if self.adol_2_moveslow == True:
                    self.adol_2_pos[0] -= 1
                    self.adol_2_pos[1] -= 1
                if self.adol_2_pos[1] == 20:
                    self.adol_2_moveslow = True
                    self.adol_2_movequick = False
                if self.adol_2_pos[1] == 10:
                    self.adol_2_pos[1] = 9
                    self.goforbroke_ok = True
                    self.flash_ok = True
                    self.adol_2_moveslow = False
                    self.goforbroke_update = pg.time.get_ticks()
                if self.adol_2_pos[1] < 7:
                    self.adol_2_alpha -= 2
                    if self.adol_2_alpha <= 4:
                        self.getready_update = pg.time.get_ticks()
                        self.adol_2_alpha = 0
                        self.flash_ok = True
                        self.adol_2_ok = False
                        self.getready_ok = True
            if self.adol_3_ok == True and self.adol_3_pos[1] > 140:
                self.adol_3_pos[1] -= 1
            if self.fact_ok == True and self.fact_pos[1] < -30:
                print(self.fact_pos[1])
                self.fact_pos[1] += 2
            if self.fact_ok == True and self.fact_pos[1] >= -30:
                self.menu_ok = True

    def dark_figure(self):
        now = pg.time.get_ticks()
        if self.dark_figure_ok == True:
            self.dark_figure_image.set_alpha(self.dark_figure_alpha)
            if self.dark_figure_alpha < 220 and self.goback == False:
                if now - self.dark_figure_update > 100:
                    self.dark_figure_update = pg.time.get_ticks()
                    self.dark_figure_alpha += 11
                    print(self.dark_figure_alpha)
                    if self.dark_figure_alpha >= 220:
                        self.goback = True
            if self.goback == True:
                print(self.dark_figure_alpha)
                if now - self.dark_figure_update > 55:
                    self.dark_figure_update = pg.time.get_ticks()
                    self.dark_figure_alpha -= 20
                    if self.dark_figure_alpha <= 140:
                        self.dark_figure_ok = False
                        self.sweat_scene_ok = False
                        self.timeofbetrayal_ok = False
                        self.flash_ok = True
                        self.chrom_ok = True
                        print("UPDATE??")

    def first_flash(self):
        if self.flash_ok == True:
            # print("FLASH")
            if self.flash_up_ok == True:
                now = pg.time.get_ticks()
                self.flash_real.blit(self.flash_surface, (0, 0))
                self.flash_real.set_alpha(self.flash_surface_alpha)
                if self.flash_surface_alpha < 255:
                    if now - self.flash_surface_update > 20:
                        self.flash_surface_update = pg.time.get_ticks()
                        self.flash_surface_alpha = self.flash_surface_alpha + 80
                        if self.flash_surface_alpha >= 255:
                            self.flash_surface_alpha = 255
                            self.flash_up_ok = False
                            self.flash_down_ok = True
                            self.scrolling_background = True
            if self.flash_down_ok == True:
                now = pg.time.get_ticks()
                self.flash_real.blit(self.flash_surface, (0, 0))
                self.flash_real.set_alpha(self.flash_surface_alpha)
                if self.flash_surface_alpha > 0:
                    if now - self.flash_surface_update > 20:
                        self.flash_surface_update = pg.time.get_ticks()
                        self.flash_surface_alpha = self.flash_surface_alpha - 55
                        if self.flash_surface_alpha <= 50:
                            self.flash_surface_alpha = 0
                            self.flash_down_ok = False
                            self.flash_up_ok = True
                            self.flash_ok = False

    def main_background(self):
        if self.scrolling_background == True:
            now = pg.time.get_ticks()
            if now - self.clouds_update > 24 and self.clouds_pos[1] <= 0:
                self.clouds_update = pg.time.get_ticks()
                self.clouds_pos[1] += 1

    def menu_background(self):

        if self.menu_ok == True:
            now = pg.time.get_ticks()
            if now - self.menu_update > 2:
                self.menu_update = pg.time.get_ticks()
                if self.menu_left_pos[0] != 0:
                    self.menu_left_pos[0] += 20
                    self.menu_right_pos[0] -= 20

    def blit_intro(self):
        if self.sweat_scene_ok == True:
            self.game.screen.blit(self.sweat_scene_surface, (0, 0))
        if self.sweat_scene_overlay_ok == True:
            self.game.screen.blit(self.sweat_scene_surface2, (0, 0))
        if self.dark_figure_ok == True:
            self.game.screen.blit(self.dark_figure_image, (0, 0))
        if self.scrolling_background == True:
            self.game.screen.blit(self.clouds, (self.clouds_pos[0], self.clouds_pos[1]))
        if self.timeofbetrayal_ok == True:
            self.game.screen.blit(self.text_thetimeofbetrayal, (self.timeofbetrayal_pos[0], self.timeofbetrayal_pos[1]))
        if self.chrom_ok == True:
            self.game.screen.blit(self.chrom, (self.chrom_pos[0], self.chrom_pos[1]))
        if self.girl_ok == True:
            self.game.screen.blit(self.girl, (self.girl_pos[0], self.girl_pos[1]))
        if self.old_man_ok == True:
            self.game.screen.blit(self.oldman, (self.old_man_pos[0], self.old_man_pos[1]))
        if self.adol_1_ok == True:
            self.game.screen.blit(self.adol_1, (self.adol_1_pos[0], self.adol_1_pos[1]))
        if self.adol_2_ok == True:
            self.game.screen.blit(self.adol_2, (self.adol_2_pos[0], self.adol_2_pos[1]))
        if self.theswordisall_ok == True:
            self.game.screen.blit(self.blackscreen, (0, 0))
        if self.straightthrough_ok == True:
            self.game.screen.blit(self.blackscreen, (0, 0))
        if self.finalchapter_ok == True:
            self.game.screen.blit(self.blackscreen, (0, 0))
        if self.goforbroke_ok == True:
            self.game.screen.blit(self.blackscreen, (0, 0))
        if self.getready_ok == True:
            self.game.screen.blit(self.blackscreen, (0, 0))
        if self.eyeturn_ok == True:
            self.game.screen.blit(self.eyeturn_surface, (0, 0))
        if self.fact_ok == True:
            self.game.screen.blit(self.fact, (self.fact_pos[0], self.fact_pos[1]))
        if self.adol_3_ok == True:
            self.game.screen.blit(self.adol_3, (self.adol_3_pos[0], self.adol_3_pos[1]))
        if self.menu_ok == True:
            self.game.screen.blit(self.menu_left, (self.menu_left_pos[0], 0))
            self.game.screen.blit(self.menu_right, (self.menu_right_pos[0], 0))
        if self.flash_ok == True:
            self.game.screen.blit(self.flash_real, (0, 0))

    def update(self):
        self.trigger()
        self.sweat_drop()
        self.main_background()
        self.menu_background()
        self.text_placement()
        self.artwork_placement()
        self.eyeturn()
        self.dark_figure()
        self.first_flash()
        self.blit_intro()

class Show_main_menu(pg.sprite.Sprite):
    def __init__(self, game):
        self._layer = 2
        self.groups = game.main_menu
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.load_images()

    def load_images(self):
        self.backdrop1 = pg.image.load("Intro_menu_background_left.png")
        self.backdrop2 = pg.image.load("Intro_menu_background_right.png")

    def update(self):
        self.blit_main_menu()

    def blit_main_menu(self):
        self.game.screen.blit(self.backdrop1, (0, 0))
        self.game.screen.blit(self.backdrop2, (240, 0))

class Show_win_screen(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.win_screen_group
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

    def update(self):
        self.game.screen.fill(WHITE)

class Show_game_over_screen(pg.sprite.Sprite):
    def __init__(self, game):
        self.groups = game.game_over
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.backdrop_ok = True
        self.backdrop_update = 0
        self.backdrop_alpha = 0
        self.backdrop_surface = pg.Surface((480, 360))
        # self.backdrop_surface.blit(self.game.screen, (0,0))
        self.gameover_ok = False
        self.gameover_alpha = 0
        self.gameover_pos = vec((480 / 2) - 122, (360 / 2) + 35)
        self.load_images()


    def load_images(self):
        self.backdrop = self.game.spritesheet_Game_start.get_image(3, 2, 481, 362)
        self.gameover = self.game.spritesheet_Game_start.get_image(484, 200, 245, 65)
        self.gameover.set_colorkey(BROWN)

    def backdrop_fadein(self):
        if self.backdrop_ok == True:
            now = pg.time.get_ticks()
            self.backdrop.set_alpha(self.backdrop_alpha)
            self.backdrop_surface.blit(self.backdrop, (0, 0))
            if self.backdrop_alpha < 250:
                if now - self.backdrop_update > 10:
                    print(self.backdrop_alpha)
                    self.backdrop_update = pg.time.get_ticks()
                    self.backdrop_alpha += 1
                if self.backdrop_alpha >= 40:
                    print("done")
                    self.gameover_ok = True


    def gameover_fadein(self):
        if self.gameover_ok == True:
            now = pg.time.get_ticks()
            self.gameover.set_alpha(self.gameover_alpha)
            if now - self.backdrop_update > 8 and self.gameover_alpha < 255:
                self.backdrop_update = pg.time.get_ticks()
                self.gameover_alpha += 5
                self.gameover_pos[1] -= 0.5


    def update(self):
        self.blit_game_over_screen()
        self.backdrop_fadein()
        self.gameover_fadein()

    def blit_game_over_screen(self):
        if self.backdrop_ok == True:
            self.game.screen.blit(self.backdrop_surface, (0, 0))

        if self.gameover_ok == True:
            self.game.screen.blit(self.gameover, (self.gameover_pos[0], self.gameover_pos[1]))

class Show_instructions(pg.sprite.Sprite):
    def __init__(self,game):
        self.groups = game.instructions
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.counter = game.instruction_counter
        self.load_images()

    def load_images(self):
        self.page_1_image = pg.image.load("InstructionsControls.png")
        self.page_1_image = pg.transform.smoothscale(self.page_1_image, (480, 360))
        self.page_2_image = pg.image.load("InstructionLifebar.png")
        self.page_2_image = pg.transform.smoothscale(self.page_2_image, (480, 360))

    def blit_instructions(self):
        self.game.screen.fill(BLACK)
        if self.counter == 0:
            self.game.screen.blit(self.page_1_image, (0,0))

        if self.counter == 1:
            self.game.screen.blit(self.page_2_image, (0,0))

    def update(self):
        self.blit_instructions()
