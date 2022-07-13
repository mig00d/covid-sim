import pygame

from circle import Circle

# constantes
WIDTH = 1500
HEIGHT = 800
BACKGROUND = (255, 255, 255)
FPS = 60
NUMBER_OF_CIRCLE = 30

# parametre fenetre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('SIM COVID')
screen.fill(BACKGROUND)

# creation de tout les cercles, les afficher et les stocker dans la liste
list_circle = []
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

                # check le cercle qui a été touché pour mettre dans la liste des infectés
                for circle_touched in list_circle:
                    if circle_touched.check_collision(infected.x, infected.y):
                        list_circle.remove(circle)
                        list_infected.append(circle)

    # rafraichir les changements et remetre la couleur du fond pour pas de "trainée"
    pygame.display.flip()
    screen.fill(BACKGROUND)

    # configurer les FPS ( frames par seconde )
    clock.tick(FPS)

pygame.quit()
