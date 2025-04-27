# geometry.py
from __future__ import annotations
from abc import ABC, abstractmethod
import math
import unittest


class Shape(ABC):
    """Базовый абстрактный класс для всех геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """Возвращает площадь фигуры."""
        raise NotImplementedError


class Circle(Shape):
    """Круг по радиусу."""

    def __init__(self, radius: float) -> None:
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self) -> str:  # удобно для отладки
        return f"Circle(radius={self.radius})"


class Triangle(Shape):
    """Треугольник по трём сторонам."""

    def __init__(self, a: float, b: float, c: float) -> None:
        if min(a, b, c) <= 0:
            raise ValueError("All sides must be positive")

        # проверка неравенства треугольника
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Sides do not form a valid triangle")

        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        """Площадь по формуле Герона."""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    # ---- специфичная функциональность ----
    def is_right(self, *, tol: float = 1e-9) -> bool:
        """True, если треугольник прямоугольный (по теореме Пифагора)."""
        sides = sorted((self.a, self.b, self.c))
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < tol

    def __repr__(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


# ------------------------------------------------------------
# Универсальная функция-обёртка (полиморфизм «по базе»)
# ------------------------------------------------------------
def area(shape: Shape) -> float:
    """
    Возвращает площадь любой фигуры, реализующей Shape,
    не зная её точного типа во время компиляции.
    """
    return shape.area()


# ============================================================
#                    UNIT-TESTS
# ============================================================
class GeometryTests(unittest.TestCase):
    def test_circle_area(self) -> None:
        self.assertAlmostEqual(Circle(1).area(), math.pi)

    def test_triangle_area(self) -> None:
        self.assertAlmostEqual(Triangle(3, 4, 5).area(), 6.0)

    def test_triangle_is_right(self) -> None:
        self.assertTrue(Triangle(3, 4, 5).is_right())
        self.assertFalse(Triangle(2, 3, 4).is_right())

    def test_invalid_circle(self) -> None:
        with self.assertRaises(ValueError):
            Circle(0)

    def test_invalid_triangle(self) -> None:
        with self.assertRaises(ValueError):
            Triangle(1, 2, 3)  # a + b == c ➜ не треугольник

    def test_generic_area_function(self) -> None:
        shapes = [Circle(2), Triangle(3, 4, 5)]
        areas = list(map(area, shapes))
        self.assertAlmostEqual(areas[0], math.pi * 4)
        self.assertAlmostEqual(areas[1], 6.0)


# Позволяет запускать тесты командой `python geometry.py`
if __name__ == "__main__":
    unittest.main()
