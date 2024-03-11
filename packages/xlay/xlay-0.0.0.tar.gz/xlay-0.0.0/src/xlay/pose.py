"""
A Point describe a position in a 3D space: location and orientation.
A Point can hold an assembly to specify the position of that assembly.

Manages reference frames and transformations.


Potential decision: 
- Pose(pose) copies the matrix


"""

import numpy as np
from scipy.spatial.transform import Rotation, Slerp

class Pose:
    def __init__(
        self,
        x=0,
        y=0,
        z=0,
        dx=[1, 0, 0],
        dy=[0, 1, 0],
        dz=[0, 0, 1],
        matrix=None,
        loc=None,
        rot=None,
        element=None,
        name=None,
        label=None,
        layer=None,
    ):
        if matrix is None:
            if loc is not None:
                x, y, z = loc
            if rot is not None:
                dx, dy, dz = rot.T
            self.matrix = np.array(
                [
                    [dx[0], dy[0], dz[0], x],
                    [dx[1], dy[1], dz[1], y],
                    [dx[2], dy[2], dz[2], z],
                    [0, 0, 0, 1],
                ],
                dtype=float,
            )
        elif isinstance(matrix, np.ndarray):
            self.matrix = matrix
        elif hasattr(matrix, "matrix"):
            self.matrix = matrix.matrix
        self.name = name
        self.label = label
        self.layer = layer
        self.element = element

    def __repr__(self):
        args = []
        if self.name is not None:
            args.append(f"name={self.name}")
        if self.x != 0:
            args.append(f"x={self.x}")
        if self.y != 0:
            args.append(f"y={self.y}")
        if self.z != 0:
            args.append(f"z={self.z}")
        return f"Pose({', '.join(args)})"

    @property
    def x(self):
        return self.matrix[0, 3]

    @x.setter
    def x(self, value):
        self.matrix[0, 3] = value

    @property
    def y(self):
        return self.matrix[1, 3]

    @y.setter
    def y(self, value):
        self.matrix[1, 3] = value

    @property
    def z(self):
        return self.matrix[2, 3]

    @z.setter
    def z(self, value):
        self.matrix[2, 3] = value

    @property
    def dx(self):
        return self.matrix[:3, 0]

    @dx.setter
    def dx(self, value):
        self.matrix[:3, 0] = value

    @property
    def dy(self):
        return self.matrix[:3, 1]

    @dy.setter
    def dy(self, value):
        self.matrix[:3, 1] = value

    @property
    def dz(self):
        return self.matrix[:3, 2]

    @dz.setter
    def dz(self, value):
        self.matrix[:3, 2] = value

    @property
    def loc(self):
        return self.matrix[:3, 3]

    @loc.setter
    def loc(self, value):
        self.matrix[:3, 3] = value

    @property
    def rot(self):
        return self.matrix[:3, :3]

    @rot.setter
    def rot(self, value):
        self.matrix[:3, :3] = value

    @property
    def n(self):
        return self.new()

    @property
    def c(self):
        return self.clone()

    def __mul__(self, other):
        matrix = self.matrix.copy()
        matrix[:3, :3] = matrix[:3, :3] @ other.matrix[:3, :3]
        return self.clone(matrix=matrix)

    def __matmul__(self, other):
        matrix = self.matrix.copy()
        matrix = matrix @ other.matrix
        return self.clone(matrix=matrix)

    def __add__(self, other):
        matrix = self.matrix.copy()
        matrix[:3, 3] += other.matrix[:3, 3]
        return self.clone(matrix=matrix)

    def tx(self, x):
        self.matrix = np.dot(
            self.matrix,
            np.array([[1, 0, 0, x], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]),
        )
        return self

    def ty(self, y):
        self.matrix = np.dot(
            self.matrix,
            np.array([[1, 0, 0, 0], [0, 1, 0, y], [0, 0, 1, 0], [0, 0, 0, 1]]),
        )
        return self

    def tz(self, z):
        self.matrix = np.dot(
            self.matrix,
            np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, z], [0, 0, 0, 1]]),
        )
        return self

    def rx(self, angle):
        angle_rad = np.radians(angle)
        cx = np.cos(angle_rad)
        sx = np.sin(angle_rad)
        self.matrix = np.dot(
            self.matrix,
            np.array(
                [
                    [1, 0, 0, 0],
                    [0, cx, -sx, 0],
                    [0, sx, cx, 0],
                    [0, 0, 0, 1],
                ]
            ),
        )
        return self

    def ry(self, angle):
        angle_rad = np.radians(angle)
        cx = np.cos(angle_rad)
        sx = np.sin(angle_rad)
        self.matrix = np.dot(
            self.matrix,
            np.array(
                [
                    [cx, 0, sx, 0],
                    [0, 1, 0, 0],
                    [-sx, 0, cx, 0],
                    [0, 0, 0, 1],
                ]
            ),
        )
        return self

    def rz(self, angle):
        angle_rad = np.radians(angle)
        cx = np.cos(angle_rad)
        sx = np.sin(angle_rad)
        self.matrix = np.dot(
            self.matrix,
            np.array(
                [
                    [cx, -sx, 0, 0],
                    [sx, cx, 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1],
                ]
            ),
        )
        return self

    def clone(self, **kwargs):
        """Return a full clone of the current pose"""
        newargs = {**self.__dict__, **kwargs}
        return Pose(**newargs)

    def new(self, **kwargs):
        """Return a new pose with the same matrix as self"""
        return Pose(matrix=self.matrix, **kwargs)

    def distance(self, pose):
        return np.linalg.norm(self.matrix[:3, 3] - pose.matrix[:3, 3])

    def render(self, style=None):
        from .primitives import Text
        primitives = []
        if style.get("labels", False):
            label = self.name if self.label is None else self.label
            primitives.append(
                self.new(element=Text(text=label), name=self.name, layer=self.layer)
            )
        if self.element is not None:
            for primitive in self.element.render():
                primitive.transform(self)
                primitive.name = f"{self.name}/{primitive.name}"
                primitives.append(primitive)
        return primitives



