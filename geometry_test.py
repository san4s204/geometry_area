from geometry import Circle, Triangle, area

print("Площадь круга =", area(Circle(2)))            # 12.566...
t = Triangle(3, 4, 5)
print("Площадь треугольника = " ,t.area())                   # 6.0
print("Треугольник является прямоугольным:", t.is_right())               # True
