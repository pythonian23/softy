import numpy as np
from .link import Link


class Node:
    def __init__(self, name, mass, loc=(0, 0)):
        self.name = name

        self.loc = np.array(loc, dtype="float32")
        self.mass = mass
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
        acc = self._force_sum / self.mass
        self.loc += (self.velocity + acc / 2) * dt  # assume linear increase
        self.velocity += acc
        self.reset()

    def apply_force(self, force: np.ndarray):
        self._force_sum += force

    def reset(self):
        self._force_sum[:] = 0
