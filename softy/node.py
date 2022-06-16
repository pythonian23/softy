import numpy as np


class Node:
    def __init__(self, mass, loc=(0, 0)):
        self.loc = np.array(loc, dtype="float32")
        self.mass = mass
        self.velocity = np.zeros(2, dtype="float32")
        self._force_sum = np.zeros(2, dtype="float32")

    def apply_force(self, force: np.ndarray):
        self._force_sum += force

    def reset(self):
        self._force_sum.zero()
