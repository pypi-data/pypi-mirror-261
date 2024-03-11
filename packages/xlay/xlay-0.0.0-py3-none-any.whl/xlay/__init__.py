"""
The library models the layout of a beamline.

A Layout is a collections of elements in positions and orientations.

A Pose is a position and orientation in 3D space and can contain a reference to an element.

An element specify an object in space, could be primitive, such as a square or complex such as an assembly of elements.

An assembly is a container of parts specified by elements at a given pose.

pose[key] returns  Pose(element[key],name=f"{pose.name}/{key}").

An element has a render method that returns a list of primitives and their poses for diplsaying the element.






"""

__version__="0.0.0"


from .pose import Pose
from .primitives import Line, Curve, Polyline, Polygon, Text, Bend, Ellipse, Circle, Box, Tube
from .assembly import Assembly, Magnet
from .layout import Beamline, Node, Layout
