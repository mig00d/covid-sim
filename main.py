import pygame
import time

from circle import Circle

pygame.init()

# constantes
WIDTH = 1500
HEIGHT = 800
BACKGROUND = (255, 255, 255)
FPS = 90
NUMBER_OF_CIRCLE = 10

FORGROUND_TEXT = (255, 255, 255)
FINAL_BACKGROUND = (0, 0, 0)
FONT = pygame.font.Font('freesansbold.ttf', 60)
TEXT = FONT.render('FIN', True, FORGROUND_TEXT, FINAL_BACKGROUND)
TEXTRECT = TEXT.get_rect()
TEXTRECT.center = (WIDTH // 2, HEIGHT // 2)

# parametre fenetre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SIM COVID')
screen.fill(BACKGROUND)

# creation de tout les cercles, les afficher et les stocker dans la liste
list_circle = []
backup = []
for i in range(NUMBER_OF_CIRCLE):
    list_circle.append(Circle(WIDTH, HEIGHT, screen, False))

# creation du patient zero
list_infected = [Circle(WIDTH, HEIGHT, screen, True)]

# appeler l'horloge ( regleur fps )
clock = pygame.time.Clock()

# main loop
running = True

while running:

    # evenements
    for events in pygame.event.get():

        # quitter la fenetre
        if events.type == pygame.QUIT:
            running = False

    # faire bouger les infectés
    for infected in list_infected:
        infected.move()

    # faire bouger tout les cercles
    for circle in list_circle:
        circle.move()

        for infected in list_infected:

            # check les collisions des infectés et transforme le cercle touché
            if infected.check_collision(circle.x, circle.y):
                circle.transform(circle.x, circle.y)

                # check le cercle qui a été touché pour mettre dans la liste de sauvegarde
                for circle_touched in list_circle:
                    if circle_touched.check_collision(infected.x, infected.y):
                        backup.append(circle_touched)
    try:
        list_circle.remove(backup[0])
        print('list_circle', list_circle)
        list_infected.append(backup[0])
        print('list_infected: ', list_infected)
        backup.remove(backup[0])
        print('backup: ', backup)

    except:
        print('a rien touché')

    # verifier que il n'y a plus de cercle non infecter pour lancer l'ecran de fin
    if len(list_circle) == 0:
        time.sleep(1)
        screen.fill(FINAL_BACKGROUND)  # ecran de fin en noir
        screen.blit(TEXT, TEXTRECT)
        pygame.display.flip()

    # rafraichir les changements et remetre la couleur du fond pour pas de "trainée"
    pygame.display.flip()
    screen.fill(BACKGROUND)

    # configurer les FPS ( frames par seconde )
    clock.tick(FPS)

pygame.quit()
