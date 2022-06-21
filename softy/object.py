from .node import Node

from typing import Any

import numpy as np
import yaml


class Object:
    def __init__(self):
        self.name = None
        self.pressure = 0
        self.nodes: dict[Any, Node] = {}
        self._init = False

    def init(self):
        self._init = True

    def deinit(self):
        self.__init__()

    def load(self, file):
        if self._init:
            raise RuntimeError(
                "Object already initialized. Run the deinit method to reuse."
            )
        data = yaml.safe_load(file)
        self.name = data["Name"]
        self.pressure = data["Pressure"]
        for name, node in data["Nodes"].items():
            self.nodes[name] = Node(name, node["mass"], loc=(node["x"], node["y"]))
        for name, node in data["Nodes"].items():
            self.nodes[name].connect(
                self.nodes[node["link"]["next"]], node["link"]["spring"]
            )
        self.init()

    def dump(self, file):
        data = {
            "Name": self.name,
            "Pressure": self.pressure,
            "Nodes": {
                name: {
                    "x": float(node.loc[0]),
                    "y": float(node.loc[1]),
                    "mass": node.mass,
                    "link": {"next": node.link.end.name, "spring": node.link.spring},
                }
                for name, node in self.nodes.items()
            },
        }
        yaml.safe_dump(data, file)

    def area(self) -> float:
        boundary = np.array([node.loc for node in self.nodes.values()], dtype="float32")
        return (
            np.abs(
                np.sum(boundary[:, 0] * np.roll(boundary[:, 1], -1))
                - np.sum(boundary[:, 0] * np.roll(boundary[:, 1], 1))
            )
            / 2
        )
