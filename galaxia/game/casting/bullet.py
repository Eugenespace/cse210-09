from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.gameconstants import *
import pygame
from pygame import mixer


class Bullet(Actor):
    """
    """
    # The actor sound
    pygame.mixer.init()
    actor_sound = mixer.Sound(ACTOR_SOUND)

    def __init__(self, pos, direction):
        """
        """
        super().__init__()
        self.set_center(pos)
        self._dead = False
        if (direction == 0):
            self.set_image(BULLET_IMAGE)
            self.set_center(pos)
            self.set_velocity(Point(20, 0))
            self.actor_sound.play()
        if (direction == 1):
            self.set_image(BULLET_ENEMY_IMAGE)
            self.set_center(pos)
            self.set_velocity(Point(-15, 0))
            self.actor_sound.play()
