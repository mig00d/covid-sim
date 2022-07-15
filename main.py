import pygame

from circle import Circle

# stock les points entre chaque experience
data = []

# variables du compteur
counter = 0

# constantes
WIDTH = 1500
HEIGHT = 800
BACKGROUND = (255, 255, 255)
FPS = 60
NUMBER_OF_CIRCLE = 100
FORGROUND_TEXT = (255, 255, 255)

NUMBER_EXPERIENCE = 10  # nombre d'experience

SIZE_CIRCLE = (50, 50)
VELOCITY_CIRCLE = 8

leaving = False

# ------------------------------------------------------------------------------------------------------------------------
for experience in range(NUMBER_EXPERIENCE + 1):
    pygame.init()

    # parametre fenetre
    pygame.display.set_caption('SIM COVID')
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(BACKGROUND)

    # appeler l'horloge ( regleur fps )
    clock = pygame.time.Clock()

    # creation de tout les cercles, les afficher et les stocker dans la liste
    list_circle = []
    backup = None
    for i in range(NUMBER_OF_CIRCLE):
        list_circle.append(Circle(WIDTH, HEIGHT, screen, False, SIZE_CIRCLE, VELOCITY_CIRCLE))

    # creation du patient zero
    list_infected = [Circle(WIDTH, HEIGHT, screen, True, SIZE_CIRCLE, VELOCITY_CIRCLE)]

    # main loop
    running = True

    while running:

        # compte les frames
        counter += 1

        # evenements
        for events in pygame.event.get():

            # quitter la fenetre
            if events.type == pygame.QUIT:
                leaving = True
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
                    backup = circle
        try:
            list_circle.remove(backup)
            list_infected.append(backup)
            backup = None

        except:
            pass

        # rafraichir les changements et remetre la couleur du fond pour pas de "trainée"
        pygame.display.flip()
        screen.fill(BACKGROUND)

        # verifier que il n'y a plus de cercle non infecter pour lancer l'ecran de fin
        if len(list_circle) == 0:
            data.append(counter)
            print(data)
            counter = 0
            running = False

        # configurer les FPS ( frames par seconde )
        clock.tick(FPS)

    pygame.quit()

    if leaving:
        break

print('Simulation Terminer')
