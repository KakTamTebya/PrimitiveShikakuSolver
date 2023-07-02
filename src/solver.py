from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class FieldNumber:
    value: int
    location: Point


class Rectangle:
    def __init__(self, top_left: Point, width: int, height: int) -> None:
        self.top_left = top_left
        self.width = width
        self.height = height

    def is_intersected_with(self, other) -> bool:
        return max(self.top_left.x, other.top_left.x) <= min(
            self.top_left.x + self.width - 1,
            other.top_left.x + other.width - 1) \
            and max(self.top_left.y, other.top_left.y) <= min(
                self.top_left.y + self.height - 1,
                other.top_left.y + other.height - 1)

    def contains_point(self, point: Point) -> bool:
        return self.top_left.x <= point.x < self.top_left.x + self.width and \
            self.top_left.y <= point.y < self.top_left.y + self.height

    def __repr__(self):
        return f"Rectangle({self.top_left.x}, {self.top_left.y}, " \
               f"{self.width}, {self.height})"

    def __str__(self):
        return repr(self)

    def __eq__(self, other):
        return self.top_left == other.top_left and self.width == other.width \
            and self.height == other.height

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return 1337 * (1337 ** 2 * self.top_left.x + 1337 * self.top_left.y
                       + self.width) + self.height


def solve(numbers, size_x, size_y):
    def is_valid_position(rect_list: [Rectangle], rect: Rectangle) -> bool:
        for x in range(rect.top_left.x, rect.top_left.x + rect.width):
            for y in range(rect.top_left.y):
                for r in rect_list:
                    if r.contains_point(Point(x, y)):
                        break
                else:
                    return False
        return True

    def is_valid_rect(rect_list: [Rectangle], rect: Rectangle,
                      index: int) -> bool:
        if rect.top_left.x < 0 or rect.top_left.x + rect.width > size_x or \
                rect.top_left.y < 0 or rect.top_left.y + rect.height > size_y:
            return False
        for r in rect_list:
            if rect.is_intersected_with(r):
                return False
        for n in numbers[index + 1:]:
            if rect.contains_point(n.location):
                return False
        return True

    def continue_recursion(rect_list: [Rectangle], rect: Rectangle, index: int,
                           used: {Rectangle}) -> None:
        if rect not in used:
            used.add(rect)
            if is_valid_rect(rect_list, rect, index):
                new_rect_list = rect_list.copy()
                new_rect_list.append(rect)
                if index == len(numbers) - 1:
                    answers.append(new_rect_list)
                elif is_valid_position(new_rect_list, rect):
                    all_options(new_rect_list, index + 1)

    def all_options(rect_list: [Rectangle], index=0) -> None:
        n = numbers[index]
        for i in range(1, int(n.value ** 0.5) + 1):
            if n.value % i == 0:
                height, width, used = i, n.value // i, set()
                for q in range(width):
                    for t in range(height):
                        r1 = Rectangle(Point(n.location.x - t,
                                             n.location.y - q), height, width)
                        r2 = Rectangle(Point(n.location.x - q,
                                             n.location.y - t), width, height)
                        continue_recursion(rect_list, r1, index, used)
                        continue_recursion(rect_list, r2, index, used)

    if sum([i.value for i in numbers]) != size_x * size_y:
        return []
    answers = []
    all_options([])
    return answers
