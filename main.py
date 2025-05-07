import random
import time
import pygame
pygame.init()


from personnage import Perso
from Rect import Rect
from variable import variable


objectif_x = -400
trying = 0
pygame.display.set_caption("undergrounds blocus")
pygame.display.set_icon(pygame.image.load("Icone.webp"))

clock = pygame.time.Clock()
variable = variable()
joueur = Perso()
rect = Rect()

variable.screen.blit(variable.fond_accueil, (-200, 0))
running = True
prob = set()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    variable.mouse_getpos()
    key = pygame.key.get_pressed()
    #print(variable.mouse_x, variable.mouse_y)
    if variable.home:  #acceuil du jeu
        joueur.__init__()
        variable.initial()
        variable.screen.blit(variable.fond_accueil, (-200, 0))
        demarrage = pygame.draw.rect(variable.screen, (255, 255, 255), (130, 237.5, 385, 68))
        world_choice= pygame.draw.rect(variable.screen, (255, 255, 255), (780, 655, 385, 68))
        magasin = pygame.draw.rect(variable.screen, (255, 255, 255), (900, 170, 200, 68))
        locker = pygame.draw.rect(variable.screen, (255, 255, 255), (80, 650, 200, 68))
        variable.screen.blit(variable.title.render("underground's blocus", False, (255, 255, 255)), (50, 50))
        if demarrage.collidepoint(variable.mouse_x, variable.mouse_y):
                pygame.draw.ellipse(variable.screen, (255, 0, 0), (70, 245, 50, 50))
        if world_choice.collidepoint(variable.mouse_x, variable.mouse_y):
                pygame.draw.ellipse(variable.screen, (255, 0, 0), (720, 665, 50, 50))
        if magasin.collidepoint(variable.mouse_x, variable.mouse_y):
                pygame.draw.ellipse(variable.screen, (255, 0, 0), (840, 180, 50, 50))
        if locker.collidepoint(variable.mouse_x, variable.mouse_y):
                pygame.draw.ellipse(variable.screen, (255, 0, 0), (20, 660.5, 50, 50))
        if variable.world_1_select:
            variable.screen.blit(variable.Small_write.render("Monde 1", False, (0, 0, 220)), (950, 50))
        if variable.world_2_select and not variable.message_erreur:
            variable.screen.blit(variable.Small_write.render("Monde 2", False, (220, 0, 0)), (950, 50))
        if variable.world_2_select and variable.message_erreur:
            variable.screen.blit(variable.Small_write.render("Monde indisponible", False, (220, 0, 0)), (750, 150))
        variable.screen.blit(variable.Small_write.render("démarrer le jeu", False, (0, 0, 0)), (145, 250))
        variable.screen.blit(variable.Small_write.render("choix du monde", False, (0, 0, 0)), (800, 670))
        variable.screen.blit(variable.Small_write.render("magasin", False, (0, 0, 0)), (920, 180))
        variable.screen.blit(variable.Small_write.render("casier", False, (0, 0, 0)), (100, 660))
        if pygame.mouse.get_pressed()[0] and demarrage.collidepoint(variable.mouse_x, variable.mouse_y) and variable.world_1_select:
            variable.condition_monde1 = True
            variable.condition_lancement = True
            variable.home = False
        if pygame.mouse.get_pressed()[0] and demarrage.collidepoint(variable.mouse_x, variable.mouse_y) and variable.world_2_select:
            variable.condition_lancement = True
            variable.home = False
        if pygame.mouse.get_pressed()[0] and world_choice.collidepoint(variable.mouse_x, variable.mouse_y):
            variable.condition_choix_du_monde = True
        if pygame.mouse.get_pressed()[0] and magasin.collidepoint(variable.mouse_x, variable.mouse_y):
            variable.condition_magasin = True
            variable.home = False
        if pygame.mouse.get_pressed()[0] and locker.collidepoint(variable.mouse_x, variable.mouse_y):
            variable.condition_locker = True
            variable.home = False


    affichage_level = pygame.font.SysFont('Trattatello', 100)


    if variable.condition_lancement:#lancement du jeu
        if variable.world_1_select:
            if variable.niveau == 4:
                variable.fin_monde()
                variable.pieces_utilisables += variable.pieces_recoltees
                variable.world1_init()
            if variable.niveau < variable.objectif_score:
                variable.screen.fill((0, 0, 0))
                variable.ancienne_variable += 1
            if variable.niveau > variable.ancienne_variable:
                variable.screen.blit(affichage_level.render(("niveau " + str(variable.niveau)), False, (255, 255, 255)),(400, 400))
                variable.screen.fill((0, 0, 0))
                variable.ancienne_variable += 1
            if variable.score == variable.objectif_score:
                variable.new_level()
                rect.giant_ecart -= 7
                rect.hauteur_bonus += 1.5
                joueur.nouvelles_dimensions_joueur()
            if variable.level_finished:
                variable.x_fond1 -= rect.speed
                variable.x_fond2 -= rect.speed
                variable.x_fond3 -= rect.speed

            if variable.niveau == 2 and variable.x_fond1 < -1992:
                variable.level_finished = False
            if variable.niveau == 3 and variable.x_fond1 < -3784:
                variable.level_finished = False

            variable.screen.blit(variable.fond1, (variable.x_fond1, 0))
            variable.screen.blit(variable.fond2, (variable.x_fond2, 0))
            variable.screen.blit(variable.fond3, (variable.x_fond3, 0))

            if key[pygame.K_UP]:
                joueur.haut(variable)
            if key[pygame.K_DOWN]:
                joueur.bas()
            if rect.x > objectif_x:
                rect.x -= rect.speed

            player = pygame.draw.rect(variable.screen, variable.normal_color,
                                      (joueur.x, joueur.y, joueur.largeur, joueur.hauteur))
            if rect.x <= objectif_x:
                joueur.vitesse += 0.3
                rect.MoveRect()
                rect.speed += 0.38
                variable.new_barriere()
                variable.prob = random.randint(1, 5)
                # prob = 1
                # print(prob)
                if variable.prob == 2 or variable.prob == 3 or variable.prob == 4:
                    rect.hauteur1 = 530
                if variable.prob == 1:
                    rect.y1 = 400
                    rect.hauteur1 = rect.hauteur_bonus
                rect.y2 = rect.y1 - rect.giant_ecart
                variable.largeur_jauge += 40
                if variable.prob == 2 or variable.prob == 3:
                    variable.bonus = False
                if variable.prob == 1:
                    variable.bonus = True
            if variable.bonus:
                piece = pygame.draw.ellipse(variable.screen, (255, 215, 0), (rect.x, 735, 25, 40))
                pygame.draw.ellipse(variable.screen, (230, 190, 0), (rect.x + 5, 745, 15, 30))
                if player.colliderect(piece):
                    variable.pieces_recoltees += 1
                    variable.bonus = False

            rect1 = pygame.draw.rect(variable.screen, (rect.red, rect.green, rect.blue),
                                          (rect.x, rect.y1, 250, rect.hauteur1))
            rect2 = pygame.draw.rect(variable.screen, (rect.red, rect.green, rect.blue),
                                          (rect.x, rect.y2, 250, rect.hauteur2))
            variable.barriere1 = pygame.draw.rect(variable.screen, (255, 0, 0,), (0, 780, 1600, 20))
            variable.barriere2 = pygame.draw.rect(variable.screen, (255, 0, 0,), (0, 0, 1600, 20))

            variable.screen.blit(
                variable.verySmall_write.render('  barriere n°: ' + str(variable.score), False, (255, 255, 255)),
                (rect.x - 10, rect.y1))
            QuitGame_world1 = pygame.draw.rect(variable.screen, (255, 0, 0), (0, 5, 65, 75))
            variable.screen.blit(variable.verySmall_write.render('Exit', False, (0, 0, 0)), (0, 25))
            back_world1 = pygame.draw.rect(variable.screen, (255, 0, 0), (0, 90, 65, 75))
            variable.screen.blit(variable.verySmall_write.render('Back', False, (0, 0, 0)), (0, 100))
            variable.screen.blit(
                variable.verySmall_write.render(("attemps: " + str(variable.attemps)), False, (255, 255, 255)), (700, 25))
            variable.screen.blit(
                variable.verySmall_write.render(("pièces: " + str(variable.pieces_recoltees)), False, (255, 255, 255)), (900, 25))

            variable.screen.blit(
                variable.verySmall_write.render(("niveau: " + str(variable.niveau)), False, (255, 255, 255)), (150, 25))
            pygame.draw.rect(variable.screen, (255, 255, 255), (355, 45, 240, 30))
            variable.screen.blit(
                pygame.font.SysFont('Trattello', 22).render(str(variable.largeur_jauge / 2) + "%", False, (0, 0, 0)),
                (357, 55))
            pygame.draw.rect(variable.screen, (0, 0, 255), (400, 50, variable.largeur_jauge, 20))

            if player.colliderect(variable.barriere1) or player.colliderect(variable.barriere2):
                joueur.initial()
                rect.initial()
                y2 = -100
                variable.attemps += 1
                variable.world1_init()
            if rect1.colliderect(player) or rect2.colliderect(player):
                joueur.initial()
                rect.initial()
                y2 = -100
                variable.attemps += 1
                variable.world1_init()
            if pygame.mouse.get_pressed()[0] and QuitGame_world1.collidepoint(variable.mouse_x, variable.mouse_y):
                running = False
            if pygame.mouse.get_pressed()[0] and back_world1.collidepoint(variable.mouse_x, variable.mouse_y):
                variable.retour_menu()

        if variable.world_2_select:
            variable.structure_world2()
            pygame.draw.rect(variable.screen, (255, 255, 255), (718, 30, 250, 30))
            variable.screen.blit(pygame.font.SysFont('Trattello', 22).render(str(variable.largeur_jauge / 2) + "%", False, (0, 0, 0)),(720, 40))
            pygame.draw.rect(variable.screen, (0, 0, 255), (763, 35, variable.largeur_jauge, 20))

            if variable.slowly:
                joueur_color = variable.slowly_color
            elif variable.inversed_gravity:
                joueur_color = variable.inversed_gravity_color
            else:
                joueur_color = variable.normal_color

            QuitGame_world2 = pygame.draw.rect(variable.screen, (255, 0, 0), (0, 0, 65, 70))
            variable.screen.blit(variable.verySmall_write.render('Exit', False, (0, 0, 0)), (0, 20))
            back_world2 = pygame.draw.rect(variable.screen, (255, 0, 0), (0, 80, 65, 70))
            variable.screen.blit(variable.verySmall_write.render('Back', False, (0, 0, 0)), (0, 100))

            variable.screen.blit(variable.verySmall_write.render('Pieces : ' + str(variable.pieces_recoltees), False, (0, 0, 0)), (200, 30))

            variable.screen.blit(variable.verySmall_write.render('Niveau : ' + str(variable.niveau), False, (0, 0, 0)), (460, 30))

            if QuitGame_world2.collidepoint(variable.mouse_x, variable.mouse_y) and pygame.mouse.get_pressed()[0]:
                running = False
            if back_world2.collidepoint(variable.mouse_x, variable.mouse_y) and pygame.mouse.get_pressed()[0]:
                variable.condition_lancement = False
                variable.home = True
                variable.initial()

            player_world2 = pygame.draw.rect(variable.screen, joueur_color,
                                             (joueur.x, joueur.y, joueur.largeur, joueur.hauteur))

            if variable.world2_niv1:
                variable.niveau = 1
                if (joueur.x >= 335 and joueur.x <= 460):
                    variable.world2_ground = 602
                elif (joueur.x > 290 and joueur.x < 335) or (joueur.x > 460 and joueur.x < 600) or (joueur.x >= 935 and joueur.x <= 1060):
                    variable.world2_ground = 1000
                else:
                    variable.world2_ground = 662
                if joueur.x > 1178 and joueur.y <= variable.world2_ground:
                    variable.world2_niv2 = True
                    variable.world2_niv1 = False
                    joueur.initial()
                    variable.normal = True
                    variable.slowly = False
                    variable.largeur_jauge += 50

            if variable.world2_niv2:
                variable.niveau = 2
                if not variable.piece_taken:
                    piece = pygame.draw.ellipse(variable.screen, (255, 215, 0), (1007, 700, 20, 30))
                    if player_world2.colliderect(piece):
                        variable.pieces_recoltees += 1
                        variable.piece_taken = True
                border = pygame.draw.rect(variable.screen, (255, 0, 0,), (1180, 0, 20, 735))
                slowly_cube = pygame.draw.rect(variable.screen, (127, 0, 127,), (640, 560, 20, 20))

                if joueur.x >= 315 and joueur.x <= 420:
                    variable.world2_ground = 602
                elif joueur.x >= 485 and joueur.x <= 660:
                    variable.world2_ground = 542
                elif (joueur.x > 250 and joueur.x < 340) or (joueur.x > 420 and joueur.x < 510) or joueur.x > 660 :
                    variable.world2_ground = 1000
                else:
                    variable.world2_ground = 662

                if joueur.x > 1178 and joueur.y <= variable.world2_ground:
                    variable.world2_niv2 = False
                    variable.world2_niv3 = True
                    joueur.initial()
                    variable.normal = True
                    variable.slowly = False
                    variable.largeur_jauge += 50
                    variable.piece_taken = False

                if  player_world2.colliderect(border):
                    joueur.initial()
                    variable.normal = True
                    variable.slowly = False
                    variable.piece_taken = False
                    variable.pieces_recoltees = 0
                if player_world2.colliderect(slowly_cube):
                    variable.slowly = True
                    variable.normal = False

            if variable.world2_niv3:
                variable.niveau = 3
                jumper = pygame.draw.rect(variable.screen, (0, 255, 255,), (200, 680, 90, 20))
                if not variable.piece_taken:
                    piece = pygame.draw.ellipse(variable.screen, (255, 215, 0), (635, 270, 20, 30))
                    if player_world2.colliderect(piece):
                        variable.pieces_recoltees += 1
                        variable.piece_taken = True

                if joueur.x >= 325 and joueur.x <= 430:
                    variable.world2_ground = 230
                elif (joueur.x > 1050) or (joueur.x >= 290 and joueur.x <= 875) or (joueur.x >= 920 and joueur.x <= 1020):
                    variable.world2_ground = 1000
                else:
                    variable.world2_ground = 662
                if player_world2.colliderect(jumper):
                    joueur.y -= 564

                if joueur.x > 1178 and joueur.y <= variable.world2_ground:
                    variable.world2_niv3 = False
                    variable.world2_niv4 = True
                    variable.normal = True
                    variable.slowly = False
                    joueur.initial()
                    variable.largeur_jauge += 50
                    variable.piece_taken = False

            if variable.world2_niv4:
                variable.niveau = 4
                if not variable.piece_taken:
                    piece = pygame.draw.ellipse(variable.screen, (255, 215, 0), (350, 215, 20, 30))
                    if player_world2.colliderect(piece):
                        variable.pieces_recoltees += 1
                        variable.piece_taken = True
                inversed_gravity_cube = pygame.draw.rect(variable.screen, (0, 200, 127,), (250, 665, 20, 20))
                normal_gravity_cube = pygame.draw.rect(variable.screen, (variable.normal_color), (510, 101, 20, 20))
                last_cube = pygame.draw.rect(variable.screen, (0, 0, 255,), (620, 700, 140, 20))
                dash_cube = pygame.draw.rect(variable.screen, (255, 0, 127,), (845, 650, 20, 20))
                if (joueur.x > 90 and joueur.x < 595) or (joueur.x > 760 and joueur.x < 915) or joueur.x > 1040 :
                    variable.world2_ground = 1000
                else:
                    variable.world2_ground = 662
                if dash_cube.colliderect(player_world2) and joueur.x < 845:
                    joueur.x += 75

                if inversed_gravity_cube.colliderect(player_world2):
                    variable.inversed_gravity = True
                    variable.normal = False
                if normal_gravity_cube.colliderect(player_world2):
                    variable.inversed_gravity = False
                    variable.normal = True

                if joueur.y > 662 and last_cube.colliderect(player_world2):
                    joueur.y = 662

                if joueur.x > 1178 and joueur.y <= variable.world2_ground:
                    variable.normal = True
                    variable.inversed_gravity = False


                if variable.niveau == 4 and joueur.x > 1178 and joueur.y <= variable.world2_ground:
                    variable.world2_niv4 = False
                    variable.world2_niv1 = True
                    variable.normal = True
                    variable.retour_menu()
                    variable.pieces_utilisables += variable.pieces_recoltees
                    variable.piece_taken = False

            if variable.inversed_gravity:
                joueur.y -= 9
            if joueur.y != variable.world2_ground:
                if variable.normal:
                    joueur.y += 4
                if variable.slowly:
                    joueur.y += 2

            if joueur.y < variable.world2_ground:
                variable.saut_possible = False
            if joueur.y == variable.world2_ground:
                variable.saut_possible = True
            if key[pygame.K_UP] and variable.saut_possible:
                joueur.haut_world2()
            if key[pygame.K_DOWN] and joueur.y < 1.4:
                joueur.bas_world2()
            if key[pygame.K_LEFT]:
                joueur.gauche()
            if key[pygame.K_RIGHT]:
                if variable.niveau == 4 and joueur.x > 620 and joueur.y < 529:
                    joueur.x -= joueur.vitesse
                joueur.droite()
            if joueur.y < 0:
                joueur.initial()
                variable.world2_niv1 = True
                variable.world2_niv2, variable.world2_niv3, variable.world2_niv4 = False, False, False
                variable.normal = True
                variable.slowly = False
                variable.inversed_gravity = False
                variable.piece_taken = False
                variable.pieces_recoltees = 0
                variable.largeur_jauge = 0
            if joueur.y > 762:
                variable.world2_niv1 = True
                variable.world2_niv2, variable.world2_niv3, variable.world2_niv4 = False, False, False
                joueur.initial()
                variable.normal = True
                variable.slowly = False
                variable.inversed_gravity = False
                variable.piece_taken = False
                variable.pieces_recoltees = 0
                variable.largeur_jauge = 0


    if variable.condition_choix_du_monde:               #lobby_choix_monde
        variable.screen.blit(variable.image_choixDuMonde, (-300, 0))
        back_choixmonde = pygame.draw.rect(variable.screen, (255, 0, 0), (0, 0, 85, 65))
        variable.screen.blit(variable.verySmall_write.render('back', False, (0, 0, 0)), (0, 10))

        if pygame.mouse.get_pressed()[0] and back_choixmonde.collidepoint(variable.mouse_x, variable.mouse_y):
            variable.condition_choix_du_monde = False
            variable.home = True
        variable.screen.blit(variable.title.render("choix du monde", False, (255, 255, 255)), (350, 50))
        world_1 = pygame.draw.rect(variable.screen, (0, 0, 255), (150, 380, 150, 100))
        variable.screen.blit(variable.Small_write.render('monde 1', False, (0, 0, 255)), (150, 480))

        if pygame.mouse.get_pressed()[0] and world_1.collidepoint(variable.mouse_x, variable.mouse_y):
            variable.choix_monde_1()
        world_2 = pygame.draw.rect(variable.screen, (255, 0, 0), (950, 380, 150, 100))
        variable.screen.blit(variable.Small_write.render('monde 2', False, (255, 0, 0)), (950, 480))
        if pygame.mouse.get_pressed()[0] and world_2.collidepoint(variable.mouse_x, variable.mouse_y) and variable.condition_monde2:
            variable.choix_monde_2()
        if pygame.mouse.get_pressed()[0] and world_2.collidepoint(variable.mouse_x, variable.mouse_y) and not variable.condition_monde2:
            variable.screen.blit(variable.title.render("monde indisponible pour l'instant", False, (220, 0, 220)), (30, 600))

    if variable.condition_magasin:
        variable.structure_magasin()
        variable.screen.blit(variable.Small_write.render("pieces : " + str(variable.pieces_utilisables), False, (0, 0, 0)), (900, 105))

        if variable.condition_SkinColor_Buying.collidepoint(variable.mouse_x, variable.mouse_y) and pygame.mouse.get_pressed()[0]:
            variable.SkinColor_Buying_showing = True
        variable.structure_magasin()
        variable.screen.blit(variable.Small_write.render("pieces : " + str(variable.pieces_utilisables), False, (0, 0, 0)),(900, 105))

        if variable.SkinColor_Buying_showing:
            variable.theBuyingofthteskincolor()


        if variable.back_magasin.collidepoint(variable.mouse_x, variable.mouse_y) and pygame.mouse.get_pressed()[0]:
            variable.condition_magasin = False
            variable.home = True
            variable.SkinColor_Buying = False
        if variable.condition_monde2_rect.collidepoint(variable.mouse_x,variable.mouse_y) and pygame.mouse.get_pressed()[0] and variable.pieces_utilisables < 5:
            variable.screen.blit(variable.title.render("Pas assez de pieces", False, (220, 0, 0)),(60, 100))

        if variable.condition_monde2_rect.collidepoint(variable.mouse_x, variable.mouse_y) and pygame.mouse.get_pressed()[0] and variable.pieces_utilisables >= 5:
            time.sleep(0.5)
            variable.condition_monde2 = True
            variable.message_erreur = False
            variable.pieces_utilisables -= 5
            #with open("variable.json", "w") as file:
                #json.dump(data_modifiee, file)
    if variable.condition_locker:
        variable.screen.blit(variable.image_casier,(0, 0))
        variable.skin_color()
        pygame.draw.rect(variable.screen, (0, 0, 0), (400, 60, 220, 50))
        variable.screen.blit(variable.title.render('Casier', False, (255, 0, 0)), (410, 60))

        variable.screen.blit(variable.verySmall_write.render('Skin Actuel', False, (variable.normal_color)), (250, 400))
        pygame.draw.rect(variable.screen, variable.normal_color, (430, 390, 50, 50))
        back_locker = pygame.draw.rect(variable.screen, (255, 0, 0), (0, 5, 65, 75))
        variable.screen.blit(variable.verySmall_write.render('Back', False, (0, 0, 0)), (0, 25))
        if back_locker.collidepoint(variable.mouse_x, variable.mouse_y) and pygame.mouse.get_pressed()[0]:
            variable.condition_locker = False
            variable.home = True
        variable.SkinColor_dress()
    pygame.display.flip()
    clock.tick(60)

#with open("variable.json", "w") as file:
    #json.dump(data_modifiee, file)
pygame.quit()
