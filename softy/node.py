import numpy as np
from .edge import Edge


class Node:
    def __init__(self, mass, loc=(0, 0)):
        self.loc = np.array(loc, dtype="float32")
        self.mass = mass
        self.velocity = np.zeros(2, dtype="float32")
        self._force_sum = np.zeros(2, dtype="float32")

        self._edges: list[Edge] = []

    def connect(self, node: Node):
        self._edges.append(Edge(self, node))

    def tick(self, dt):
        acc = self._force_sum / self.mass
        self.loc += (self.velocity + acc / 2) * dt  # assume linear increase
        self.velocity += acc
        self.reset()

    def apply_force(self, force: np.ndarray):
        self._force_sum += force

    def reset(self):
        self._force_sum.zero()