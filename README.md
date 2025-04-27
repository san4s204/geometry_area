## Возможности

* **Круг** — площадь по радиусу  
* **Треугольник** — площадь по трём сторонам (формула Герона) + метод `is_right()`  
* **Полиморфный API** — универсальная функция `area(shape)` работает с любой фигурой  
* **Простое расширение** — наследуйтесь от абстрактного класса `Shape` и переопределите `area()`  
* **100 % покрытие юнит-тестами** — тесты на `unittest` встроены прямо в файл

---

## Установка

Сборка не требуется — библиотека состоит из одного файла.

```bash
git clone https://github.com/san4s204/geometry_area.git
cd geometry
```

## Быстрый старт

```python
from geometry import Circle, Triangle, area

print(area(Circle(2)))          # → 12.566370614359172
t = Triangle(3, 4, 5)
print(t.area())                 # → 6.0
print(t.is_right())             # → True
```

## Добавление собственной фигуры
```python
from geometry import Shape, area

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.w, self.h = width, height

    def area(self) -> float:
        return self.w * self.h

print(area(Rectangle(4, 2)))    # → 8
```
Никаких изменений в другом коде не нужно — полиморфная area() уже готова.
