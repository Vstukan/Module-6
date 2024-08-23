class Figure:
    sides_count = 0

    def __init__(self, rgb, color: tuple, *sides: int, filled: bool = True):
        self.color = list(rgb)
        self.sides = [0]
        self.filled = True
        self.__color = color
    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r, self.g, self.b = r, g, b
        if 0 <= self.r <= 255 and 0 <= self.g <= 255 and 0 <= self.b <= 255:
            return True
        else:
            return False
    def set_color(self, r, g, b) :
        if self.__is_valid_color(r, g, b) is True:
            self.color = [self.r, self.g, self.b]
            return self.color
    def __is_valid_sides(self, *args):
        for side in self.sides:
            if len(self.sides) == self.sides_count and side > 0 and type(side) == int:
                return True
            else:
                return False

    def get_sides(self, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = sides
    def __len__ (self):
        return sum(self.sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides) and self.sides_count == len(self.new_sides):
            self._sides = self.new_sides
        else:
            return self.sides

class Circle(Figure):

       sides_count = 1

    def __radius(self):
        return self.__len__ * (2 / pi)

    def get_square(self) :
        return (self.__len__ ** 2) / (4 * pi)
class Triangle(Figure):
    sides_count = 3
    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self) :
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides: int, filled: bool = True) :
        super().__init__(color, *sides, filled)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else :
            self.__sides = [1 * self.sides_count]

    def get_sides(self) :
        return [*self.__sides]
    def get_volume(self):
        return self.__sides[1] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
