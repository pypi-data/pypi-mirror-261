from dataclasses import dataclass, field, is_dataclass, asdict
from typing import List, Optional
import json

class DataclassJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        return super().default(o)

@dataclass
class Color:
    value: str  # Expected in hex format, e.g. "#FFFFFF"

@dataclass
class Node:
    id: str
    type: str
    x: int
    y: int
    width: int
    height: int

@dataclass
class TextNode(Node):
    text: str
    color: Optional[Color] = None

@dataclass
class FileNode(Node):
    file: str
    subpath: Optional[str] = None
    color: Optional[Color] = None

@dataclass
class LinkNode(Node):
    url: str
    color: Optional[Color] = None

@dataclass
class GroupNode(Node):
    label: Optional[str] = None
    background: Optional[str] = None
    backgroundStyle: Optional[str] = None
    color: Optional[Color] = None

@dataclass
class Edge:
    id: str
    fromNode: str
    toNode: str
    fromSide: Optional[str] = None
    fromEnd: Optional[str] = None
    toSide: Optional[str] = None
    toEnd: Optional[str] = None
    color: Optional[Color] = None
    label: Optional[str] = None

@dataclass
class Canvas:
    nodes: Optional[List[Node]] = field(default_factory=list)
    edges: Optional[List[Edge]] = field(default_factory=list)


def export(canvas: Canvas, filename: str):
    with open(filename, "w") as f:
        json.dump(canvas, f, cls=DataclassJSONEncoder) 