# libraries
import pygame


# class to manage the ship
class Ship:
    # initialise the ship and starting position
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load("img/ship.bmp")
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    # draw the ship at its current location
    def blitme(self):
        self.screen.blit(self.image, self.rect)
