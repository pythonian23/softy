from .node import Node
from .link import Link

from typing import Any

import yaml


class Object:
    def __init__(self):
        self.name = None
        self.nodes: dict[Any, Node] = {}
        self._init = False

    def deinit(self):
        self.__init__()

    def load(self, file):
        if self._init:
            raise RuntimeError(
                "Object already initialized. Run the deinit method to reuse."
            )
        data = yaml.safe_load(file)
        self.name = data["Name"]
        for name, node in data["Nodes"].items():
            self.nodes[name] = Node(name, node["mass"], loc=(node["x"], node["y"]))
        for edge in data["Edges"]:
            self.nodes[edge["start"]].connect_forward(
                self.nodes[edge["end"]], edge["spring"]
            )

    def dump(self, file):
        ...
