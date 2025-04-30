import time

import pygame

class variable:

    def __init__(self):

        self.pieces_recoltees = 0
        self.mouse_y = None
        self.mouse_x = None
        self.WhiteColor = None
        self.condition_lancement = False
        self.condition_choix_du_monde = False
        self.home = True
        self.bonus = False
        self.condition_magasin = False
        self.condition_locker = False
        self.niveau3 = None
        self.niveau2 = None
        self.niveau1 = None
        self.world_1_select = True
        self.world_2_select = False
        self.condition_monde2 = False
        self.message_erreur = False
        self.fond_accueil = pygame.image.load("Image_fond.webp")
        self.fond1 = pygame.image.load("1eme image fond underground blocus.webp")
        self.fond2 = pygame.image.load("2eme image fond undergrounds blocus.webp")
        self.fond3 = pygame.image.load("3eme image fond underground blocus.webp")
        self.world2_fond1 = pygame.image.load("1eme image 2eme monde.webp")
        self.world2_fond2 = pygame.image.load("2eme_image_2eme_monde.png")
        self.world2_fond3 = pygame.image.load("3eme_image_2eme_monde.png")
        self.world2_fond4 = pygame.image.load("4eme_image_2eme_monde.png")
        self.fond_magasin = pygame.image.load("Image_fond_magasin.webp")
        self.image_choixDuMonde = pygame.image.load("image_choixDuMonde.webp")
        self.image_casier = pygame.image.load("Image_fonc_casier.png")

        self.screen = pygame.display.set_mode((1200, 800))
        self.largeur_jauge = 0
        self.niveau = 1
        self.objectif_score = 5
        self.score = 0
        self.attemps = 1
        self.ancienne_variable = 1
        self.x_fond1 = -200
        self.x_fond2 = 1592
        self.x_fond3 = 3384
        self.level_finished = False
        self.pieces_utilisables = 2
        self.prob = set()
        self.world2_ground = 662
        self.saut_possible = True
        self.world2_niv2 = False
        self.world2_niv3 = False
        self.world2_niv1 = True
        self.world2_niv4 = False
        self.normal = True
        self.normal_color = (0, 255, 0)
        self.slowly = False
        self.slowly_color = (127, 0, 127)
        self.inversed_gravity = False
        self.inversed_gravity_color = (0, 200, 127,)
        self.jumper = pygame.draw.rect(self.screen, (127, 0, 127,), (640, 560, 20, 20))
        self.piece_taken = False

        self.title = pygame.font.SysFont('Courier', 55)
        self.Small_write = pygame.font.SysFont('Courier', 40)
        self.verySmall_write = pygame.font.SysFont('Trattello', 40)
        self.pourcent = pygame.font.SysFont('Trattello', 22)

        self.SkinColor_Buying_showing = False
        self.SkinColor_intialX = 570
        self.SkinColor_intialY = 360
        self.WhiteColor,self.RednColor,self.lightGreen_Color,self.BlueColor,self.Yello_Color  = (
            (255, 255, 255),(255, 0, 0),(0, 255, 0),(0, 0, 255),(255, 255, 0))
        self.Aqua_Color,self.Pink_Color,self.Gray_Color,self.DarkRed_Color,self.DarkGreen_Color = (
            (0, 255, 255),(255, 0, 255),(192, 192, 192),(128, 0, 0),(0, 128, 0))
        self.Purple_Color,self.DarkBlue_Color,self.DarkAqua_Color,self.Orange_Color,self.lightBlue_Color = (
            (128, 0, 128),(0, 0, 128),(0, 128, 128),(255, 165, 0),(0, 191, 255))
        self.lightPurple_Color, self.Black_Color, self.night_Color, self.Turquoise_Color, self.DarkOrange_Color = (
        147, 112, 219), (0, 0, 0), (25, 25, 112), (127, 255, 212), (184, 134, 11)

        self.WhiteColor_buying, self.RednColor_buying, self.lightGreen_Color_buying, self.BlueColor_buying, self.Yello_Color_buying = (
            False, False, False, False, False)
        self.Aqua_Color_buying, self.Pink_Color_buying, self.Gray_Color_buying, self.DarkRed_Color_buying, self.DarkGreen_Color_buying = (
            False, False, False, False, False)
        self.Purple_Color_buying, self.DarkBlue_Color_buying, self.DarkAqua_Color_buying, self.Orange_Color_buying, self.lightBlue_Color_buying = (
            False, False, False, False, False)
        self.lightPurple_Color_buying, self.Black_Color_buying, self.night_Color_buying, self.Turquoise_Color_buying, self.DarkOrange_Color_buying = (
            False, False, False, False, False)

    def mouse_getpos(self):
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

    def initial(self):
        self.fond_accueil = pygame.image.load("Image_fond.webp")
        self.fond1 = pygame.image.load("1eme image fond underground blocus.webp")
        self.fond2 = pygame.image.load("2eme image fond undergrounds blocus.webp")
        self.fond3 = pygame.image.load("3eme image fond underground blocus.webp")
        self.objectif_score = 5
        self.niveau = 1
        self.score = 0
        self.attemps = 0
        self.largeur_jauge = 0
        self.level_finished = False
        self.x_fond1 = -200
        self.x_fond2 = 1592
        self.x_fond3 = 3384
        self.pieces_recoltees = 0
        self.world2_niv2 = False
        self.world2_niv3 = False
        self.world2_niv1 = True
        self.world2_niv4 = False
        self.normal = True
        #self.normal_color = (0, 255, 0)
        self.slowly = False
        self.slowly_color = (127, 0, 127)
        self.SkinColor_Buying_showing = False

    def world1_init(self):
        self.niveau = 1
        self.x_fond1 = -200
        self.x_fond2 = 1592
        self.x_fond3 = 3384

    def new_barriere(self):
        self.score += 1

    def new_level(self):
        self.level_finished = True
        self.score = 0
        self.niveau += 1
        self.largeur_jauge = 0

    def fin_monde(self):
        self.condition_lancement = False
        self.home = True
        self.condition_monde1 = False
        self.message_erreur = False

    def retour_menu(self):
        self.condition_lancement = False
        self.screen.fill((0, 0, 0))
        self.home = True

    def choix_monde_1(self):
        self.condition_choix_du_monde = False
        self.home = True
        self.world_1_select = True
        self.world_2_select = False

    def choix_monde_2(self):
        if self.condition_monde2:
            self.condition_choix_du_monde = False
            self.home = True
            self.world_2_select = True
            self.world_1_select = False
        else:
            self.condition_choix_du_monde = False
            self.home = True

    def structure_world2(self):
        if self.world2_niv1:
            self.screen.blit(self.world2_fond1, (self.x_fond1, 0))# fond d'ecran_niv1

            pygame.draw.rect(self.screen, (0, 0, 255), (360, 640, 100, 20))#plateformes niv1

            pygame.draw.rect(self.screen, (0, 0, 255,), (0, 700, 290, 20))#sol niv1
            pygame.draw.rect(self.screen, (0, 0, 255,), (625, 700, 310, 20))
            pygame.draw.rect(self.screen, (0, 0, 255,), (1085, 700, 290, 20))

        if self.world2_niv2:
            self.screen.blit(self.world2_fond2, (self.x_fond1, 0))# fond d'ecran_niv2

            pygame.draw.rect(self.screen, (0, 0, 255,), (0, 700, 250, 20))#sol niv2
            pygame.draw.rect(self.screen, (0, 0, 255,), (340, 640, 80, 20))
            pygame.draw.rect(self.screen, (0, 0, 255,), (510, 580, 150, 20))


        if self.world2_niv3:
            self.screen.blit(self.world2_fond3, (self.x_fond1, 0))  # fond d'ecran_niv3

            pygame.draw.rect(self.screen, (0, 0, 255,), (0, 700, 290, 20))
            pygame.draw.rect(self.screen, (0, 0, 255,), (350, 268, 80, 20))
            pygame.draw.rect(self.screen, (0, 0, 255,), (900, 700, 20, 20))

        if self.world2_niv4:
            self.screen.blit(self.world2_fond4, (self.x_fond1, 0))  # fond d'ecran_niv4

            pygame.draw.rect(self.screen, (0, 0, 255,), (-200, 700, 290, 20))
            pygame.draw.rect(self.screen, (0, 0, 255,), (940, 700, 100, 20))


    def skin_color(self):
        pygame.draw.rect((self.screen), (0, 0, 0), (560, 350, 160, 130))
        self.WhiteColor_rect = pygame.draw.rect((self.screen), (255, 255, 255),
                                           (self.SkinColor_intialX, self.SkinColor_intialY, 20, 20))
        self.RednColor_rect = pygame.draw.rect((self.screen), (255, 0, 0),
                                          (self.SkinColor_intialX + 30 * 1, self.SkinColor_intialY, 20, 20))
        self.lightGreen_Color_rect = pygame.draw.rect((self.screen), ((0, 255, 0)),
                                                 (self.SkinColor_intialX + 30 * 2, self.SkinColor_intialY, 20, 20))
        self.BlueColor_rect = pygame.draw.rect((self.screen), ((0, 0, 255)),
                                         (self.SkinColor_intialX + 30 * 3, self.SkinColor_intialY, 20, 20))
        self.Yello_Color_rect = pygame.draw.rect((self.screen), ((255, 255, 0)),
                                               (self.SkinColor_intialX + 30 * 4, self.SkinColor_intialY, 20, 20))

        self.Aqua_Color_rect = pygame.draw.rect((self.screen), ((0, 255, 255)),
                                                (self.SkinColor_intialX, self.SkinColor_intialY + 30 * 1, 20, 20))
        self.Pink_Color_rect = pygame.draw.rect((self.screen), ((255, 0, 255)),
                                            (self.SkinColor_intialX + 30 * 1, self.SkinColor_intialY + 30 * 1, 20, 20))
        self.Gray_Color_rect = pygame.draw.rect((self.screen), ((192, 192, 192)),
                                                (self.SkinColor_intialX + 30 * 2, self.SkinColor_intialY + 30 * 1, 20,
                                                 20))
        self.DarkRed_Color_rect = pygame.draw.rect((self.screen), ((128, 0, 0)),
                                            (self.SkinColor_intialX + 30 * 3, self.SkinColor_intialY + 30 * 1, 20, 20))
        self.DarkGreen_Color_rect = pygame.draw.rect((self.screen), ((0, 128, 0)),
                                                (self.SkinColor_intialX + 30 * 4, self.SkinColor_intialY + 30 * 1, 20,
                                                 20))

        self.Purple_Color_rect = pygame.draw.rect((self.screen), ((128, 0, 128)),
                                                   (self.SkinColor_intialX, self.SkinColor_intialY + 30 * 2, 20, 20))
        self.DarkBlue_Color_rect = pygame.draw.rect((self.screen), ((0, 0, 128)), (
        self.SkinColor_intialX + 30 * 1, self.SkinColor_intialY + 30 * 2, 20, 20))
        self.DarkAqua_Color_rect = pygame.draw.rect((self.screen), ((0, 128, 128)), (
        self.SkinColor_intialX + 30 * 2, self.SkinColor_intialY + 30 * 2, 20, 20))
        self.Orange_Color_rect = pygame.draw.rect((self.screen), ((255, 165, 0)),
                                           (self.SkinColor_intialX + 30 * 3, self.SkinColor_intialY + 30 * 2, 20, 20))
        self.lightBlue_Color_rect = pygame.draw.rect((self.screen), (0, 191, 255),
                                           (self.SkinColor_intialX + 30 * 4, self.SkinColor_intialY + 30 * 2, 20, 20))

        self.lightPurple_Color_rect = pygame.draw.rect((self.screen), (147, 112, 219),
                                               (self.SkinColor_intialX, self.SkinColor_intialY + 30 * 3, 20, 20))
        self.Black_Color_rect = pygame.draw.rect((self.screen), (0, 0, 0),
                                           (self.SkinColor_intialX + 30 * 1, self.SkinColor_intialY + 30 * 3, 20, 20))
        self.night_Color_rect = pygame.draw.rect((self.screen), (25, 25, 112),
                                           (self.SkinColor_intialX + 30 * 2, self.SkinColor_intialY + 30 * 3, 20, 20))
        self.Turquoise_Color_rect = pygame.draw.rect((self.screen), (127, 255, 212),
                                           (self.SkinColor_intialX + 30 * 3, self.SkinColor_intialY + 30 * 3, 20, 20))
        self.DarkOrange_Color_rect = pygame.draw.rect((self.screen), (184, 134, 11),
                                           (self.SkinColor_intialX + 30 * 4, self.SkinColor_intialY + 30 * 3, 20, 20))
    def structure_magasin(self):
        self.screen.blit(self.fond_magasin, (-200, 0))
        self.back_magasin = pygame.draw.rect(self.screen, (255, 0, 0), (0, 5, 65, 75))
        self.screen.blit(self.verySmall_write.render('Back', False, (0, 0, 0)), (0, 25))
        pygame.draw.rect((self.screen), (255, 255, 255), (160, 200, 250, 50))
        pygame.draw.rect((self.screen), (255, 255, 255), (560, 200, 250, 50))
        self.screen.blit(self.Small_write.render("2eme MONDE", False, (220, 0, 0)), (165, 205))
        self.screen.blit(self.Small_write.render("Skin Color", False, (220, 0, 0)), (565, 205))
        self.condition_monde2_rect = pygame.draw.rect((self.screen), (255, 255, 255), (200, 260, 150, 50))
        self.condition_SkinColor_Buying = pygame.draw.rect((self.screen), (255, 255, 255), (600, 260, 150, 50))
        self.screen.blit(self.verySmall_write.render("5 pieces", False, (220, 0, 0)), (220, 270))
        self.screen.blit(self.verySmall_write.render("2 pieces", False, (220, 0, 0)), (620, 270))
        if self.SkinColor_Buying_showing:
            self.skin_color()

    def theBuyingofthteskincolor(self):
        if self.WhiteColor_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.WhiteColor_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.RednColor_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.RednColor_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.lightGreen_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.lightGreen_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.BlueColor_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.BlueColor_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Yello_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Yello_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Aqua_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Aqua_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Pink_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Pink_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Gray_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Gray_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.DarkRed_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.DarkRed_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.DarkGreen_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.DarkGreen_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Purple_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Purple_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.DarkBlue_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.DarkBlue_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.DarkAqua_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.DarkAqua_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Orange_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Orange_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.lightBlue_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.lightBlue_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.lightPurple_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.lightPurple_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Black_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Black_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.night_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.night_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.Turquoise_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.Turquoise_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2
        if self.DarkOrange_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0]and self.pieces_utilisables >= 2:
            self.DarkOrange_Color_buying = True
            time.sleep(0.5)
            self.pieces_utilisables -= 2

    def SkinColor_dress(self):
        if self.WhiteColor_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.WhiteColor_buying:
            self.normal_color = self.WhiteColor
        if self.RednColor_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.RednColor_buying:
            self.normal_color = self.RednColor
        if self.lightGreen_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.lightGreen_Color_buying:
            self.normal_color = self.lightGreen_Color
        if self.BlueColor_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.BlueColor_buying:
            self.normal_color = self.BlueColor
        if self.Yello_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Yello_Color_buying:
            self.normal_color = self.Yello_Color
        if self.Aqua_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Aqua_Color_buying:
            self.normal_color = self.Aqua_Color
        if self.Pink_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Pink_Color_buying:
            self.normal_color = self.Pink_Color
        if self.Gray_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Gray_Color_buying:
            self.normal_color = self.Gray_Color
        if self.DarkRed_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.DarkRed_Color_buying:
            self.normal_color = self.DarkRed_Color
        if self.DarkGreen_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.DarkGreen_Color_buying:
            self.normal_color = self.DarkGreen_Color
        if self.Purple_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Purple_Color_buying:
            self.normal_color = self.Purple_Color
        if self.DarkBlue_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.DarkBlue_Color_buying:
            self.normal_color = self.DarkBlue_Color
        if self.DarkAqua_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.DarkAqua_Color_buying:
            self.normal_color = self.DarkAqua_Color
        if self.Orange_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Orange_Color_buying:
            self.normal_color = self.Orange_Color
        if self.lightBlue_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.lightBlue_Color_buying:
            self.normal_color = self.lightBlue_Color
        if self.lightPurple_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.lightPurple_Color_buying:
            self.normal_color = self.lightPurple_Color
        if self.Black_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Black_Color_buying:
            self.normal_color = self.Black_Color
        if self.night_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.night_Color_buying:
            self.normal_color = self.night_Color
        if self.Turquoise_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.Turquoise_Color_buying:
            self.normal_color = self.Turquoise_Color
        if self.DarkOrange_Color_rect.collidepoint(self.mouse_x, self.mouse_y) and pygame.mouse.get_pressed()[0] and self.DarkOrange_Color_buying:
            self.normal_color = self.DarkOrange_Color
