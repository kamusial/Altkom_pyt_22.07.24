from collections import namedtuple

# tworzenie klasy krotki
Point = namedtuple('Point', ['x', 'y'])

# tworzenie instancji
p = Point(10, 20)

print(p.x, p.y)
print(p[0], p[1])