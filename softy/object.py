from .node import Node

from typing import Any

import yaml


class Object:
    def __init__(self):
        self.name = None
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
        yaml.dump(data, file)
