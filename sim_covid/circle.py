import pygame
import random


class Circle(pygame.sprite.Sprite):
    def __init__(self, width, height, surface, infected):
        super().__init__()

        # definie si il est infecter ou pas
        self.infected = infected

        # instancier les parametres
        self.size_circle = (30, 30)
        self.width = width
        self.height = height
        self.surface = surface

        # mettre la bonne couleur au patien zero
        if infected:
            self.image = pygame.image.load('circle_green.png')
        else:
            self.image = random.choice([pygame.image.load('circle_blue.png'), pygame.image.load('circle_red.png')])

        # mettre l'image a la bonne taille
        self.image = pygame.transform.scale(self.image, self.size_circle)

        # position de depart aleatoire
        self.x = random.randint(30, width - 30)
        self.y = random.randint(30, height - 30)

        # proprieter autre
        self.velocity = 2
        self.direction_x = 0
        self.direction_y = 0

        # direction aleatoire au debut
        while self.direction_x == 0 and self.direction_y == 0:
            self.direction_x = random.uniform(-1, 1)
            self.direction_y = random.uniform(-1, 1)

    # permet de dire si il deux objets se touche
    def check_collision(self, x, y) -> bool:
        if 30 > self.x - x > -30 and 30 > self.y - y > -30:
            return True
        else:
            return False

    # transforme un cercle en infecté
    def transform(self, x, y):
        self.image = pygame.image.load('circle_green.png')
        self.size_circle = (30, 30)
        self.image = pygame.transform.scale(self.image, self.size_circle)
        self.x = x
        self.y = y

    # fonction pour faire bouger le cercle et le faire rebondire au limite de la fenetre
    def move(self):
        if self.x > self.width - 30 or self.x < 0:
            self.direction_x *= -1

        if self.y > self.height - 30 or self.y < 0:
            self.direction_y *= -1

        self.x += self.velocity * self.direction_x
        self.y += self.velocity * self.direction_y

        self.surface.blit(self.image, (self.x, self.y))
