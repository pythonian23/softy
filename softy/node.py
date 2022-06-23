import numpy as np
from .link import Link


class Node:
    def __init__(self, name, mass, loc=(0, 0)):
        self._precalc = Precalculated()

        self.name = name

        self.loc = np.array(loc, dtype="float32")
        self._mass = 0
        self.set_mass(mass)
        self.velocity = np.zeros(2, dtype="float32")
        self._force_sum = np.zeros(2, dtype="float32")

        self.link: Link = ...

    def connect(self, node, spring):
        """
        Connect another node as the next node. This connects both ways.
        """
        link = Link(self, node, spring=spring)
        self.link = link

    def tick(self, dt):
        acc = self._force_sum * self._precalc.divide_by_mass
        self.loc += (self.velocity + acc / 2) * dt  # assume linear increase
        self.velocity += acc
        self.reset()

    def apply_force(self, force: np.ndarray):
        self._force_sum += force

    def reset(self):
        self._force_sum[:] = 0

    def set_mass(self, mass):
        self._mass = mass
        self._precalc.divide_by_mass = 1 / mass

    def get_mass(self):
        return self._mass


class Precalculated:
    def __init__(self):
        self.divide_by_mass = 0
