"""
name is for access
label is for presentation


render output options:

1) flat list of transformation, primitive
2) flat list of Point(primitive) 


"""

import matplotlib.pyplot as plt
import numpy as np

from .pose import (
    Pose,
    Line,
    Curve,
    Polyline,
    Polygon,
    Text,
    Bend,
    Ellipse,
    Circle,
    Box,
)


def resolve_style(style, primitive, layer, name):
    if style is None:
        style = {}
    if layer in style:
        style = {**style, **style[layer]}
    if name in style:
        style = {**style, **style[name]}
    if primitive.__class__.__name__ in style:
        style = {**style, **style[primitive.__class__.__name__]}


class SimpleProjection:
    def __init__(self, axes="xy"):
        self.axes = axes
        self.idx0 = {"x": 0, "y": 1, "z": 2}[axes[0]]
        self.idx1 = {"x": 1, "y": 2, "z": 0}[axes[1]]

    def transform(self, points):
        """Transform points from 3D to 2D

        Args:
            points np.ndarray 3xN: N 3D points in columns
        """
        return points[self.idx0], points[self.idx1]


class Canvas2D:
    default_style = {}

    def __init__(self, projection="xy", center=[0, 0], scale=1, units="m", style=None):
        if isinstance(projection, str):
            self.projection = SimpleProjection(projection)
        else:
            self.projection = projection
        if style is None:
            style = Canvas2D.default_style
        self.center = center
        self.scale = scale
        self.units = units
        self.artists = {}
        self.elements = {}

    def add(self, element, key=None, style=None):
        if key is None:
            key = element.label
        self.elements[key] = (element, style)

    def initialize(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_aspect("equal")
        plt.show()

    def clear(self):
        self.ax.clear()

    def draw(self, style=None):
        self.clear()
        if style is not None:
            style = self.style
        for key, (element, style) in self.elements.items():
            for primitive in element.render(style):
                artists = self.draw_primitive(primitive, style)
                self.artists[key] = artists

    def draw_primitive(self, primitive, style):
        style = resolve_style(style, primitive, primitive.layer, primitive.name)
        if style.get("visible", True):
            args = dict(
                label=style.get("label", None),
                color=style.get("color", "black"),
                linewidth=style.get("linewidth", 1),
                linestyle=style.get("linestyle", "-"),
                marker=style.get("marker", None),
                markersize=style.get("markersize", 5),
                markerfacecolor=style.get("markerfacecolor", None),
                markeredgecolor=style.get("markeredgecolor", None),
                markeredgewidth=style.get("markeredgewidth", 1),
                alpha=style.get("alpha", 1),
                zorder=style.get("zorder", None),
            )
