from random import randint, choice
from src.solver import Rectangle, Point


def generate_puzzle(file_to_write_path: str, size_x=randint(5, 8),
                    size_y=randint(5, 8)) -> None:
    def get_lucky():
        return randint(1, 4) == 1

    def throw_coin():
        return randint(1, 2) == 1

    def divide_rectangle(rect: Rectangle, depth=0):
        nonlocal rectangles
        if depth > 1 and get_lucky():
            rectangles.append(rect)
        elif throw_coin() and rect.width > 1:
            if rect.height == 1:
                if rect.width > 3:
                    x = randint(2, rect.width - 2)
                else:
                    rectangles.append(rect)
                    return
            else:
                x = randint(1, rect.width - 1)
            divide_rectangle(
                Rectangle(rect.top_left, x, rect.height), depth + 1)
            divide_rectangle(
                Rectangle(Point(rect.top_left.x + x, rect.top_left.y),
                          rect.width - x, rect.height), depth + 1)
        elif rect.height > 1:
            if rect.width == 1:
                if rect.height > 3:
                    y = randint(2, rect.height - 2)
                else:
                    rectangles.append(rect)
                    return
            else:
                y = randint(1, rect.height - 1)
            divide_rectangle(
                Rectangle(rect.top_left, rect.width, y), depth + 1)
            divide_rectangle(
                Rectangle(Point(rect.top_left.x, rect.top_left.y + y),
                          rect.width, rect.height - y), depth + 1)
        else:
            rectangles.append(rect)

    rectangles = []
    divide_rectangle(Rectangle(Point(0, 0), size_x, size_y))
    field = [['-'] * size_x for _ in range(size_y)]
    for r in rectangles:
        y_r = randint(r.top_left.y, r.top_left.y + r.height - 1)
        x_r = randint(r.top_left.x, r.top_left.x + r.width - 1)
        if throw_coin() and get_lucky():
            sign = choice(['<', '>'])
            if sign == '>' and r.width * r.height > 1:
                value = randint(1, r.width * r.height - 1)
            else:
                value = randint(r.width * r.height + 1, size_x * size_y + 1)
            field[y_r][x_r] = sign + str(value)
        else:
            field[y_r][x_r] = str(r.width * r.height)
    with open(file_to_write_path, "w") as file:
        for line in field:
            file.write(' '.join(line) + '\n')
