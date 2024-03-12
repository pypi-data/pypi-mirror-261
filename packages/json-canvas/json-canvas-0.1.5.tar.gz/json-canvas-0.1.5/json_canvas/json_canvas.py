from dataclasses import dataclass, field, is_dataclass, asdict
from typing import List, Optional
import json
import random
import time
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
def generate_random_color():
    # Generate a random hex color code
    return Color(value=f"#{random.randint(0, 0xFFFFFF):06X}")

def generate_random_node(node_type, canvas_width, canvas_height):
    # Generate a random Node with random values
    return Node(
        id=str(random.randint(1, 100)),
        type=node_type,
        x=random.randint(0, canvas_width),
        y=random.randint(0, canvas_height),
        width=random.randint(50, 200),
        height=random.randint(50, 200)
    )

def generate_random_text_node(canvas_width, canvas_height):
    # Generate a random TextNode with random text and color
    return TextNode(
        id=str(random.randint(1, 100)),
        type="text",
        x=random.randint(0, canvas_width),
        y=random.randint(0, canvas_height),
        width=random.randint(50, 200),
        height=random.randint(50, 200),
        text=f"Random Text {random.randint(1, 100)}",
        color=generate_random_color()
    )

def generate_random_file_node(canvas_width, canvas_height):
    # Generate a random FileNode with random file and color
    return FileNode(
        id=str(random.randint(1, 100)),
        type="file",
        x=random.randint(0, canvas_width),
        y=random.randint(0, canvas_height),
        width=random.randint(50, 200),
        height=random.randint(50, 200),
        file=f"random_file_{random.randint(1, 100)}.txt",
        subpath=f"subfolder/{random.randint(1, 10)}",
        color=generate_random_color()
    )

def generate_random_link_node(canvas_width, canvas_height):
    # Generate a random LinkNode with random URL and color
    return LinkNode(
        id=str(random.randint(1, 100)),
        type="link",
        x=random.randint(0, canvas_width),
        y=random.randint(0, canvas_height),
        width=random.randint(50, 200),
        height=random.randint(50, 200),
        url=f"https://example.com/{random.randint(1, 100)}",
        color=generate_random_color()
    )

def generate_random_group_node(canvas_width, canvas_height):
    # Generate a random GroupNode with random label, background, and color
    return GroupNode(
        id=str(random.randint(1, 100)),
        type="group",
        x=random.randint(0, canvas_width),
        y=random.randint(0, canvas_height),
        width=random.randint(50, 200),
        height=random.randint(50, 200),
        label=f"Group {random.randint(1, 100)}",
        background=f"#{random.randint(0, 0xFFFFFF):06X}",
        backgroundStyle="random_style",
        color=generate_random_color()
    )

def generate_random_edge(nodes):
    # Generate a random Edge connecting two random nodes
    from_node = random.choice(nodes)
    to_node = random.choice(nodes)
    return Edge(
        id=str(random.randint(1, 100)),
        fromNode=from_node.id,
        toNode=to_node.id,
        color=generate_random_color(),
        label=f"Edge from {from_node.id} to {to_node.id}"
    )

def generate_random_canvas(num_nodes, num_edges, canvas_width, canvas_height):
    # Generate a random Canvas with the specified number of nodes and edges
    nodes = []
    edges = []

    for _ in range(num_nodes):
        node_type = random.choice(["text", "file", "link", "group"])
        if node_type == "text":
            node = generate_random_text_node(canvas_width, canvas_height)
        elif node_type == "file":
            node = generate_random_file_node(canvas_width, canvas_height)
        elif node_type == "link":
            node = generate_random_link_node(canvas_width, canvas_height)
        else:
            node = generate_random_group_node(canvas_width, canvas_height)
        nodes.append(node)

    for _ in range(num_edges):
        edge = generate_random_edge(nodes)
        edges.append(edge)

    return Canvas(nodes=nodes, edges=edges)

def generate_random_canvas_wrapper(num_nodes_mean, num_nodes_std, num_edges_mean, num_edges_std, canvas_width_mean, canvas_width_std, canvas_height_mean, canvas_height_std):
    # Generate random values based on statistical distributions
    num_nodes = int(random.gauss(num_nodes_mean, num_nodes_std))
    num_edges = int(random.gauss(num_edges_mean, num_edges_std))
    canvas_width = int(random.gauss(canvas_width_mean, canvas_width_std))
    canvas_height = int(random.gauss(canvas_height_mean, canvas_height_std))

    return generate_random_canvas(num_nodes, num_edges, canvas_width, canvas_height)

def generate_and_export_random_canvas(num_nodes_mean, num_nodes_std, num_edges_mean, num_edges_std, canvas_width_mean, canvas_width_std, canvas_height_mean, canvas_height_std, filename):
    start_time = time.time()

    random_canvas = generate_random_canvas_wrapper(num_nodes_mean, num_nodes_std, num_edges_mean, num_edges_std, canvas_width_mean, canvas_width_std, canvas_height_mean, canvas_height_std)

    export(random_canvas, filename)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Random canvas generated and exported in {elapsed_time:.4f} seconds.")