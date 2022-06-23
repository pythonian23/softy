from .node import Node

import numpy as np


class Link:
    def __init__(self, start: Node, end: Node, spring=0):
        self.start = start
        self.end = end
        self.spring = spring
        self._neutral_length = np.linalg.norm(start.loc - end.loc)

    def apply_force(self, force: np.ndarray):
        self.start.apply_force(force)
        self.end.apply_force(force)
