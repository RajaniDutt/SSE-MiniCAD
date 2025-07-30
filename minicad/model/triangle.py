from minicad.model.shape import Shape
from minicad.model.point import Point

from PySide6.QtGui import QPainter, QPolygon
from PySide6.QtCore import QRectF, QPoint

import math


class Triangle(Shape):
    def __init__(self, center: Point, side: float):
        super().__init__(center)
        self._side = side


    def draw(self, painter: QPainter) -> None:
        # TODO: Task 3 - Implement the drawing mechanism for a triangle
        height = (self._side * math.sqrt(3)) / 2

        p1 = QPoint(self._center.x, int(self._center.y - (2 / 3) * height))  # Top vertex
        p2 = QPoint(int(self._center.x - self._side / 2), int(self._center.y + (1 / 3) * height))  # Bottom-left
        p3 = QPoint(int(self._center.x + self._side / 2), int(self._center.y + (1 / 3) * height))  # Bottom-right


        triangle = QPolygon([p1, p2, p3])
        painter.drawPolygon(triangle)


        painter.drawText(self._center.x, self._center.y, str(self._id))
        pass

    # TODO: Task 4 - Implement the scale method
    def scale(self, scalingFactor: float) -> None:
        self._side *= scalingFactor
